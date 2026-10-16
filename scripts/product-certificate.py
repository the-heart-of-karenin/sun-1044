"""Exact certificate for the newly found product of two second-order solutions.

Uses the required t=-324, x=108*z, and only rational operations.  No numerical
guessing and no background work.  The square-root term enters only by its
square and logarithmic derivative.
"""
import importlib.util
from pathlib import Path
from time import perf_counter
import sympy as s

start = perf_counter()
spec = importlib.util.spec_from_file_location("period_operator", Path(__file__).with_name("period-operator.py"))
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
x = m.x
original = m.monic_coefficients()
C = (1+12*x)**3-x
B, A = 1-24*x, 1+30*x
N = 3359232*x**4-46656*x**3-52200*x**2-1419*x+53
a = s.cancel(1/x+s.diff(C, x)/(2*C)+12/B)
b = s.cancel(N/(18*x*B**2*C))
d2 = s.Rational(160, 3)*A**2/(x**2*B**4*C)
dlog = s.cancel(s.diff(A, x)/A-1/x-2*s.diff(B, x)/B-s.diff(C, x)/(2*C))

# Remove the common first derivative from each factor.  The normalized
# second-order potentials are beta +/- d.
beta = s.cancel(b-s.diff(a, x)/2-a*a/4)
M3 = -dlog
normalized_product = [
    s.cancel(2*M3*s.diff(beta, x)+4*d2+2*s.diff(beta, x, 2)),
    s.cancel(4*M3*beta+6*s.diff(beta, x)),
    4*beta,
    M3,
    s.Integer(1),
]

# (D+a)^n, with coefficient differentiation included.
powers = [[s.Integer(1)]]
for _ in range(4):
    old = powers[-1]
    new = [s.Integer(0)]*(len(old)+1)
    for k, value in enumerate(old):
        new[k] += s.diff(value, x)+a*value
        new[k+1] += value
    powers.append([s.cancel(v) for v in new])

for k in range(4):
    product_coefficient = sum(normalized_product[n]*powers[n][k]
                              for n in range(k, 5))
    assert s.cancel(product_coefficient-original[k]) == 0
    print("D^"+str(k)+" coefficient: exact zero remainder")
assert s.limit(x*b, x, 0) == s.Rational(53, 18)
print("Initial product slope = -53/9, matching the original power series")
print("elapsed", round(perf_counter()-start, 4), "seconds")
