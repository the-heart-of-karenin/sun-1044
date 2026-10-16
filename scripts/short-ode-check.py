"""Bounded modular linear algebra; no background jobs or open-ended searches.

This is a discovery aid, not a proof of a guessed differential equation.
"""
from math import comb
from time import perf_counter

P = 2**127 - 1
N = 80


def nullspace_mod(rows, cols):
    a = [r[:] for r in rows]
    pivots = []
    rank = 0
    for col in range(cols):
        idx = next((i for i in range(rank, len(a)) if a[i][col]), None)
        if idx is None:
            continue
        a[rank], a[idx] = a[idx], a[rank]
        inv = pow(a[rank][col], -1, P)
        a[rank] = [v * inv % P for v in a[rank]]
        for i in range(len(a)):
            if i != rank and a[i][col]:
                c = a[i][col]
                a[i] = [(v - c * w) % P for v, w in zip(a[i], a[rank])]
        pivots.append(col)
        rank += 1
        if rank == len(a):
            break
    free = [j for j in range(cols) if j not in pivots]
    basis = []
    for j in free:
        v = [0] * cols
        v[j] = 1
        for i, c in enumerate(pivots):
            v[c] = -a[i][j] % P
        basis.append(v)
    return basis


def rational_reconstruction(a):
    bound = (P // 2) ** 0.5
    r0, r1, v0, v1 = P, a, 0, 1
    while abs(r1) > bound:
        q = r0 // r1
        r0, r1, v0, v1 = r1, r0 - q * r1, v1, v0 - q * v1
    if v1 == 0:
        raise ArithmeticError("Failed to reconstruct")
    if v1 < 0:
        r1, v1 = -r1, -v1
    return r1, v1


def main():
    start = perf_counter()
    coeffs = [
        comb(2 * n, n)
        * sum(comb(n, k) * comb(n + 2 * k, 2 * k) * comb(2 * k, k)
              * (-324) ** (n - k) for k in range(n + 1)) % P
        for n in range(N)
    ]
    for order, degree in [(3, 4), (4, 4), (4, 5), (4, 6)]:
        cols = (order + 1) * (degree + 1)
        rows = [[pow(n - j, r, P) * coeffs[n - j] % P if n >= j else 0
                 for j in range(degree + 1) for r in range(order + 1)]
                for n in range(N)]
        basis = nullspace_mod(rows, cols)
        print("order", order, "z-degree", degree, "nullity", len(basis))
        if basis:
            vector = basis[0]
            pivot = next(c for c in vector if c)
            vector = [c * pow(pivot, -1, P) % P for c in vector]
            for j in range(degree + 1):
                print(j, [rational_reconstruction(c)
                          for c in vector[j * (order + 1):(j + 1) * (order + 1)]])
            break
    print("elapsed", round(perf_counter() - start, 4), "seconds")


if __name__ == "__main__":
    main()
