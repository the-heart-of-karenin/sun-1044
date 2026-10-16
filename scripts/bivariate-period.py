"""Exact two-variable period equations; no work runs on import."""
import sympy as s

a,b = s.symbols('a b')


def second_derivatives():
    """Rows expressing H_aa and H_bb in (H,H_a,H_b,H_ab)."""
    J = 8*a*a+2*a+36*b-1
    K = 8*a*a+20*a+108*b-1
    u = s.Matrix([[-2*(2*a+1), -(20*a*a+8*a+72*b-1),
                   -2*b*(4*a+5), -b*K]])/(a*J)
    v = (a*(1-4*a)*u+s.Matrix([[-2,1-10*a,-22*b,b*(1-16*a)]]))/(12*b*b)
    return u.applyfunc(s.cancel),v.applyfunc(s.cancel)


def verify_coefficients():
    """Generic coefficient identities; boundary cases are in the note."""
    m,k=s.symbols('m k')
    am=m*(m+k)/(2*(2*m+2*k-1)*(m+3*k))
    am2=am*(m-1)*(m+k-1)/(2*(2*m+2*k-3)*(m+3*k-1))
    bk=k**3*(m+k)/(2*(2*m+2*k-1)*(m+3*k)*(m+3*k-1)*(m+3*k-2))
    p1=m*(m+k)-2*(2*m+2*k-1)*(m+3*k)*am
    p2=-(m*m+m*k)
    p2+=(2+6*(m-1)+10*k+2*(m-1)**2+20*(m-1)*k)*am
    p2+=(4+12*(m-2)+8*k+8*(m-2)**2+8*(m-2)*k)*am2
    p2+=(36*m+36*m*m+108*m*(k-1))*bk
    assert s.cancel(p1)==0
    assert s.cancel(p2)==0


if __name__=='__main__':
    verify_coefficients()
    print('Both generic bivariate coefficient identities verified exactly.')
