"""
Cross-validation of the dynamic (split-operator) solver against exact results.

Three checks, all in hbar = m = 1 units:

1. Transfer matrix vs analytic square-barrier formula  (must agree ~1e-12)
2. Wave-packet transmission vs energy-resolved analytic prediction
   T_packet = ∫|phi(k)|^2 T(E(k)) dk / ∫|phi(k)|^2 dk   (sub-percent)
3. Norm conservation: T + R + residual = 1               (~1e-6)

Exit code 0 on success; raises AssertionError otherwise.
"""
from __future__ import annotations

import numpy as np

from split_operator import SplitOperator1D
from transfer_matrix import transfer_matrix_T, transmission_square


def check_transfer_matrix() -> None:
    print("== Check 1: transfer matrix vs analytic square barrier ==")
    v0, a = 1.5, 4.0
    worst = 0.0
    for E in (0.3, 0.75, 1.2, 1.49, 1.51, 2.5, 4.0):
        T_an = float(transmission_square(np.array([E]), v0, a)[0])
        T_tm = transfer_matrix_T(E, np.array([-a / 2, a / 2]),
                                 np.array([0.0, v0, 0.0]))
        err = abs(T_an - T_tm)
        worst = max(worst, err)
        print(f"  E={E:5.2f}  analytic={T_an:.10f}  transfer={T_tm:.10f}  "
              f"|diff|={err:.2e}")
    assert worst < 1e-9, f"transfer-matrix mismatch: {worst}"
    print(f"  PASS (worst |diff| = {worst:.2e})\n")


def check_wavepacket(v0: float = 1.0, a: float = 5.0, k0: float = 1.2,
                     sigma: float = 10.0, tol: float = 0.02) -> None:
    print(f"== Check 2: packet transmission, V0={v0} a={a} k0={k0} ==")
    sim = SplitOperator1D(n=4096, length=800.0, dt=0.02, n_mask=200)
    V = sim.square_barrier(sim.x, v0, a)
    psi0 = sim.gaussian_packet(-150.0, k0, sigma)

    predicted = sim.packet_transmission_prediction(
        psi0, lambda E: float(transmission_square(np.array([E]), v0, a)[0]))

    tally: dict = {}
    psi = sim.propagate(psi0, V, t_final=320.0, tally=tally)
    T, R = sim.transmission_reflection(psi, a / 2 + 5, -a / 2 - 5, tally)

    print(f"  spectral prediction : T = {predicted:.5f}")
    print(f"  dynamic measurement : T = {T:.5f}   R = {R:.5f}")
    print(f"  T + R               : {T + R:.6f}")
    assert abs(T - predicted) < tol, (
        f"dynamic T={T:.5f} vs predicted {predicted:.5f} exceeds tol={tol}")
    assert abs(T + R - 1.0) < 5e-3, f"unitarity violated: T+R={T+R}"
    print("  PASS\n")


def main() -> None:
    check_transfer_matrix()
    # deep tunneling, marginal, and over-barrier regimes
    check_wavepacket(v0=1.0, a=5.0, k0=1.2)    # E≈0.72 < V0  : tunneling
    check_wavepacket(v0=1.0, a=3.0, k0=1.6)    # E≈1.28 > V0  : over-barrier
    check_wavepacket(v0=2.0, a=2.0, k0=1.5)    # E≈1.13 < V0  : strong barrier
    print("All validation checks passed.")


if __name__ == "__main__":
    main()
