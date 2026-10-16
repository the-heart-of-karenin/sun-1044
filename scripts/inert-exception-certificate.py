"""Two finite exceptions to the rational differential-basis argument."""
from math import comb


def original_sum(p):
    modulus=p*p
    inv2160=pow(2160,-1,modulus)
    total=0
    for n in range(p):
        an=sum(comb(n,k)*comb(n+2*k,2*k)*comb(2*k,k)
               *pow(-324,n-k,modulus) for k in range(n+1))%modulus
        total=(total+comb(2*n,n)*an*pow(inv2160,n,modulus))%modulus
    return total


if __name__=='__main__':
    for p in (17,331):
        assert pow(-105,(p-1)//2,p)==p-1
        value=original_sum(p)
        assert value==0
        print('S_'+str(p)+' = '+str(value)+' (mod '+str(p*p)+')')
