"""Bounded discovery probe, not a proof of a Frobenius congruence."""
from math import factorial
from time import perf_counter
from importlib.util import spec_from_file_location, module_from_spec
from pathlib import Path

_spec = spec_from_file_location('modular7', Path(__file__).with_name('modular7-certificate.py'))
_module = module_from_spec(_spec)
_spec.loader.exec_module(_module)
eta_series = _module.eta_series


def probe(p, length, precision=2):
    mod = p**precision
    n = length
    one = [1]+[0]*(n-1)

    def add(a,b): return [(x+y)%mod for x,y in zip(a,b)]
    def scale(c,a): return [c*x%mod for x in a]
    def mul(a,b):
        c=[0]*n
        for i,u in enumerate(a):
            if not u:continue
            for j,v in enumerate(b[:n-i]):
                if v:c[i+j]=(c[i+j]+u*v)%mod
        return c
    def inv(a):
        c=[pow(a[0],-1,mod)]+[0]*(n-1)
        for k in range(1,n):c[k]=-sum(a[j]*c[k-j] for j in range(1,k+1))*c[0]%mod
        return c
    def sqrt(a):
        assert a[0]==1
        c=one[:]
        for k in range(1,n):c[k]=(a[k]-sum(c[j]*c[k-j] for j in range(1,k)))*pow(2,-1,mod)%mod
        return c

    ep=eta_series(n); ei=eta_series(n,True)
    tq=[x%mod for x in ei]
    for k in range(2,n):tq[k]=(tq[k]+ep[k-2])%mod
    tq[1]=(tq[1]-2)%mod
    X=[0]+inv(tq)[:-1]
    rr=scale(-2,mul(X,inv(add(one,scale(2,X)))))
    rr2=mul(rr,rr)
    aa=scale(-pow(4,-1,mod),mul(mul(rr,add(rr,scale(2,one))),inv(add(one,scale(-1,rr2)))))
    bb=scale(pow(16,-1,mod),mul(mul(rr2,rr2),inv(mul(mul(add(one,scale(-1,rr)),mul(add(one,scale(-1,rr)),add(one,scale(-1,rr)))),add(one,rr)))))
    E=one[:]
    for d in (1,2,3,5,6,10,15,30):
        for k in range(d,n,d):
            for i in range(n-1,k-1,-1):E[i]=(E[i]-E[i-k])%mod
    Z=sqrt(mul(E,mul(tq,mul(tq,tq))))
    H=mul(add(one,scale(4,X)),Z)
    ap=[one]; bp=[one]
    for _ in range(p-1):ap.append(mul(ap[-1],aa));bp.append(mul(bp[-1],bb))
    Sp=[0]*n
    for nn in range(p):
        for k in range(nn+1):
            m=nn-k
            if m+4*k>=n:continue
            c=factorial(2*nn)*factorial(nn+2*k)//(factorial(nn)**2*factorial(m)*factorial(k)**3)%mod
            if c:Sp=add(Sp,scale(c,mul(ap[m],bp[k])))
    Hp=[H[k//p] if k%p==0 else 0 for k in range(n)]
    defect=add(mul(Sp,Hp),scale(-1,H))
    bad=[(k,v) for k,v in enumerate(defect) if v]
    return bad[:5],len(bad)


if __name__=='__main__':
    start=perf_counter()
    for p in (11,13,17,19):
        bad,count=probe(p,4*p)
        print(p,'first defects:',bad,'nonzero count',count,flush=True)
    print('elapsed',round(perf_counter()-start,3),'seconds',flush=True)
