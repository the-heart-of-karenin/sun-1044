"""Exact rational certificates for the section-locus period identities.

Uses rational function field operations instead of a long symbolic expansion.
No numerical series matching is used here.
"""
from time import perf_counter
from sympy import QQ
from sympy.polys.fields import field


def add(*rows):
    return [sum(v) for v in zip(*rows)]


def scale(c,row):
    return [c*v for v in row]


if __name__=='__main__':
    st=perf_counter()
    K,j=field('j',QQ)
    z,o=K.zero,K.one
    deriv=lambda row:[v.diff(j) for v in row]
    e0,e1,e2,e3=([o,z,z,z],[z,o,z,z],[z,z,o,z],[z,z,z,o])
    a=-j*(j+2)/(4*(1-j*j))
    b=-j**4/(16*(j-1)**3*(j+1))
    ap,bp=a.diff(j),b.diff(j)
    J=8*a*a+2*a+36*b-1
    L=8*a*a+20*a+108*b-1
    u=scale(1/(a*J),[-2*(2*a+1),-(20*a*a+8*a+72*b-1),
                      -2*b*(4*a+5),-b*L])
    v=scale(1/(12*b*b),add(scale(a*(1-4*a),u),[-2,1-10*a,-22*b,b*(1-16*a)]))
    r=[-16*(j-2)*(j-1)**3*(j+1),-4*(j-1)**2*(j+2)*(3*j*j-2*j-2),
       j**3*(3*j*j-8*j+2),z]
    row=add(deriv(r),[z,r[0]*ap,r[0]*bp,r[1]*bp+r[2]*ap],
            scale(r[1]*ap,u),scale(r[2]*bp,v))
    lam=(5*j*j+3*j+1)/(j*(j-1)*(j+1))
    assert row==scale(lam,r)
    assert (j*lam).numer[(0,)]==-(j*lam).denom[(0,)]
    print('First derivative relation: exact certificate passed.',flush=True)

    # Partial derivatives before restriction, evaluated in one rational field.
    ua=add(scale(1/(a*J),[-4,-40*a-8,-8*b,-b*(16*a+20)]),
           scale(-(1/a+(16*a+2)/J),u))
    ub=add(scale(1/(a*J),[z,-72,-2*(4*a+5),-(L+108*b)]),scale(-36/J,u))
    va=scale(1/(12*b*b),add(scale(1-8*a,u),scale(a*(1-4*a),ua),[z,-10,z,-16*b]))
    U=add(ub,[z,z,u[0],u[1]],scale(u[2],v))
    V=add(va,[z,v[0],z,v[2]],scale(v[1],u))
    det=1-u[3]*v[3]
    aab=scale(1/det,add(U,scale(u[3],V)))
    abb=scale(1/det,add(V,scale(v[3],U)))
    M=[add(scale(ap,e1),scale(bp,e2)),
       add(scale(ap,u),scale(bp,e3)),
       add(scale(ap,e3),scale(bp,v)),
       add(scale(ap,aab),scale(bp,abb))]
    rows=[e0]
    for _ in range(3):
        prev=rows[-1]
        rows.append(add(deriv(prev),*(scale(prev[i],M[i]) for i in range(4))))
    A=2*(9*j**4-19*j*j+5*j+2)/(j*(j-1)*(j+2)*(3*j-2)*(3*j+1))
    B=(29*j**4+71*j**3+12*j*j-8*j-8)/(4*j*(j-1)**2*(j+1)**2*(j+2)*(3*j-2)*(3*j+1))
    residual=add(rows[3],scale(3*A,rows[2]),scale(A.diff(j)+4*B+2*A*A,rows[1]),
                 scale(2*B.diff(j)+4*A*B,rows[0]))
    mu=residual[0]/r[0]
    assert residual==scale(mu,r)
    assert mu==0
    print('Restricted period: exact symmetric-square certificate passed.',flush=True)

    t=j/(3*j-2)
    N=24300*t**8-58860*t**7+73437*t**6-44294*t**5+15111*t**4-3160*t**3+407*t*t-30*t+1
    Qt=N/(4*t*t*(t-1)**2*(4*t-1)**2*(5*t-1)**2*(9*t-1)**2)
    Qj=B-A.diff(j)/2-A*A/4
    assert Qj==Qt*t.diff(j)**2
    print('Level-30 projective equation: exact rational comparison passed.',flush=True)

    # Direct comparison with the c=-2 normalization of Campbell-Cooper-Ye.
    X=-j/(2*(j+1))
    Xp=X.diff(j)
    G=(1+5*X)*(1+4*X)*(1+X)*(1-4*X)
    HG=-4*X*(1-4*X-58*X*X-75*X**3)
    dG=(G.diff(j)/Xp)
    Ap=(1/X+dG/(2*G))*Xp-Xp.diff(j)/Xp
    Bp=-HG/(4*X*X*G)*Xp*Xp
    ell=-(1/(1-j*j))
    assert A==Ap-2*ell
    assert B==Bp+ell*ell-ell.diff(j)-Ap*ell
    print('Published level-30 normalization: exact pullback certificate passed.',flush=True)
    print('elapsed',round(perf_counter()-st,4),'seconds',flush=True)
