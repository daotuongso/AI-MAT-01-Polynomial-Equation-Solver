# Mathematical methodology

For `n >= 1`, polynomial `P(x)=a_n*x^n+...+a_0` and `a_n ≠ 0`. Over the complex numbers, **exactly n roots counted with algebraic multiplicity** (Fundamental Theorem of Algebra). The tool accepts real rational coefficients only; non-real coefficients are outside Rev.0.

1. Parse real numeric literals into SymPy Rational to preserve exact input (including decimals as exact rational values).
2. `Poly(...).sqf_list()` yields relatively square-free factors and their root multiplicities.
3. For each factor `f`, apply SymPy `nroots` with `maxsteps=300` and 20 displayed digits. For linear factors, use exact root formula. This handles repeated roots without relying on unstable duplicate detection from raw nroots.
4. Optionally `roots(P)` for `n<=4`; include explicit exact roots only if the returned multiplicities cover all `n`. Approximate expressions may involve radicals; if unavailable, omit rather than fabricate.
5. Calculate `abs(P(root))/max(1, sum(|a_i|*max(1,|root|)^i))` for a dimensionless normalized residual. The degree sum of root multiplicities must equal n, else fail.
6. Classify as real when imaginary component is small compared with numerical precision and magnitude; otherwise complex. This is a numerical classification and may be uncertain for ill-conditioned polynomials.

Examples include: x²-5x+6=0 → 2,3; x³-3x²+3x-1=(x-1)³; x²+1→±i. Mathematical correctness is additionally tested with independent known benchmark equations and coefficient reconstruction checks.

**Limits:** high degree coefficients may be ill-conditioned; a small residual does not guarantee a small forward root error, nor exact proof. Numerical solver can fail to converge; report failure instead of asserting roots. Maximum n=20 configured. Do not claim closed-form radicals exist for arbitrary n.
