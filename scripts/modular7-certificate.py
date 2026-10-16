"""Bounded exact construction of the level-30 degree-seven modular equation.

All series arithmetic is over integers. Mathematical divisor bounds, not
series agreement alone, are required for the final modular-identity proof.
"""
from time import perf_counter
from math import gcd
from functools import reduce
import sympy as s


def mul(a,b,n):
    c=[0]*n
    for i,u in enumerate(a):
        if not u:
            continue
        for j,v in enumerate(b[:n-i]):
            if v:
                c[i+j]+=u*v
    return c


def eta_series(n,reverse=False):
    f=[1]+[0]*(n-1)
    for d,sg in [(1,1),(2,1),(3,-1),(5,-1),(6,-1),(10,-1),(15,1),(30,1)]:
        if reverse:
            sg=-sg
        for k in range(d,n,d):
            if sg==1:
                for i in range(n-1,k-1,-1):
                    f[i]-=f[i-k]
            else:
                for i in range(k,n):
                    f[i]+=f[i-k]
    return f


if __name__=='__main__':
    start=perf_counter()
    n=195
    p,pi=eta_series(n),eta_series(n,True)
    Q=pi[:]
    for k in range(2,n):
        Q[k]+=p[k-2]
    Q[1]-=2
    powers=[[1]+[0]*(n-1)]
    for _ in range(8):
        powers.append(mul(powers[-1],Q,n))
    powers7=[]
    for row in powers:
        powers7.append([row[k//7] if k%7==0 else 0 for k in range(n)])
    cols=[]
    pairs=[(i,j) for i in range(9) for j in range(i,9)]
    exps=list(range(-64,130))
    for i,j in pairs:
        f=mul(powers[i],powers7[j],n)
        g=mul(powers[j],powers7[i],n) if i!=j else None
        cols.append([(f[e+i+7*j] if 0<=e+i+7*j<n else 0)
                     +(g[e+j+7*i] if g is not None and 0<=e+j+7*i<n else 0) for e in exps])
    # Use only exponents through 45 to construct the equation; reserve the
    # remaining coefficients for a separate exact validation.
    rows=[[col[k] for col in cols] for k,e in enumerate(exps) if e<=45]
    M=s.polys.matrices.DomainMatrix.from_list(rows,s.QQ)
    ker=M.nullspace().to_Matrix()
    assert ker.rows==1
    vals=[int(v) for v in ker.tolist()[0]]
    common=reduce(gcd,vals)
    vals=[v//common for v in vals]
    T,U=s.symbols('T U')
    poly=sum(c*(T**i*U**j+(T**j*U**i if i!=j else 0)) for c,(i,j) in zip(vals,pairs))
    if s.Poly(poly,U).coeff_monomial(U**8).subs(T,0)<0:
        vals=[-v for v in vals]
        poly=-poly
    assert all(sum(v*col[k] for v,col in zip(vals,cols))==0 for k in range(len(exps)))
    print('Exact modular-equation series certificate through q^129 passed.',flush=True)
    print('Diagonal factorization:',s.factor(poly.subs(U,T)),flush=True)
    point={T:-10,U:-10}
    print('At T=U=-10: F_T, F_TT, F_TU =',
          s.diff(poly,T).subs(point),s.diff(poly,T,2).subs(point),s.diff(poly,T,U).subs(point),flush=True)
    from pathlib import Path
    (Path(__file__).resolve().parents[1] / 'data' / 'modular7-polynomial.txt').write_text(str(s.expand(poly)),encoding='utf-8')
    print('Saved modular7-polynomial.txt; elapsed',round(perf_counter()-start,4),'seconds',flush=True)
