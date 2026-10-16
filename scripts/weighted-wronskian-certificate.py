"""Exact, bounded checks of the CM correspondence used in the Wronskian proof."""
from pathlib import Path
from time import perf_counter
import sympy as s

if __name__=='__main__':
    start=perf_counter()
    al=(15+s.sqrt(-105))/30
    A=s.Matrix([[15,-11],[30,-15]])
    M=s.Matrix([[7,3],[30,13]])
    Ap=M*A*M.inv()
    gamma=(Ap*s.diag(s.Rational(1,7),1)).adjugate()
    z=s.simplify((M[0,0]*al+M[0,1])/(M[1,0]*al+M[1,1]))
    assert M.det()==1 and M[1,0]%30==0
    assert gamma==s.Matrix([[-6195,1439],[-3810,885]])
    assert gamma.det()==15 and gamma[1,0]%30==0
    assert gamma[0,0]%15==0 and gamma[1,1]%15==0
    den=s.simplify(gamma[1,0]*z+gamma[1,1])
    assert s.simplify(den+s.sqrt(-105)/7)==0
    assert s.simplify((gamma[0,0]*z+gamma[0,1])/den-7*z)==0
    assert s.simplify(den**2+s.Rational(15,7))==0
    # Existing exact modular polynomial, independently differentiate it here.
    T,U,r=s.symbols('T U r')
    pol=s.sympify((Path(__file__).resolve().parents[1] / 'data' / 'modular7-polynomial.txt').read_text(encoding='utf-8'),
                 locals={'T':T,'U':U})
    at={T:-10,U:-10}
    assert pol.subs(at)==0
    assert s.diff(pol,T).subs(at)==s.diff(pol,U).subs(at)!=0
    Upp=s.cancel(-2*(s.diff(pol,T,2)-s.diff(pol,T,U)).subs(at)/s.diff(pol,U).subs(at))
    assert Upp==-s.Rational(122,315)
    # T=-2/r-2; s=-2/(U+2), at r=s=1/4 and dU/dT=-1.
    spp=s.Rational(1,128)*32**2+s.Rational(1,32)*Upp*32**2+s.Rational(1,32)*256
    assert spp==s.Rational(1136,315)
    alpha=2*(9*r**4-19*r**2+5*r+2)/(r*(r-1)*(r+2)*(3*r-2)*(3*r+1))
    rho=s.cancel(-alpha.subs(r,s.Rational(1,4))+spp/2)
    assert rho==-s.Rational(96,35)
    Gsq=r*r*(r+2)*(3*r-2)*(3*r+1)/(4*(r-1))
    assert Gsq.subs(r,s.Rational(1,4))==s.Rational(105,1024)
    print('Exact CM matrices, g^2=7, s prime=-1, s second=1136/315, rho=-96/35: passed.')
    print('elapsed',round(perf_counter()-start,3),'seconds')
