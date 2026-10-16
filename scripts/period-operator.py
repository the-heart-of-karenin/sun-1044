"""Small exact setup for the normalized fourth-order period equation.

The independent variable is x=108*z; the point of interest is x=1/20.
No work runs on import.
"""
import sympy as s
from sympy.functions.combinatorial.numbers import stirling

x, h = s.symbols("x h")


def monic_coefficients():
    rs = [
        18*h**3*(h-1),
        h*(1170*h**3-135*h**2+743*h+106),
        6*(2*h+1)*(2223*h**3+2268*h**2+1949*h+648),
        3888*(2*h+1)*(2*h+3)*(17*h**2+24*h+12),
        116640*(h+1)*(2*h+1)*(2*h+3)*(2*h+5),
    ]
    poly = s.Poly(sum(x**j*r for j, r in enumerate(rs)), h)
    ordinary = [sum(poly.coeff_monomial(h**r)*stirling(r, k, kind=2)*x**k
                    for r in range(k, 5)) for k in range(5)]
    return [s.cancel(a/ordinary[4]) for a in ordinary]


def product_auxiliary():
    a0, a1, a2, a3, _ = monic_coefficients()
    b1 = s.factor((8*a2-12*s.diff(a3, x)-3*a3*a3)/20)
    b0 = s.factor((12*s.diff(a2, x)-8*a1+4*a2*a3
                   -10*s.diff(a3, x, 2)-a3**3-9*a3*s.diff(a3, x))/20)
    return b0, b1


def mod_at_root(expr, factor):
    num, den = s.fraction(s.cancel(expr))
    return s.rem(s.Poly(num, x).as_expr()
                 * s.invert(s.Poly(den, x).as_expr(), factor, x), factor, x)


if __name__ == "__main__":
    from time import perf_counter
    start = perf_counter()
    b0, b1 = product_auxiliary()
    r = s.symbols("r")
    print("Auxiliary equation is i''' + b1 i' + b0 i=0")
    for f in (x, 1+8*x, 1+30*x, 1+27*x+216*x*x):
        residue1 = mod_at_root(s.cancel(f**2*b1)/s.diff(f, x)**2, f)
        residue0 = mod_at_root(s.cancel(f**3*b0)/s.diff(f, x)**3, f)
        indicial = s.factor(r*(r-1)*(r-2)+residue1*r+residue0)
        print("factor", f, "indicial", indicial, "roots", s.solve(indicial, r))
    residue1 = s.limit(x*x*b1, x, s.oo)
    residue0 = s.limit(x**3*b0, x, s.oo)
    indicial = s.factor(r*(r-1)*(r-2)+residue1*r+residue0)
    print("infinity, x-power convention", indicial, "roots", s.solve(indicial, r))
    print("elapsed", round(perf_counter()-start, 4), "seconds")
