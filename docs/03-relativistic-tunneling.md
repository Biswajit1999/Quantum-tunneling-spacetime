# 3. Relativistic Tunneling: Klein Paradox, Graphene, and Curved Spacetime

## 3.1 The Klein paradox

In 1929 Oskar Klein applied the Dirac equation to a sharp potential step of height
V₀. For V₀ exceeding E + mc², instead of the exponential damping the Schrödinger
equation predicts, the solution inside the step is *oscillatory*: the barrier is
penetrated with high probability. In the limit of a very high step the reflection
coefficient stays finite and transmission persists — the Klein paradox.

The modern resolution invokes the negative-energy continuum: a super-critical step
pulls the positron continuum above the electron continuum, so transmission proceeds
via hole states — physically, electron–positron pair creation at strong field
gradients (Sauter 1931; Schwinger mechanism in QED). "Klein tunneling" is thus not
barrier penetration by a single particle but a many-body process masquerading as
one in the single-particle equation.

Key signatures:

- For **massless** Dirac particles in 1D, transmission through any electrostatic
  barrier at normal incidence is **exactly 1**, independent of barrier height or
  width — chirality forbids backscattering.
- For massive particles, transmission windows open when V₀ − E > 2mc² (the
  "Klein zone").

## 3.2 Graphene: Klein tunneling on a tabletop

Charge carriers in graphene obey a 2D massless Dirac equation with c → v_F ≈ c/300.
Katsnelson, Novoselov & Geim (2006) predicted, and Stander et al. and Young & Kim
(2009) confirmed, perfect transmission through electrostatic (np-n junction)
barriers at normal incidence, with angle-dependent suppression off-normal. Klein
tunneling is why electrostatic confinement of graphene electrons is hard — and why
graphene became the experimental playground for relativistic tunneling.

Recent work extends this to **space-time modulated barriers** (arXiv:2510.21154):
temporal modulation of the potential provides access to Klein-tunneling physics in
parameter regimes unreachable with static barriers, connecting to the broader
"time crystals / temporal interfaces" program in photonics and condensed matter.

## 3.3 Dirac and Klein–Gordon equations in curved spacetime

Coupling spin-½ fields to gravity requires the tetrad (vierbein) formalism: the
curved-space Dirac equation reads

[iγ^a e_a^μ (∂_μ + Γ_μ) − mc/ħ]ψ = 0,

with spin connection Γ_μ. Two results relevant to this repository:

1. **Flat–curved mapping in 1+1D:** any solution of the free massless Dirac
   equation in 1+1D flat spacetime can be mapped by a local phase transformation
   into a solution on a curved static background — the metric is encoded in the
   phase (Boada et al. / Sci. Rep. 7, 40346). This underlies cold-atom and
   trapped-ion *analogue gravity* simulators of Dirac fields in curved space.
2. **Horizons as barriers:** near a black-hole horizon the effective potential for
   field modes forms a barrier; greybody factors are transmission coefficients of
   a relativistic tunneling problem. This makes "tunneling in spacetime" literal —
   see doc 04 for Hawking radiation as a tunneling process.

## 3.4 Tunneling of relativistic wave packets

Numerically, relativistic tunneling is integrated with the same split-operator
technology as the Schrödinger case, applied to the Dirac or Klein–Gordon equation
(the kinetic step uses the relativistic dispersion or the free Dirac propagator in
momentum space). Qualitative differences from the non-relativistic simulator:

- Zitterbewegung trembling of packet centroids,
- pair-creation-like interference once the Klein-zone condition is met,
- transmission that *increases* with barrier height past criticality, the inverse
  of Schrödinger intuition.

The webpage's "physics notes" section flags exactly where the non-relativistic
simulator's predictions would fail in the relativistic regime.

*Citations: see `references.md`.*
