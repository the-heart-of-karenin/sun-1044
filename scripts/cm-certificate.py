"""Small exact checks for the level-30 CM value used in the proof."""
from fractions import Fraction as Q
from math import factorial
from pathlib import Path
import sympy as s


def exp_lower(x,n=16):
    return sum((x**k/Q(factorial(k))) for k in range(n+1))


def exp_upper(x,n=16):
    return exp_lower(x,n)+x**(n+1)/Q(factorial(n+1))/(1-x/Q(n+2))


if __name__=='__main__':
    # 3.14 < pi < 22/7; 10.24 < sqrt(105) < 10.25.
    lower=Q(157,50)*Q(256,25)/15
    upper=Q(22,7)*Q(41,4)/15
    rho_lo,rho_hi=Q(29,250),Q(59,500)
    assert exp_lower(lower)>1/rho_hi
    assert exp_upper(upper)<1/rho_lo
    R=Q(3,25)
    tail=R*R/((1-R)*(1-R*R))
    tail+=sum((R**d/(1-R**d)**2) for d in (2,3,5,6,10,15,30))
    assert tail<Q(1,25)
    # exp(1/25) < 25/24, proved by its geometric-series majorant.
    assert rho_lo*(1+rho_lo)*Q(24,25)>Q(3,25)
    assert rho_hi*(1+rho_hi)*Q(25,24)<Q(7,50)
    print('Elementary interval isolation: -11 < T(tau_0) < -9 passed.')

    T,U,X=s.symbols('T U X')
    poly=s.sympify((Path(__file__).resolve().parents[1] / 'data' / 'modular7-polynomial.txt').read_text(encoding='utf-8'),locals={'T':T,'U':U})
    at={T:-10,U:-10}
    assert poly.subs(at)==0
    f1=s.diff(poly,U).subs(at)
    f2=s.diff(poly,T,2).subs(at)
    f12=s.diff(poly,T,U).subs(at)
    Upp=s.cancel(-2*(f2-f12)/f1)
    Ypp=-100*Upp-40
    G=(1+5*X)*(1+4*X)*(1+X)*(1-4*X)
    lam=1+X*s.diff(G,X)/(2*G)-X*Ypp/2
    assert Upp==-s.Rational(122,315)
    assert Ypp==-s.Rational(80,63)
    assert lam.subs(X,-s.Rational(1,10))==s.Rational(4,21)
    assert G.subs(X,-s.Rational(1,10))==s.Rational(189,500)
    print('Exact modular-equation derivatives and lambda = 4/21 passed.')
