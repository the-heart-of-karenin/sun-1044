"""Bounded symbolic calculation for an additional anti-invariant section."""
import sympy as s
from time import perf_counter

q,e,u=s.symbols('q e u')
X=(q-e)*(u*q+1/e)
rhs=X**3+(1-2*e)*X**2+(2-e)*(q-e)*X+(q-e)**2
Q=s.cancel(rhs/((q-e)**2*q))

if __name__=='__main__':
    start=perf_counter()
    print('Cubic after removing q(q-e)^2:',s.factor(Q))
    disc=s.factor(s.discriminant(Q,q))
    print('Discriminant:',disc)
    at=s.factor(Q.subs(e,s.Rational(3,5)))
    print('At e=3/5:',at)
    print('Discriminant at e=3/5:',s.factor(disc.subs(e,s.Rational(3,5))))
    du=s.factor(s.together(Q.subs(q,s.Rational(1,135))).subs(e,s.Rational(3,5)))
    print('Necessary condition at d=1/135:',du)
    A,B,c,d=s.symbols('A B c d')
    xx=A*q*q+B*q-1
    L=(3*B+d*A)/2
    M=s.cancel((3*B*B-2*c*A-L*L+2*d*A*L)/(2*A))
    # Y=sqrt(A)*(A*q^2+L*q+M).
    residual=s.Poly(s.expand(xx**3+(3-2*c)*xx**2+(3-c)*(q-c+1)*xx
                    +(q-c+1)**2-q*(q-d)*A*(A*q*q+L*q+M)**2),q)
    equations=[s.factor(s.together(residual.coeff_monomial(q**j)).as_numer_denom()[0])
               for j in range(1,4)]
    fixed=[f.subs({c:s.Rational(8,5),d:s.Rational(1,135)}) for f in equations]
    gb=s.groebner(fixed,B,A)
    print('General quadratic X with constant -1, fixed CM Groebner basis:')
    for f in gb.polys: print(s.factor(f.as_expr()))
    r=s.symbols('r')
    AA=r*r/d
    aa=r**3/d
    bb=r*(3*B+r*r)/2
    xx=AA*q*q+B*q+c-1
    residual=s.Poly(s.expand(xx**3+(3-2*c)*xx**2+(3-c)*(q-c+1)*xx
                    +(q-c+1)**2-q*(q-d)/d*(aa*q*q+bb*q+c-1)**2),q)
    equations=[s.factor(s.together(residual.coeff_monomial(q**j)).as_numer_denom()[0])
               for j in range(2,5)]
    fixed=[f.subs({c:s.Rational(8,5),d:s.Rational(1,135)}) for f in equations]
    gb=s.groebner(fixed,B,r)
    print('General quadratic X with constant c-1, fixed CM Groebner basis:')
    for f in gb.polys: print(s.factor(f.as_expr()))
    print('elapsed',round(perf_counter()-start,3),'seconds')
