"""Tiny, bounded exact checks of transcriptions and the new coefficient reduction.

These finite checks do not prove either of Sun's conjectures.
"""
from math import comb
from time import perf_counter


def truncated(p):
    mod = p*p
    return sum(comb(2*n, n)
               * sum(comb(n, k)*comb(n+2*k, 2*k)*comb(2*k, k)
                     * pow(-324, n-k, mod) for k in range(n+1))
               * pow(pow(2160, n, mod), -1, mod)
               for n in range(p)) % mod


def polynomial_coefficient(p):
    terms = {(1, 1): -1, (2, 1): 1, (1, 2): 1,
             (2, 2): 864, (3, 2): -1404, (2, 3): -1404,
             (4, 2): 540, (3, 3): 1080, (2, 4): 540}
    result = {(0, 0): 1}
    for _ in range((p-1)//2):
        new = {}
        for (i, j), c in result.items():
            for (a, b), d in terms.items():
                if i+a < p and j+b < p:
                    pair = i+a, j+b
                    new[pair] = (new.get(pair, 0)+c*d) % p
        result = new
    return pow(15, (p-1)//2, p)*result.get((p-1, p-1), 0) % p


if __name__ == "__main__":
    start = perf_counter()
    examples = [(109, 4*2**2-2*109), (53, 2-2*53),
                (47, 2*47-12*2**2), (19, 2*19-6),
                (41, 20*2**2-2*41), (13, 10-2*13),
                (43, 28*2**2-2*43), (11, 14-2*11), (17, 0)]
    values = {p: truncated(p) for p, _ in examples}
    for p, expected in examples:
        assert values[p] == expected % (p*p)
    print("One small example in each of nine branches: all match")
    for p in (11, 13, 17):
        assert polynomial_coefficient(p) == values[p] % p
    print("Fixed polynomial coefficient reduction at p=11,13,17: all match")
    print("elapsed", round(perf_counter()-start, 4), "seconds")
