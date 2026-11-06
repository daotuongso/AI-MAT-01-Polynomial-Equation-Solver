---
name: bto-mat-01-polynomial-solver
description: Solve one-variable polynomial equations of user-chosen degree and descending-order real coefficients; return approximate complex roots, multiplicity and residual validation.
---
# MAT-01 – Giải phương trình đa thức bậc n – Rev.0

1. Read `START_HERE.md` and all ten Read Contract documents in this session; do not inherit read confirmation.
2. Accept user-selected degree n (1..20 for reference tool); only then request `n+1` real coefficients in order `a_n, a_(n-1), ..., a_0`. Never invent values.
3. If the leading coefficient is zero or count/type invalid, stop and request correction; do not silently reduce degree.
4. Use SymPy through `tools/solve_polynomial.py`; if unavailable or fails, state `BLOCKED` rather than fabricate roots.
5. Report roots (real and complex), multiplicity, numerical precision and residual quality, label numeric results as approximations; symbolic roots only if complete.
6. Never self-approve the Skill, claim business UAT, generate unrelated artifacts, modify GitHub or enlarge scope.
