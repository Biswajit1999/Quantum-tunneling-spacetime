# 1. Foundations: Non-Relativistic Quantum Tunneling

## 1.1 The phenomenon

A particle with energy E incident on a potential barrier V(x) with max V > E is
classically forbidden from crossing. Quantum mechanically the wavefunction does not
vanish inside the barrier; it decays (for a flat barrier) as

ψ(x) ∝ e^(−κx),  κ = √(2m(V₀ − E))/ħ,

and emerges on the far side with finite amplitude. The transmission probability for a
rectangular barrier of height V₀ and width a (E < V₀) is exactly

T(E) = [1 + (V₀² sinh²(κa)) / (4E(V₀ − E))]⁻¹,

reducing in the opaque limit κa ≫ 1 to T ≈ 16E(V₀−E)/V₀² · e^(−2κa). The
exponential sensitivity to width and mass is why tunneling dominates phenomena from
alpha decay (Gamow 1928) to stellar fusion rates and scanning tunneling microscopy,
yet is negligible for macroscopic objects — with the notable engineered exception of
Josephson circuits (see §1.5).

## 1.2 WKB approximation

For slowly varying barriers, the semiclassical (WKB) transmission is

T ≈ exp[ −(2/ħ) ∫ dx √(2m(V(x) − E)) ],

integrated between classical turning points. WKB is the workhorse for alpha decay
(Gamow factor), field ionization, and — generalized to field theory — the Coleman
bounce of false vacuum decay (doc 04). Its breakdown near turning points is handled
by Airy-function connection formulae.

## 1.3 Transfer-matrix method (exact, piecewise-constant)

Any potential approximated by N constant segments admits an exact solution: in each
segment ψ = A e^(ikx) + B e^(−ikx) (k possibly imaginary), and continuity of ψ, ψ′
at each interface gives a 2×2 matrix relation. The product of all interface and
propagation matrices yields the global transfer matrix M, with

T(E) = 1/|M₁₁|²   (equal asymptotic wavenumbers).

This is implemented in `simulations/transfer_matrix.py` and used as ground truth to
validate the time-dependent solver.

## 1.4 Time-dependent picture: split-operator method

The interactive webpage and `split_operator.py` integrate the time-dependent
Schrödinger equation iħ∂ₜψ = [p²/2m + V(x)]ψ with the Strang-split spectral scheme:

ψ(t+dt) = e^(−iV dt/2ħ) · F⁻¹ e^(−iħk² dt/2m) F · e^(−iV dt/2ħ) ψ(t) + O(dt³),

where F is the FFT. The scheme is exactly unitary, so the norm is conserved to
machine precision; absorbing masks at the grid edges remove wrap-around artifacts
of the periodic FFT domain (the absorbed flux is tallied per side so that
T + R + remaining norm = 1).

A Gaussian packet ψ₀ ∝ exp[−(x−x₀)²/4σ² + ik₀x] has mean energy
⟨E⟩ = ħ²k₀²/2m + ħ²/(8mσ²); the second term (finite-width zero-point energy)
matters when comparing packet transmission to fixed-energy T(E). The correct
comparison decomposes the packet spectrally:

T_packet = ∫ dk |φ_inc(k)|² T(E(k)) / ∫ dk |φ_inc(k)|²,

which is what `validate.py` checks.

## 1.5 Resonant tunneling and macroscopic tunneling

Two barriers in series form a quantum well; at energies matching quasi-bound states
the transmission peaks at T → 1 even deep below the barrier tops (the basis of
resonant-tunneling diodes). The double-barrier preset in the webpage shows this:
sweep the packet energy and watch transmission spike at resonance.

At the opposite extreme of scale, Clarke, Devoret and Martinis demonstrated in 1985
that the phase variable of a current-biased Josephson junction — a collective
coordinate of ~10⁹ Cooper pairs — tunnels out of its metastable washboard-potential
well, with energy-level quantisation inside the well. This discovery of
*macroscopic quantum tunneling* was recognised with the 2025 Nobel Prize in Physics
and underpins today's superconducting qubits.

## 1.6 What the simulator shows

- Exponential suppression: raise barrier height or width and watch T collapse.
- Above-barrier reflection: even with E > V₀, R ≠ 0 — a purely wave effect.
- Transmission resonances: T(E) oscillates above the barrier (Ramsauer–Townsend-like).
- Resonant tunneling: double-barrier preset, sharp sub-barrier transmission peaks.
- Wave-packet reshaping: the transmitted packet appears advanced and distorted —
  the gateway drug to the tunneling-time debate (doc 02).

*Citations: see `references.md`.*
