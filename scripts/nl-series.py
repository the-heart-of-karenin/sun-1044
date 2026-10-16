"""Bounded series exploration along the explicit section locus.

This is a discovery calculation, not a proof of a differential identity.
It uses 80 coefficients modulo one prime and at most degree 12.
"""
from math import factorial
from time import perf_counter

P = 1000000007


def conv(a, b, n):
    out = [0]*n
    ia = [(i, v) for i, v in enumerate(a) if v]
    ib = [(i, v) for i, v in enumerate(b) if v]
    for i, u in ia:
        for j, v in ib:
            if i+j >= n:
                break
            out[i+j] = (out[i+j]+u*v) % P
    return out


def series(n=80):
    inv4, inv16 = pow(4, -1, P), pow(16, -1, P)
    aa = [0]+[(-2 if i % 2 else -1)*inv4 % P for i in range(1,n)]
    bb = [0]*4+[((i+2)**2//4)*inv16 % P for i in range(n-4)]
    one = [1]+[0]*(n-1)
    ap, bp = [one], [one]
    for _ in range(n-1):
        ap.append(conv(ap[-1], aa, n))
    for _ in range((n-1)//4):
        bp.append(conv(bp[-1], bb, n))
    fac = [factorial(i) % P for i in range(2*n+5)]
    inv = [pow(u, -1, P) for u in fac]

    def coeff(m,k):
        return fac[2*(m+k)]*inv[m+k]**2*fac[m+3*k]*inv[m]*inv[k]**3 % P

    out = [[0]*n for _ in range(3)]
    for k in range((n-1)//4+1):
        for m in range(n-4*k):
            term = conv(ap[m], bp[k], n)
            cs = [coeff(m,k), (m+1)*coeff(m+1,k), (k+1)*coeff(m,k+1)]
            for row, c in zip(out, cs):
                for i in range(m+4*k,n):
                    row[i] = (row[i]+c*term[i]) % P
    return out


def kernel(rows, width):
    rows = [r[:] for r in rows]
    pivots, rank = [], 0
    for col in range(width):
        pivot = next((i for i in range(rank,len(rows)) if rows[i][col]),None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        iv = pow(rows[rank][col],-1,P)
        rows[rank] = [a*iv % P for a in rows[rank]]
        for i in range(len(rows)):
            if i != rank and rows[i][col]:
                v = rows[i][col]
                rows[i] = [(a-v*b) % P for a,b in zip(rows[i],rows[rank])]
        pivots.append(col)
        rank += 1
    free = [j for j in range(width) if j not in pivots]
    if not free:
        return None
    v = [0]*width
    v[free[0]] = 1
    for i, col in enumerate(pivots):
        v[col] = -rows[i][free[0]] % P
    return v


if __name__ == '__main__':
    from fractions import Fraction
    start = perf_counter()
    fs = series()
    print('first coefficients modulo P', [r[:8] for r in fs])
    for degree in range(13):
        rows = [[(fs[k][i-j] if i >= j else 0)
                 for k in range(3) for j in range(degree+1)]
                for i in range(80)]
        v = kernel(rows, 3*(degree+1))
        if v is not None:
            print('first relation degree', degree)
            # Rational reconstruction is deliberately separate from proof.
            def reconstruct(a):
                r0,r1,t0,t1=P,a,0,1
                bound=int((P//2)**.5)
                while abs(r1)>bound:
                    q=r0//r1
                    r0,r1=r1,r0-q*r1
                    t0,t1=t1,t0-q*t1
                return str(Fraction(r1,t1))
            print([[reconstruct(a) for a in v[k*(degree+1):(k+1)*(degree+1)]] for k in range(3)])
            break
    else:
        print('No relation within the stated degree bound.')
    print('elapsed',round(perf_counter()-start,4),'seconds')
