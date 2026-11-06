#!/usr/bin/env python3
"""One-variable polynomial solver, n then descending coefficients. Offline only."""
import argparse
import json
import re
import sys
from pathlib import Path

try:
    import sympy as sp
except ImportError:
    print("BLOCKED: SymPy is required (pip install -r requirements.txt).", file=sys.stderr)
    raise SystemExit(3)

MAX_DEGREE = 20
PRECISION = 20
LITERAL = re.compile(r"^[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:/[1-9]\d*)?$")

class InputError(ValueError):
    pass

class SolveError(RuntimeError):
    pass


def parse_degree(n):
    if type(n) is not int or not (1 <= n <= MAX_DEGREE):
        raise InputError(f"degree must be an integer from 1 to {MAX_DEGREE}")
    return n


def parse_coefficient(v):
    if type(v) is int:
        v = str(v)
    if not isinstance(v, str) or len(v) > 64 or not LITERAL.fullmatch(v.strip()):
        raise InputError(f"invalid coefficient: {v!r}; use integer, decimal or fraction as text")
    try:
        return sp.Rational(v.strip())
    except (ValueError, TypeError, ZeroDivisionError) as err:
        raise InputError(f"invalid coefficient: {v!r}") from err


def validate(n, coefficients):
    n = parse_degree(n)
    if not isinstance(coefficients, list) or len(coefficients) != n + 1:
        raise InputError(f"expected {n + 1} descending coefficients, received {len(coefficients) if isinstance(coefficients,list) else 'invalid list'}")
    c = [parse_coefficient(x) for x in coefficients]
    if c[0] == 0:
        raise InputError("leading coefficient a_n must be nonzero; do not silently reduce degree")
    return n, c


def _residual(coefficients, z):
    z = sp.N(z, PRECISION + 10)
    p = sp.N(0, PRECISION + 10)
    for a in coefficients:
        p = p * z + a
    bound = sp.N(0, PRECISION + 10)
    r = max(sp.N(1, PRECISION + 10), abs(z))
    for a in coefficients:
        bound = bound * r + abs(a)
    return abs(complex(sp.N(p, 18))) / max(1.0, float(sp.N(bound, 18)))


def solve(degree, coefficients):
    degree, coefficients = validate(degree, coefficients)
    x = sp.Symbol("x")
    poly = sp.Poly.from_list(coefficients, gens=x)
    # Algebraic multiplicities via square-free factorization.
    sqf = poly.sqf_list()[1]
    results = []
    try:
        for factor, multiplicity in sqf:
            if factor.degree() == 1:
                a, b = factor.all_coeffs()
                numeric = [sp.N(-b / a, PRECISION + 10)]
            else:
                numeric = factor.nroots(n=PRECISION + 10, maxsteps=300)
            for z in numeric:
                z = sp.N(z, PRECISION + 10)
                real = float(sp.re(z))
                imag = float(sp.im(z))
                # No forced snapping for nonzero near-real complex roots; report uncertainty.
                nearly_real = abs(imag) <= 1e-15 * max(1.0, abs(real))
                results.append({
                    "real": real, "imag": imag,
                    "multiplicity": int(multiplicity),
                    "classification": "real (numerical)" if nearly_real else "complex",
                    "near_real": nearly_real,
                    "normalized_residual": _residual(coefficients, z),
                })
    except (Exception,) as err:
        raise SolveError("numerical root solver did not converge or could not solve: " + str(err)) from err

    if sum(item["multiplicity"] for item in results) != degree:
        raise SolveError("degree/multiplicity invariant failed; refusing incomplete roots")
    results.sort(key=lambda a: (round(a["real"], 12), round(a["imag"], 12)))
    # Closed form only if complete; may not be available for arbitrary n.
    exact = None
    if degree <= 4:
        try:
            rdict = sp.roots(poly.as_expr(), x)
            if sum(int(m) for m in rdict.values()) == degree:
                exact = [{"root": str(k), "multiplicity": int(m)} for k, m in rdict.items()]
        except Exception:
            exact = None
    return {
        "status": "COMPLETED", "degree": degree,
        "coefficients": [str(a) for a in coefficients],
        "equation": str(poly.as_expr()) + " = 0",
        "number_of_distinct_roots": len(results),
        "number_of_roots_with_multiplicity": sum(v["multiplicity"] for v in results),
        "roots": results, "exact_roots_if_available": exact,
        "numerical_precision_digits": PRECISION,
        "limitations": "Numeric roots are approximate; small residual does not imply small forward error for ill-conditioned polynomials.",
    }


def interactive():
    try:
        n = parse_degree(int(input(f"Nhập bậc n (1–{MAX_DEGREE}): ").strip()))
        s = input(f"Nhập {n+1} hệ số a_n,...,a_0 (cách nhau dấu cách hoặc ;): ").strip().replace(";", " ")
        return solve(n, s.split())
    except ValueError as err:
        raise InputError(str(err)) from err


def main():
    parser = argparse.ArgumentParser(description="Solve a one-variable polynomial of user-entered degree")
    parser.add_argument("file", nargs="?", help="JSON input with degree and coefficients")
    parser.add_argument("--interactive", action="store_true", help="ask n then n+1 coefficients")
    parser.add_argument("--json", action="store_true", help="machine-readable result (default also JSON)")
    a = parser.parse_args()
    try:
        if a.interactive:
            answer = interactive()
        elif a.file:
            data = json.loads(Path(a.file).read_text(encoding="utf8"))
            answer = solve(data.get("degree"), data.get("coefficients"))
        else:
            parser.error("provide --interactive or a JSON input file")
        print(json.dumps(answer, ensure_ascii=False, indent=2))
    except (InputError, SolveError, OSError, ValueError, TypeError) as err:
        print("BLOCKED: " + str(err), file=sys.stderr)
        raise SystemExit(2)

if __name__ == "__main__":
    main()
