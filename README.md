# MAT-01 – AI Polynomial Equation Solver – Rev.0

**Scope strictly limited to** solving a single polynomial equation with user-selected integer degree `n`, followed by its `n+1` coefficients `a_n...a_0` in descending order. Equation: `a_n*x**n + ... + a_0 = 0`.

Input may use integer, exact decimal or rational real coefficients (`3`, `-0.5`, `2/3`); leading coefficient **must be nonzero**. Supports `1 <= n <= 20` as a practical safety limit of the reference CLI; this bound may be changed only by controlled revision/Owner decision. Returns complex roots, multiplicities, real/complex classification, and numerical residuals. Symbolic exact roots are presented when SymPy supplies a complete low-degree answer. Repeated roots are found by square-free factorization.

**No equations outside one-variable polynomials:** no systems, differential equations, inequalities, graphs, automated uploads, UI apps, research or integration. Does not modify Parent/Core or any GitHub repository.

Start at [START_HERE.md](START_HERE.md). Execution: `python -m pip install -r requirements.txt`, then `python tools/solve_polynomial.py --interactive` or `python tools/solve_polynomial.py EXAMPLES/SAMPLE_QUADRATIC.json`. Offline calculations only; dependency must be installed locally.

Owner-requested new Skill ID `MAT-01` is **proposed** and not sourced from Master Catalogue. State `READY_FOR_OWNER_REVIEW`, approved=false, release_authorized=false.
