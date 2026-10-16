"""Exact rational quadric comparison along the entire level-30 curve."""
from sympy import QQ
from sympy.polys.fields import field
from time import perf_counter


def add(*rows):return [sum(v) for v in zip(*rows)]
def scale(c,row):return [c*v for v in row]
def outer(u,v):return [[(u[i]*v[j]+v[i]*u[j])/2 for j in range(4)] for i in range(4)]
def matrix_add(*ms):return [[sum(m[i][j] for m in ms) for j in range(4)] for i in range(4)]
def matrix_scale(c,m):return [[c*v for v in row] for row in m]


if __name__=='__main__':
    start=perf_counter()
    K,r=field('r',QQ);zero,one=K.zero,K.one
    e0,e1,e2,e3=([one,zero,zero,zero],[zero,one,zero,zero],
                 [zero,zero,one,zero],[zero,zero,zero,one])
    a=r*(r+2)/(4*(r*r-1));b=-r**4/(16*(r-1)**3*(r+1))
    J=8*a*a+2*a+36*b-1;L=8*a*a+20*a+108*b-1
    u=scale(1/(a*J),[-2*(2*a+1),-(20*a*a+8*a+72*b-1),-2*b*(4*a+5),-b*L])
    v=scale(1/(12*b*b),add(scale(a*(1-4*a),u),[-2,1-10*a,-22*b,b*(1-16*a)]))
    ua=add(scale(1/(a*J),[-4,-40*a-8,-8*b,-b*(16*a+20)]),scale(-(1/a+(16*a+2)/J),u))
    ub=add(scale(1/(a*J),[zero,-72,-2*(4*a+5),-(L+108*b)]),scale(-36/J,u))
    va=scale(1/(12*b*b),add(scale(1-8*a,u),scale(a*(1-4*a),ua),[zero,-10,zero,-16*b]))
    vb=add(scale(1/(12*b*b),add(scale(a*(1-4*a),ub),[zero,zero,-22,1-16*a])),scale(-2/b,v))
    U=add(ub,[zero,zero,u[0],u[1]],scale(u[2],v))
    V=add(va,[zero,v[0],zero,v[2]],scale(v[1],u))
    determinant=1-u[3]*v[3]
    aab=scale(1/determinant,add(U,scale(u[3],V)))
    abb=scale(1/determinant,add(V,scale(v[3],U)))
    aaa=add(ua,scale(u[0],e1),scale(u[1],u),scale(u[2],e3),scale(u[3],aab))
    bbb=add(vb,scale(v[0],e2),scale(v[1],e3),scale(v[2],v),scale(v[3],abb))
    t=a/b;z=b
    C=(1-4*t*z)**3-108*z;B=1+8*t*z;A=1-10*t*z
    Cz=-12*t*(1-4*t*z)**2-108;Czz=96*t*t*(1-4*t*z)
    aa=1/z+Cz/(2*C)-4*t/B
    aaz=-1/z**2+Czz/(2*C)-Cz*Cz/(2*C*C)+32*t*t/(B*B)
    N=768*t**5*z**4+32*t**4*z**3-108*t**3*z*z-192*t*t*z*z+9*t*t*z+78*t*z+t+6
    Nz=3072*t**5*z**3+96*t**4*z*z-216*t**3*z-384*t*t*z+9*t*t+78*t
    bb=-N/(z*B*B*C)
    bbz=-Nz/(z*B*B*C)-bb*(1/z+16*t/B+Cz/C)
    d2=6*t*(t+4)*A*A/(z*z*B**4*C)
    yp=add(scale(t,e1),e2)
    ypp=add(scale(t*t,u),scale(2*t,e3),v)
    yppp=add(scale(t**3,aaa),scale(3*t*t,aab),scale(3*t,abb),bbb)
    w=add(scale(bb,e0),scale(aa/2,yp),scale(one/2,ypp))
    vv=add(scale(bbz+2*aa*bb,e0),scale(2*bb+aaz/2+aa*aa,yp),scale(3*aa/2,ypp),scale(one/2,yppp))
    qmat=matrix_add(outer(e0,w),matrix_scale(-one/4,outer(yp,yp)),matrix_scale(1/(4*d2),outer(vv,vv)))
    ap,bp=a.diff(r),b.diff(r)
    hp=add(scale(ap,e1),scale(bp,e2))
    hpp=add(scale(ap.diff(r),e1),scale(bp.diff(r),e2),scale(ap*ap,u),scale(2*ap*bp,e3),scale(bp*bp,v))
    alpha=2*(9*r**4-19*r*r+5*r+2)/(r*(r-1)*(r+2)*(3*r-2)*(3*r+1))
    beta=(29*r**4+71*r**3+12*r*r-8*r-8)/(4*r*(r-1)**2*(r+1)**2*(r+2)*(3*r-2)*(3*r+1))
    imat=matrix_add(outer(e0,hpp),matrix_scale(-one/2,outer(hp,hp)),matrix_scale(alpha,outer(e0,hp)),matrix_scale(2*beta,outer(e0,e0)))
    er=[-16*(r-2)*(r-1)**3*(r+1),-4*(r-1)**2*(r+2)*(3*r*r-2*r-2),r**3*(3*r*r-8*r+2),zero]
    lam=qmat[0][3]/imat[0][3]
    difference=matrix_add(qmat,matrix_scale(-lam,imat))
    kap=difference[1][1]/(er[1]*er[1])
    assert difference==matrix_scale(kap,outer(er,er))
    import sympy as s
    print('lambda(r) =',s.factor(lam.as_expr()))
    print('kappa(r) =',s.factor(kap.as_expr()))
    print('Exact curve identity passed; elapsed',round(perf_counter()-start,3),'seconds')
