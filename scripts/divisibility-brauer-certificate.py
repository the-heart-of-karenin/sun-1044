"""Short exact checks for the new constant-term/coordinate reduction."""
from fractions import Fraction as Q
from pathlib import Path
from math import comb
from time import perf_counter
import runpy
import sympy as s

if __name__=='__main__':
    start=perf_counter()
    old=runpy.run_path(str(Path(__file__).with_name('prime-power-probe.py')))
    nmax=16
    av=old['a_values'](nmax)
    beta=[sum(comb(n,k)*(-540)**(n-k)*av[k] for k in range(n+1))
          for n in range(nmax+1)]
    dd=[(357*n+103)*beta[n]+192780*n*(beta[n-1] if n else 0)
        for n in range(nmax+1)]
    for n in range(nmax+1):
        # Coefficient of phi(t)^(2j+1), phi=t*(1-540t²)^(-1/2).
        transformed=Q(0)
        for j in range(n+1):
            h=n-j
            poch=Q(1)
            for k in range(h): poch*=Q(2*j+1+2*k,2)
            fact=1
            for k in range(1,h+1):fact*=k
            transformed+=Q(dd[j],2*j+1)*540**h*poch/fact
        assert transformed==Q(old['r_value'](n,av),2*n+1)
        bprev=beta[n-1] if n else 0
        assert 2*dd[n]==(2*n+1)*(357*beta[n]+192780*bprev)-(151*beta[n]+192780*bprev)
    X,S,U=s.symbols('X S U')
    assert s.expand((X*S*(S*S-4*X)).subs(X,U+S*S/8))==s.expand(-4*S*U*U+S**5/16)
    assert old['a_values'](2,t=-4)[2]==10
    x,y=s.symbols('x y')
    for p,root in ((7,-1),(17,9)):
        cubic=s.Poly((x+y+1)**3-324*x*y*(x+y+1)-540*x*y,x,y,modulus=p).as_expr()
        gb=s.groebner([cubic,s.diff(cubic,x),s.diff(cubic,y)],x,y,modulus=p)
        assert [f.as_expr() for f in gb.polys]==[
            s.Poly(x-root,x,y,modulus=p).as_expr(),s.Poly(y-root,x,y,modulus=p).as_expr()]
        assert beta[(p-1)//2]%p==0
    assert not any(24+12*m==8*a+3*b for m in range(2) for a in range(3) for b in range(4))
    print('Exact odd coordinate transform through degree 33, integer equivalence, D6 normal form: passed.')
    print('Unique cubic nodes mod7/mod17, zero Hasse coefficients, torsion-height exclusion: passed.')
    print('elapsed',round(perf_counter()-start,3),'seconds')
