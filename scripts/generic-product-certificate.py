"""Exact rational attempt at the tensor-product structure for arbitrary t."""
from sympy import QQ
from sympy.polys.fields import field
from time import perf_counter


if __name__=='__main__':
    start=perf_counter()
    K,t,z=field('t,z',QQ)
    D=lambda f:f.diff(z)
    # theta coefficients, from the proved fourth-order equation.
    # Rather than expand theta by hand, obtain these four coefficients in SymPy.
    import sympy as s
    T,Z,h=s.symbols('t z h')
    rr=[-h**3*(h-1),
        2*h*((11*T+54)*h**3+(-T+81)*h**2+(7*T+39)*h+T+6),
        -12*T*(2*h+1)*((7*T+45)*h**3+7*T*h**2+(6*T-5)*h+2*T),
        8*T**3*(2*h+1)*(2*h+3)*(17*h**2+24*h+12),
        -80*T**4*(h+1)*(2*h+1)*(2*h+3)*(2*h+5)]
    poly=s.Poly(sum(Z**j*r for j,r in enumerate(rr)),h)
    cs=[K(poly.coeff_monomial(h**j)) for j in range(5)]
    ordinary=[cs[0],z*(cs[1]+cs[2]+cs[3]+cs[4]),
              z*z*(cs[2]+3*cs[3]+7*cs[4]),z**3*(cs[3]+6*cs[4]),z**4*cs[4]]
    c0,c1,c2,c3,_=[v/ordinary[4] for v in ordinary]
    C=(1-4*t*z)**3-108*z;B=1+8*t*z;A=1-10*t*z
    a=1/z+D(C)/(2*C)-4*t/B
    dlog=D(A)/A-1/z-2*D(B)/B-D(C)/(2*C)
    assert c3==4*a-dlog
    H=-dlog
    b=(c2-4*D(a)-5*a*a-3*H*a)/4
    beta=b-D(a)/2-a*a/4
    # Coefficient of D in the gauged tensor-product operator.
    predicted1=4*D(a).diff(z)+12*a*D(a)+4*a**3+H*(3*D(a)+3*a*a)+8*beta*a+4*H*beta+6*D(beta)
    assert c1==predicted1
    base0=D(D(D(a)))+4*a*D(D(a))+3*D(a)**2+6*a*a*D(a)+a**4
    base0+=H*(D(D(a))+3*a*D(a)+a**3)+4*beta*(D(a)+a*a)
    base0+=(4*H*beta+6*D(beta))*a+2*H*D(beta)+2*D(D(beta))
    d2=(c0-base0)/4
    norm=d2*z*z*B**4*C/(A*A)
    print('b =',b)
    assert b==-(768*t**5*z**4+32*t**4*z**3-108*t**3*z*z-192*t*t*z*z+9*t*t*z+78*t*z+t+6)/(z*B*B*C)
    print('d2 normalization =',norm)
    assert norm==6*t*(t+4)
    assert D(d2)/(2*d2)==dlog
    print('All four coefficient identities passed; elapsed',round(perf_counter()-start,3),'seconds')
