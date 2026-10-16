"""Short exact identities for the Hodge-class route to divisibility."""
import sympy as S
from time import perf_counter


if __name__ == '__main__':
    started=perf_counter()
    r,c,b=S.symbols('r c b')
    aa=r*(r+2)/(4*(r*r-1))
    bb=-r**4/(16*(r-1)**3*(r+1))
    R0=-16*(r-2)*(r-1)**3*(r+1)
    R1=-4*(r-1)**2*(r+2)*(3*r*r-2*r-2)
    R2=r**3*(3*r*r-8*r+2)
    at=lambda f:S.factor(f.subs(r,S.Rational(1,4)))
    k=S.Rational(315,16)
    assert 54-S.Rational(448,135)*at(R0)==103
    assert k*at(S.diff(aa,r))-S.Rational(448,135)*at(R1)==357*at(aa)
    assert k*at(S.diff(bb,r))-S.Rational(448,135)*at(R2)==357*at(bb)
    tau=(15+S.I*S.sqrt(105))/30
    G=S.sqrt(105)/32
    period=[90,90*tau+k/(2*S.I*G),90*tau*tau+2*tau*k/(2*S.I*G)]
    assert [S.simplify(a) for a in period]==[90,45,33]
    assert S.simplify(tau*S.conjugate(tau))==S.Rational(11,30)
    # Two independent marked-elliptic-surface invariants for the full family.
    inv=[(c-1)/b,c**3/b]
    jac=S.factor(S.det(S.Matrix([[S.diff(f,c),S.diff(f,b)] for f in inv])))
    assert jac==c**2*(2*c-3)/b**3
    assert jac.subs({c:S.Rational(8,5),b:S.Rational(1,540)})!=0
    print('Exact cohomology row, CM Hodge vector (90,45,33), and moduli Jacobian verified.')
    print('Elapsed',round(perf_counter()-started,3),'seconds.')
