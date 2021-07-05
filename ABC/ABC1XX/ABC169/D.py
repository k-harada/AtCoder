import numpy as np


def solve(n):
    # primes
    primes = np.ones(10 ** 6 + 1, dtype=int)
    primes[:2] = 0
    for p in range(2, 10 ** 6 + 1):
        if primes[p]:
            primes[p * p::p] = 0

    res = 0
    for p in range(10 ** 6 + 1):
        if primes[p] and n % p == 0:
            c = 0
            while n % p == 0:
                n = n // p
                c += 1
            d = 1
            while c >= d:
                c -= d
                res += 1
                d += 1
    if n > 1:
        res += 1

    return res


def main():
    n = int(input())
    res = solve(n)
    print(res)


def test():
    assert solve(24) == 3
    assert solve(1) == 0
    assert solve(64) == 3
    # assert solve(1000000007) == 1
    # assert solve(997764507000) == 7


if __name__ == "__main__":
    test()
    main()
