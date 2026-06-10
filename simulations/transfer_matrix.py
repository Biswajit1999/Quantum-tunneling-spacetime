"""
Exact transmission through piecewise-constant 1D potentials (transfer matrices).

Units: hbar = m = 1.

Provides
--------
transmission_square(E, V0, a)   : analytic square-barrier T(E)
transfer_matrix_T(E, xs, Vs)    : general piecewise-constant T(E)
phase_time(E, V0, a)            : Wigner phase (group) time -> Hartman effect

Run as a script to generate figures/transmission.png and figures/hartman.png.
"""
from __future__ import annotations

import numpy as np

HBAR = 1.0
MASS = 1.0


def transmission_square(E: np.ndarray, V0: float, a: float) -> np.ndarray:
    """Analytic T(E) for a rectangular barrier of height V0, width a."""
    E = np.asarray(E, dtype=float)
    T = np.empty_like(E)
    below = E < V0
    above = E > V0
    at = ~(below | above)

    Eb = E[below]
    kap = np.sqrt(2.0 * MASS * (V0 - Eb)) / HBAR
    T[below] = 1.0 / (1.0 + (V0**2 * np.sinh(kap * a) ** 2)
                      / (4.0 * Eb * (V0 - Eb)))

    Ea = E[above]
    kp = np.sqrt(2.0 * MASS * (Ea - V0)) / HBAR
    T[above] = 1.0 / (1.0 + (V0**2 * np.sin(kp * a) ** 2)
                      / (4.0 * Ea * (Ea - V0)))

    T[at] = 1.0 / (1.0 + MASS * V0 * a**2 / (2.0 * HBAR**2))
    return T


def _wavenumber(E: float, V: float) -> complex:
    """k in a region of constant potential V (possibly evanescent)."""
    return np.sqrt(complex(2.0 * MASS * (E - V))) / HBAR


def transfer_matrix_T(E: float, xs: np.ndarray, Vs: np.ndarray) -> float:
    """
    Transmission for a piecewise-constant potential (exact).

    Region j has constant potential Vs[j]; interfaces sit at xs (sorted,
    length n-1 for n regions). In each region
    psi_j = A_j e^{i k_j x} + B_j e^{-i k_j x}, and continuity of psi, psi'
    at x_j gives (A_{j+1}, B_{j+1}) = M_j (A_j, B_j) with the explicit-phase
    interface matrix below. Incident from the left: A_1 = 1, B_n = 0, so
    t = det(M)/M22 = M11 - M12 M21 / M22.

    Assumes Vs[0] == Vs[-1] = lead potential; returns 0 for E below the lead.
    """
    xs = np.asarray(xs, float)
    Vs = np.asarray(Vs, float)
    assert len(Vs) == len(xs) + 1, "need n region potentials for n-1 interfaces"
    if E <= Vs[0]:
        return 0.0

    ks = [_wavenumber(E, V) for V in Vs]
    M = np.eye(2, dtype=complex)
    for j, xj in enumerate(xs):
        k1, k2 = ks[j], ks[j + 1]
        m11 = 0.5 * (1 + k1 / k2) * np.exp(1j * (k1 - k2) * xj)
        m12 = 0.5 * (1 - k1 / k2) * np.exp(-1j * (k1 + k2) * xj)
        m21 = 0.5 * (1 - k1 / k2) * np.exp(1j * (k1 + k2) * xj)
        m22 = 0.5 * (1 + k1 / k2) * np.exp(-1j * (k1 - k2) * xj)
        M = np.array([[m11, m12], [m21, m22]], dtype=complex) @ M
    # incident from left: t = 1 / M22* ... with this convention:
    t = M[0, 0] - M[0, 1] * M[1, 0] / M[1, 1]
    return float(abs(t) ** 2 * (ks[-1].real / ks[0].real))


def transmission_amplitude_square(E: float, V0: float, a: float) -> complex:
    """Complex transmission amplitude t(E) for the square barrier (for phase time)."""
    k = np.sqrt(2 * MASS * E) / HBAR
    q = _wavenumber(E, V0)
    # standard result, barrier on [0, a]
    denom = (np.cos(q * a) - 0.5j * (q / k + k / q) * np.sin(q * a))
    return np.exp(-1j * k * a) / denom


def phase_time(E: float, V0: float, a: float, dE: float = 1e-6) -> float:
    """Wigner phase (group) time tau = hbar d(arg t)/dE, numerically."""
    p1 = np.angle(transmission_amplitude_square(E - dE, V0, a))
    p2 = np.angle(transmission_amplitude_square(E + dE, V0, a))
    dphi = np.unwrap([p1, p2])[1] - np.unwrap([p1, p2])[0]
    return HBAR * dphi / (2 * dE)


def main() -> None:
    import pathlib
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    outdir = pathlib.Path(__file__).parent / "figures"
    outdir.mkdir(exist_ok=True)

    # --- T(E) curves -----------------------------------------------------
    V0, a = 1.5, 4.0
    E = np.linspace(0.01, 4.0, 1500)
    T = transmission_square(E, V0, a)

    fig, ax = plt.subplots(1, 2, figsize=(11, 4))
    ax[0].plot(E, T, color="teal")
    ax[0].axvline(V0, ls="--", color="orange", label=r"$E=V_0$")
    ax[0].set(xlabel="E", ylabel="T(E)", title=f"Square barrier V0={V0}, a={a}")
    ax[0].legend()
    ax[1].semilogy(E, T, color="teal")
    ax[1].axvline(V0, ls="--", color="orange")
    ax[1].set(xlabel="E", ylabel="T(E) [log]",
              title="Exponential suppression below the barrier")
    fig.tight_layout()
    fig.savefig(outdir / "transmission.png", dpi=160)

    # --- Hartman effect ---------------------------------------------------
    E0 = 0.5 * V0
    widths = np.linspace(0.5, 12, 120)
    taus = [phase_time(E0, V0, w) for w in widths]
    free = widths / np.sqrt(2 * E0)  # classical crossing time at v = k

    fig2, ax2 = plt.subplots(figsize=(6.5, 4))
    ax2.plot(widths, taus, color="purple", label="Wigner phase time")
    ax2.plot(widths, free, ls="--", color="gray", label="free flight a/v")
    ax2.set(xlabel="barrier width a", ylabel=r"$\tau$",
            title=f"Hartman effect: phase time saturates (E={E0}, V0={V0})")
    ax2.legend()
    fig2.tight_layout()
    fig2.savefig(outdir / "hartman.png", dpi=160)
    print(f"Figures written to {outdir}")


if __name__ == "__main__":
    main()
