"""A bounded probe at selected prime powers, not a prime search or proof."""
from math import comb
from time import perf_counter


def a_values(nmax,t=-324):
    values=[]
    for n in range(nmax+1):
        if n==0:
            values.append(1)
            continue
        total=0
        for j in range(1,min(4,n)+1):
            h=n-j
            if j==1:c=(t+27)*h*h+(5*t+27)*h+t+6
            elif j==2:c=3*t*((t+18)*h*h-2*t*h-t-2)
            elif j==3:c=-t**3*h*(5*h+3)
            else:c=2*t**4*(h+1)**2
            total+=c*values[h]
        assert total%(n*n)==0
        values.append(total//(n*n))
    return values


def r_value(n,av):
    return sum((357*k+103)*av[k]*comb(2*n-2*k,n-k)*135**(n-k)
               for k in range(n+1))


if __name__=='__main__':
    start=perf_counter()
    targets=((5,2),(5,3),(7,2),(7,3),(11,2),(13,2),(17,2),(19,2))
    av=a_values(max((p**r-1)//2 for p,r in targets))
    for p,r in targets:
        index=(p**r-1)//2
        val=r_value(index,av)
        vp=0;unit=val
        while unit%p==0:
            vp+=1;unit//=p
        eps=1 if p%4==1 else -1
        chi=0 if p in (3,5) else (1 if pow(15,(p-1)//2,p)==1 else -1)
        expected=(54*chi**r+49*eps**r)%p
        print('p,r=',p,r,'valuation',vp,'R/p^r modp=',val//(p**r)%p,
              'tentative two-character value=',expected,flush=True)
    print('elapsed',round(perf_counter()-start,3),'seconds')
