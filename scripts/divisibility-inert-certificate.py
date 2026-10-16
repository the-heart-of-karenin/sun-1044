"""Exact, bounded checks for the proposed superspecial-reduction argument.

The geometric/deformation argument is in divisibility-inert-powers.md.
This file checks identities and a few fixed coefficients; it is not a proof
by prime enumeration. No work runs on import.
"""
from pathlib import Path
from math import comb
from runpy import run_path
from time import perf_counter
import sympy as S


if __name__ == '__main__':
    started = perf_counter()
    x, y, v, q, z = S.symbols('x y v q z')
    w = 1-x-y
    c, b = 1+S.Rational(3,5)*v, v/540
    # Projective coordinates x_old=x/w, y_old=y/w.
    old_g = (1+x/w+y/w)**3/((x/w)*(y/w))-324*(1+x/w+y/w)
    assert S.cancel((v*old_g-540)*(x*y*w)**2
                    +540*x*y*w*(x*y*(c-x-y)-b)) == 0
    c0, e, d = S.Rational(8,5), S.Rational(3,5), S.Rational(1,135)
    rhs = lambda X: X**3+(3-2*c0)*X**2+(3-c0)*(q-e)*X+(q-e)**2
    assert S.factor(rhs(S.Integer(0))-(q-e)**2) == 0
    XQ = (5*q-3)*(135*q-16)/80
    # Express Y_Q^2 without adjoining sqrt(15).
    YQ2 = S.Rational(135,4096)*(q-e)**2*(135*q-64)**2*q*(q-d)
    assert S.factor(rhs(XQ)-YQ2) == 0
    assert S.factor(rhs(z).subs(q,0)-(z+1)*(z-e)**2) == 0
    assert S.limit(XQ/q**2,q,S.oo) == S.Rational(135,16)
    assert S.Rational(4)-2*S.Rational(4,3)-2*S.Rational(1,2) == S.Rational(1,3)
    assert S.Rational(4)-3*S.Rational(1,2) == S.Rational(5,2)
    assert 3**2*2**3*S.Rational(1,3)*S.Rational(5,2) == 60
    C=(x+y+z)**3-324*x*y*(x+y+z)-540*x*y*z
    assert S.expand(S.diff(C,x)-S.diff(C,y)-108*(x-y)*(3*x+3*y+8*z)) == 0
    assert S.factor(C.subs({z:1,y:-S.Rational(8,3)-x})) == -S.Rational(125,27)
    assert S.discriminant(C.subs({y:x,z:1}),x) == 2**6*3**9*7*17**2
    assert S.discriminant(C.subs({y:1,z:0}),x) == 2**12*3**12*5
    print('Projective model, sections, height arithmetic, and bad-prime identities: exact.')

    # Two fixed inert primes and their first two powers; no search.
    av=run_path(str(Path(__file__).with_name('prime-power-probe.py')))['a_values']((37**2-1)//2)
    for p in (23,37):
        assert pow((-105)%p,(p-1)//2,p)==p-1
        for r in (1,2):
            n=(p**r-1)//2
            betan=sum(comb(n,j)*(-540)**(n-j)*av[j] for j in range(n+1))
            betaprev=sum(comb(n-1,j)*(-540)**(n-1-j)*av[j] for j in range(n))
            derivative=n*(betan+540*betaprev)
            assert betan%(p**r)==0 and derivative%(p**r)==0
            print('p =',p,'r =',r,': log and parameter-derivative coefficient are p-integral.')
    print('Elapsed',round(perf_counter()-started,3),'seconds.')
