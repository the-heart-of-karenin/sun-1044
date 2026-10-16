"""Exact rational comparison of two period quadrics at the required point.

This is a symbolic certificate, not a numerical prime search.
"""
from sympy import QQ, Matrix, Rational as R, symbols, diff, cancel
from sympy.polys.fields import field
from time import perf_counter


def add(*rows):
    return [sum(v) for v in zip(*rows)]


def scale(c,row):
    return [c*v for v in row]


def outer(u,v):
    return (Matrix(u)*Matrix(v).T+Matrix(v)*Matrix(u).T)/2


if __name__=='__main__':
    start=perf_counter()
    K,a,b=field('a,b',QQ)
    z,o=K.zero,K.one
    e0,e1,e2,e3=([o,z,z,z],[z,o,z,z],[z,z,o,z],[z,z,z,o])
    J=8*a*a+2*a+36*b-1
    L=8*a*a+20*a+108*b-1
    u=scale(1/(a*J),[-2*(2*a+1),-(20*a*a+8*a+72*b-1),
                    -2*b*(4*a+5),-b*L])
    v=scale(1/(12*b*b),add(scale(a*(1-4*a),u),[-2,1-10*a,-22*b,b*(1-16*a)]))
    ua=[c.diff(a) for c in u];ub=[c.diff(b) for c in u]
    va=[c.diff(a) for c in v];vb=[c.diff(b) for c in v]
    U=add(ub,[z,z,u[0],u[1]],scale(u[2],v))
    V=add(va,[z,v[0],z,v[2]],scale(v[1],u))
    det=1-u[3]*v[3]
    aab=scale(1/det,add(U,scale(u[3],V)))
    abb=scale(1/det,add(V,scale(v[3],U)))
    aaa=add(ua,scale(u[0],e1),scale(u[1],u),scale(u[2],e3),scale(u[3],aab))
    bbb=add(vb,scale(v[0],e2),scale(v[1],e3),scale(v[2],v),scale(v[3],abb))
    aval,bval=QQ(-3,20),QQ(1,2160)
    def ev(row):
        def poly(p):
            return sum(coef*aval**powers[0]*bval**powers[1] for powers,coef in p.items())
        return [R(poly(c.numer)/poly(c.denom)) for c in row]
    e0,e1,e2,e3,u,v,aaa,aab,abb,bbb=map(ev,(e0,e1,e2,e3,u,v,aaa,aab,abb,bbb))
    from sympy import factorint, ilcm
    denominator=ilcm(*[c.q for row in (u,v,aaa,aab,abb,bbb) for c in row])
    print('Elimination denominator primes:',factorint(denominator))
    x=symbols('x')
    C=(1+12*x)**3-x;B=1-24*x;A=1+30*x
    N=3359232*x**4-46656*x**3-52200*x**2-1419*x+53
    aa=1/x+diff(C,x)/(2*C)+12/B
    bb=N/(18*x*B**2*C)
    d2=R(160,3)*A**2/(x**2*B**4*C)
    at=lambda c:cancel(c).subs(x,R(1,20))
    y=e0
    yp=add(scale(-3,e1),scale(R(1,108),e2))
    ypp=add(scale(9,u),scale(R(-1,18),e3),scale(R(1,11664),v))
    yppp=add(scale(-27,aaa),scale(R(1,4),aab),scale(R(-1,1296),abb),scale(R(1,1259712),bbb))
    w=add(scale(at(bb),y),scale(at(aa)/2,yp),scale(R(1,2),ypp))
    t=add(scale(at(diff(bb,x)+2*aa*bb),y),
          scale(at(2*bb+diff(aa,x)/2+aa*aa),yp),
          scale(3*at(aa)/2,ypp),scale(R(1,2),yppp))
    quad=outer(y,w)-outer(yp,yp)/4+outer(t,t)/(4*at(d2))
    r=symbols('r')
    ar=r*(r+2)/(4*(r*r-1));br=-r**4/(16*(r-1)**3*(r+1))
    ar1=diff(ar,r).subs(r,R(1,4));br1=diff(br,r).subs(r,R(1,4))
    hp=add(scale(ar1,e1),scale(br1,e2))
    hpp=add(scale(diff(ar,r,2).subs(r,R(1,4)),e1),
            scale(diff(br,r,2).subs(r,R(1,4)),e2),
            scale(ar1*ar1,u),scale(2*ar1*br1,e3),scale(br1*br1,v))
    alpha=2*(9*r**4-19*r*r+5*r+2)/(r*(r-1)*(r+2)*(3*r-2)*(3*r+1))
    beta=(29*r**4+71*r**3+12*r*r-8*r-8)/(4*r*(r-1)**2*(r+1)**2*(r+2)*(3*r-2)*(3*r+1))
    ii=outer(y,hpp)-outer(hp,hp)/2+alpha.subs(r,R(1,4))*outer(y,hp)+2*beta.subs(r,R(1,4))*outer(y,y)
    er=[-16*(r-2)*(r-1)**3*(r+1),-4*(r-1)**2*(r+2)*(3*r*r-2*r-2),r**3*(3*r*r-8*r+2),0*r]
    er=[c.subs(r,R(1,4)) for c in er]
    lam=cancel(quad[0,3]/ii[0,3])
    kap=cancel((quad-lam*ii)[1,1]/(er[1]*er[1]))
    assert quad==lam*ii+kap*outer(er,er)
    print('Q_fixed = lambda * I_restricted + kappa * E^2')
    print('lambda =',lam)
    print('kappa =',kap)
    print('Exact quadratic-form identity passed.')
    print('elapsed',round(perf_counter()-start,3),'seconds')
