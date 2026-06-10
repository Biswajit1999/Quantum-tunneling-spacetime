"""
1D time-dependent Schrödinger equation: split-operator (Strang) FFT propagator.

Units: hbar = m = 1. Mirrors the JavaScript solver in ../index.html, with
research-grade extras: energy-resolved transmission via spectral decomposition,
norm bookkeeping with absorbing boundaries, and figure output.

Method (Feit-Fleck-Steiger 1982):
    psi(t+dt) = e^{-iV dt/2} F^{-1} e^{-i k^2 dt / 2} F e^{-iV dt/2} psi(t)
unitary, O(dt^3) per step.
"""
from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np


@dataclass
class SplitOperator1D:
    n: int = 2048
    length: float = 400.0
    dt: float = 0.02
    n_mask: int = 100          # absorbing cells per edge
    mask_strength: float = 0.03

    x: np.ndarray = field(init=False)
    k: np.ndarray = field(init=False)
    dx: float = field(init=False)

    def __post_init__(self) -> None:
        self.dx = self.length / self.n
        self.x = -self.length / 2 + self.dx * np.arange(self.n)
        self.k = 2 * np.pi * np.fft.fftfreq(self.n, d=self.dx)
        d = np.minimum(np.arange(self.n), self.n - 1 - np.arange(self.n))
        ramp = np.clip((self.n_mask - d) / self.n_mask, 0, 1)
        self.mask = 1.0 - self.mask_strength * ramp**3
        self.kin_phase = np.exp(-0.5j * self.k**2 * self.dt)

    # ----------------------------------------------------------------- setup
    def gaussian_packet(self, x0: float, k0: float, sigma: float) -> np.ndarray:
        psi = (2 * np.pi * sigma**2) ** -0.25 * np.exp(
            -((self.x - x0) ** 2) / (4 * sigma**2) + 1j * k0 * self.x)
        return psi.astype(complex)

    @staticmethod
    def square_barrier(x: np.ndarray, v0: float, a: float,
                       center: float = 0.0) -> np.ndarray:
        return np.where(np.abs(x - center) <= a / 2, v0, 0.0)

    # ------------------------------------------------------------------ run
    def propagate(self, psi: np.ndarray, V: np.ndarray, t_final: float,
                  tally: dict | None = None) -> np.ndarray:
        """Propagate to t_final; absorbed probability tallied per side."""
        steps = int(round(t_final / self.dt))
        half_v = np.exp(-0.5j * V * self.dt)
        if tally is None:
            tally = {}
        tally.setdefault("absorb_left", 0.0)
        tally.setdefault("absorb_right", 0.0)
        mid = self.n // 2
        for _ in range(steps):
            psi = half_v * psi
            psi = np.fft.ifft(self.kin_phase * np.fft.fft(psi))
            psi = half_v * psi
            p_before = np.abs(psi) ** 2 * self.dx
            psi = psi * self.mask
            lost = p_before - np.abs(psi) ** 2 * self.dx
            tally["absorb_left"] += float(lost[:mid].sum())
            tally["absorb_right"] += float(lost[mid:].sum())
        return psi

    # ------------------------------------------------------------- analysis
    def transmission_reflection(self, psi: np.ndarray, x_right: float,
                                x_left: float, tally: dict) -> tuple[float, float]:
        p = np.abs(psi) ** 2 * self.dx
        T = float(p[self.x > x_right].sum()) + tally["absorb_right"]
        R = float(p[self.x < x_left].sum()) + tally["absorb_left"]
        return T, R

    def packet_transmission_prediction(self, psi0: np.ndarray,
                                       T_of_E) -> float:
        """
        Energy-resolved prediction: decompose the incident packet spectrally,
        weight T(E(k)) by |phi(k)|^2 over positive k.
        """
        phi = np.fft.fft(psi0)
        w = np.abs(phi) ** 2
        pos = self.k > 0
        E = 0.5 * self.k[pos] ** 2
        Tk = np.array([T_of_E(e) for e in E])
        return float((w[pos] * Tk).sum() / w[pos].sum())


def demo() -> None:
    import pathlib
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    sim = SplitOperator1D()
    v0, a, k0, sigma = 1.0, 5.0, 1.2, 10.0
    V = sim.square_barrier(sim.x, v0, a)
    psi = sim.gaussian_packet(-80.0, k0, sigma)

    outdir = pathlib.Path(__file__).parent / "figures"
    outdir.mkdir(exist_ok=True)

    snapshots, times = [], (0.0, 40.0, 80.0, 140.0)
    tally: dict = {}
    t_now = 0.0
    for t in times:
        psi = sim.propagate(psi, V, t - t_now, tally)
        t_now = t
        snapshots.append(np.abs(psi) ** 2)

    T, R = sim.transmission_reflection(psi, a / 2 + 2, -a / 2 - 2, tally)
    print(f"V0={v0}, a={a}, k0={k0}:  T={T:.4f}  R={R:.4f}  T+R={T+R:.4f}")

    fig, axes = plt.subplots(len(times), 1, figsize=(9, 9), sharex=True)
    for ax, dens, t in zip(axes, snapshots, times):
        ax.fill_between(sim.x, dens, color="teal", alpha=0.6, lw=0)
        ax.plot(sim.x, V * dens.max() / max(v0, 1e-9) * 0.8,
                color="orange", lw=1)
        ax.set_ylabel(f"t = {t:g}")
        ax.set_yticks([])
    axes[-1].set_xlabel("x   (hbar = m = 1)")
    axes[0].set_title(
        f"Wave packet tunneling: V0={v0}, a={a}, k0={k0} (E≈{0.5*k0**2:.2f})"
        f"  →  T={T:.3f}")
    fig.tight_layout()
    fig.savefig(outdir / "wavepacket.png", dpi=160)
    print(f"Figure written to {outdir/'wavepacket.png'}")


if __name__ == "__main__":
    demo()
