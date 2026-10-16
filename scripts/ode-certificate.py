"""Exact symbolic certificate for the fourth-order equation in research-notes.md.

This verifies operator identities, rather than inferring an equation from a
finite coefficient match. All computations are small and synchronous.
"""
import sympy as s
from time import perf_counter

start = perf_counter()
z, t, h, u = s.symbols("z t h u")

P = [
    -h**2,
    (t + 27)*h**2 + (5*t + 27)*h + t + 6,
    3*t*((t + 18)*h**2 - 2*t*h - t - 2),
    -t**3*h*(5*h + 3),
    2*t**4*(h + 1)**2,
]
Q = [s.factor(4**j*P[j]*s.rf(h+s.Rational(1, 2), j)
              *(h+j)*(h+j-1)*(h+j-2)/s.rf(h+1, j))
     for j in range(5)]
R = [
    -h**3*(h-1),
    2*h*((11*t+54)*h**3+(-t+81)*h**2+(7*t+39)*h+t+6),
    -12*t*(2*h+1)*((7*t+45)*h**3+7*t*h**2+(6*t-5)*h+2*t),
    8*t**3*(2*h+1)*(2*h+3)*(17*h**2+24*h+12),
    -80*t**4*(h+1)*(2*h+1)*(2*h+3)*(2*h+5),
]
L4 = sum(z**j*r for j, r in enumerate(R))
L5 = sum(z**j*q for j, q in enumerate(Q))
remainder = s.expand((1-10*t*z)*L5
                    -(1+8*t*z)*(h*L4+z*s.diff(L4, z))
                    +2*(1+2*t*z)*L4)
assert remainder == 0
print("Hadamard closure / left factor identity: exact zero remainder")

v = 27*u/(1-t*u)**3
r = 1/(1-t*u)
pp = (1-2*v)/(v*(1-v))
qq = -s.Rational(2, 9)/(v*(1-v))
gg1 = s.factor(pp*s.diff(v, u)-s.diff(v, u, 2)/s.diff(v, u)
               -2*s.diff(r, u)/r)
gg0 = s.factor(qq*s.diff(v, u)**2
               -(pp*s.diff(v, u)-s.diff(v, u, 2)/s.diff(v, u))*s.diff(r, u)/r
               +2*(s.diff(r, u)/r)**2-s.diff(r, u, 2)/r)
LG = sum(u**j*p for j, p in enumerate(P))
g2 = s.expand(LG).coeff(h, 2)*u**2
g1 = (s.expand(LG).coeff(h, 2)+s.expand(LG).coeff(h, 1))*u
g0 = s.expand(LG).coeff(h, 0)
assert s.factor(g1/g2-gg1) == 0
assert s.factor(g0/g2-gg0) == 0
print("Gauss equation pullback: exact zero remainders")

b0, b1, b2 = 1, 2*(t+6), 6*(t*t+24*t+90)
assert s.expand(R[0].subs(h, 2)*b2+R[1].subs(h, 1)*b1+R[2].subs(h, 0)*b0) == 0
print("Initial coefficient forcing L4 F = 0: exact zero")
print("Fourth-order leading coefficient at t=-324:",
      s.factor(s.expand(L4.subs(t, -324)).coeff(h, 4)))
print("elapsed", round(perf_counter()-start, 4), "seconds")
