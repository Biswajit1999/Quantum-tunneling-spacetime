# Research Quality Upgrade

This repository has been upgraded with a compact research-quality layer: reference anchors, validation checks, and explicit scientific/software boundaries.

## Scope

Quantum tunneling and semiclassical spacetime lab covering wave-packet barriers, Klein tunneling, false-vacuum decay and Hawking analogies.

## Equations And Models

- Time-dependent Schrodinger equation
- WKB transmission T approx exp(-2 integral sqrt(2m(V-E))/hbar dx)

## Reference Anchors

The file `data/research-reference.json` stores benchmark anchors used by `scripts/validate_repository.mjs`. These are intentionally small and auditable so the repository can be checked without network access.

## Browser Upgrade

If this repository contains a browser interface, `research-overlay.js` adds a non-invasive mission-control quality panel with validation status and benchmark telemetry.

## References

- Griffiths, D.J. and Schroeter, D.F., 2018. Introduction to Quantum Mechanics. Cambridge University Press.
