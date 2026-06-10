# 2. The Tunneling-Time Problem: How Long Does Tunneling Take?

Arguably the longest-running open controversy in quantum mechanics. The question
"how much time does the particle spend inside the barrier?" has no unique
operational meaning, because time is not an operator and the particle has no
trajectory. Different clocks measure different, equally legitimate, times.

## 2.1 A century of definitions

- **MacColl (1932):** first noted the transmitted packet suffers "no appreciable
  delay" crossing the barrier.
- **Wigner phase time / Eisenbud–Wigner delay (1955):** τ_φ = ħ d(arg t(E))/dE,
  the group delay of the transmitted peak.
- **Hartman effect (1962):** the phase time *saturates* with barrier width — for
  opaque barriers the apparent crossing speed exceeds c. Resolution: the
  transmitted packet is a reshaped, attenuated copy of the leading edge of the
  incident packet; no information travels superluminally. The phase time is a
  non-local arrival-time descriptor, not a traversal time.
- **Büttiker–Landauer time (1982):** modulate the barrier and find the crossover
  frequency; gives τ_BL = ∫ dx m/(ħκ(x)), the "semiclassical" traversal time.
- **Larmor clock (Baz'/Rybachenko; Büttiker 1983):** use spin precession in a weak
  magnetic field confined to the barrier as a local clock; decomposes into in-plane
  (τ_y) and out-of-plane (τ_z, back-action) components.
- **Steinberg weak-value interpretation (1995):** the Larmor times are weak values
  of a projector onto the barrier region — conditioned on transmission. This frames
  the "speed" debate in terms of weak measurement rather than trajectories.

## 2.2 The attoclock era

Strong-field ionization gives an experimental handle: an intense elliptically
polarized laser pulse tears an electron out through the field-suppressed Coulomb
barrier, and the rotating field vector acts as a clock hand ("attoclock") — the
final momentum angle encodes the ionization instant. Experiments (Keller group and
successors) sparked a decade of conflicting claims of zero versus finite (tens of
attoseconds) tunneling delays, with the interpretation hinging on Coulomb-field
corrections and the definition of the starting time.

Key recent developments:

- **Kheifets & collaborators / unified analyses (2024):** the measured quantity
  decomposes into a *tunneling time* and a *barrier time-delay*; the latter can be
  extracted from the difference between adiabatic and nonadiabatic ionization and,
  in the weak-measurement limit, coincides with the Larmor-clock interaction time
  (arXiv:2402.14431).
- **"In Search of Lost Tunneling Time" (2025):** the attoclock does *not* measure
  the local Larmor time but a non-local time closely related to the Wigner phase
  time; a Steinberg weak-value treatment yields a position-resolved time density
  and a non-zero Larmor tunneling time (arXiv:2503.07859). The two clock families
  appear complementary, not contradictory.
- **Ramsey-clock unification (2024):** a proposal/analysis promoting Ramsey
  interferometry as a unifying framework for the zoo of tunneling times
  (PMC11094764 / associated journal article).

## 2.3 Where the field stands

The modern consensus, such as it exists:

1. There is no single tunneling time; each protocol defines its own observable.
2. The Hartman effect does not imply superluminal signaling (causality is safe —
   the transmitted field is determined by the incident field's leading tail).
3. Local clocks (Larmor-type, weak measurement) and non-local clocks (phase time,
   attoclock) measure different functionals of the same scattering amplitude, and
   2024–2025 work has begun mapping precisely how they relate.
4. Experiment now constrains theory at the attosecond level; "instantaneous
   tunneling" claims survive only under specific definitional choices.

## 2.4 The webpage's Tunneling-Time Observatory

Module 3 of `index.html` implements the Larmor clock as a live numerical
experiment: a two-component spinor packet with components seeing Zeeman-split
barriers V₀ ∓ ω/2, spin initially along +x. The transmitted spin orientation
yields τ_y = −⟨σ_y⟩/ω and τ_z = ⟨σ_z⟩/ω, which converge (weak-ω limit) to the
weak values −ħ∂(arg t)/∂V₀ and −ħ∂(ln|t|)/∂V₀. The module also plots τ_φ, τ_y,
τ_z, τ_BL versus barrier width at fixed energy — the Hartman saturation of the
non-local clocks against the linear growth of the local back-action clock,
which is precisely the dichotomy the 2024–2025 attoclock reanalyses formalize.

## 2.5 Connection to the simulator

In the wave-packet lab you can directly observe phase-time phenomenology: compare
arrival of a freely propagating packet against the transmitted fraction through an
opaque barrier — the transmitted peak emerges *earlier* than naive expectation,
while remaining strictly inside the envelope causally allowed by the incident
leading edge. The `transfer_matrix.py` script computes the Wigner phase time
explicitly and reproduces Hartman saturation.

*Citations: see `references.md`.*
