# 4. Tunneling of Spacetime: False Vacuum Decay and Hawking Radiation

Here tunneling stops being something that happens *in* spacetime and becomes
something that happens *to* spacetime — or to the quantum fields that define its
vacuum.

## 4.1 False vacuum decay (Coleman formalism)

A scalar field sitting in a local (false) minimum of its potential is metastable:
quantum fluctuations nucleate bubbles of true vacuum that, above a critical radius,
grow at asymptotically light speed and convert the universe. The decay rate per
unit volume is computed from the Euclidean *bounce* solution (Coleman 1977):

Γ/V = A e^(−S_E[φ_bounce]/ħ),

the field-theoretic generalization of the WKB exponent. Coleman & De Luccia (1980)
added gravity: bubble interiors are open FRW universes, and gravitation can
stabilize or destabilize the false vacuum depending on the vacuum energies.

**Why anyone cares:** the measured Higgs and top masses place the Standard Model
vacuum tantalizingly close to the metastability boundary; inflationary and
landscape cosmologies rely on vacuum transitions; and a bubble nucleation event
would be the ultimate tunneling-in-spacetime phenomenon — undetectable until
arrival, since the wall approaches at ~c.

## 4.2 Quantum simulators of vacuum decay (2024–2026)

False vacuum decay has moved from chalkboard to laboratory analogues:

- **Ferromagnetic superfluid / cold-atom experiments** observed bubble nucleation
  from a metastable state (Zenesini et al., Nat. Phys. 2024).
- **Cold-atom gauge-theory simulators** probed false vacuum decay dynamics in a
  lattice gauge theory setting (Zhu, Liu et al. 2024).
- **Rydberg atom arrays** probed bubble nucleation dynamics directly
  (arXiv:2512.04637), and neutral-atom studies examined nucleation in quenched
  spin chains (Darbha et al., Phys. Rev. B 2024).
- **D-Wave annealer (2025):** real-time simulation of bubble formation and
  interaction in a 5,564-qubit ring — bubbles of true vacuum forming, moving,
  merging.
- **Methodology:** finite experimental boundaries seed spurious edge nucleation;
  a high-density "trench" at the boundary recovers cosmologically relevant bulk
  nucleation (arXiv:2504.02829, Phys. Rev. A 2025).

The webpage's third module is a visual analogue of exactly this physics: stochastic
nucleation at a rate Γ ∝ e^(−B/ΔV-ish), supercritical bubbles expanding with
accelerating walls, percolation of the true vacuum.

## 4.3 Hawking radiation as tunneling (Parikh–Wilczek)

Parikh & Wilczek (2000) recast Hawking radiation as a tunneling process: a
positive-energy particle materializes just inside the horizon and tunnels out, the
barrier being set *by the particle itself*, since emission of energy ω shrinks the
horizon from 2M to 2(M−ω). Working in Painlevé–Gullstrand coordinates (stationary,
horizon-regular), the imaginary part of the action for the outgoing null geodesic
gives

Γ ∝ e^(−2 Im S/ħ) = e^(+ΔS_BH) = e^(−8πωM(1 − ω/2M)),

i.e. the Hawking thermal spectrum at T_H = ħc³/(8πGMk_B) *plus* non-thermal
corrections from energy conservation (back-reaction). Two consequences with active
2024–2026 literature:

- the non-thermal spectrum carries **correlations between successive quanta**,
  with total entropy conserved — an argument that tunneling-based emission is
  consistent with unitarity and relevant to the information-loss problem
  (arXiv:2502.09924, Entropy 2025);
- the method generalizes to charged/rotating horizons, de Sitter horizons, and the
  Hamilton–Jacobi variant for fermions, and connects to instanton treatments
  (arXiv:1806.03766).

## 4.4 The throughline

One mathematical object unifies this repository: the imaginary part of an action.

| Phenomenon | "Barrier" | Exponent |
|---|---|---|
| Alpha decay, STM, RTDs | potential V(x) | 2∫κ dx (WKB / Gamow) |
| False vacuum decay | field potential V(φ) | Euclidean bounce action S_E |
| Hawking radiation | horizon + energy conservation | 2 Im S = ΔS_BH |

Quantum tunneling in spacetime is the statement that the third row exists: the
geometry of spacetime itself participates in, and is altered by, a tunneling event.

*Citations: see `references.md`.*
