import numpy as np


LARGE = 998244353


def solve_wa(p):
    sq = int(p ** 0.5 + 10)
    primes = np.ones(sq + 1, dtype=np.int64)
    primes[:2] = 0
    for q in range(sq + 1):
        if primes[q]:
            primes[q * q::q] = 0
    primes = np.arange(sq + 1)[primes == 1]
    # print(primes)
    res = 1
    x = p - 1
    for q in primes:
        c = 1
        d = q
        while x % q == 0:
            x //= q
            c += (d * (q - 1)) % LARGE
            d *= (q * q) % LARGE
            d %= LARGE
            c %= LARGE
        # print(res, c, p)
        res *= c
        res %= LARGE
    x %= LARGE
    res *= (1 + x * (x - 1)) % LARGE
    # print(res)
    # print(type(x), type(c), type(d), type(q), type(res))
    return (res + 1) % LARGE


def solve(p):
    sq = int(p ** 0.5 + 10)
    primes = [1] * (sq + 1)
    primes[0] = 0
    primes[1] = 0
    for q in range(sq + 1):
        if primes[q]:
            for r in range(q * q, sq + 1, q):
                primes[r] = 0
    primes = [q for q in range(sq + 1) if primes[q]]
    # print(primes)
    res = 1
    x = p - 1
    for q in primes:
        c = 1
        d = q
        while x % q == 0:
            x //= q
            c += d * (q - 1)
            d *= q * q
            d %= LARGE
            c %= LARGE
        # print(res, c, p)
        res *= c
        res %= LARGE
    res *= 1 + x * (x - 1)
    # print(res)
    return (res + 1) % LARGE


def main():
    p = int(input())
    res = solve_wa(p)
    print(res)


def test_large():
    n = 10 ** 12
    sq = int(n ** 0.5 + 10)
    primes = np.ones(sq + 1, dtype=np.int32)
    primes[:2] = 0
    for q in range(sq + 1):
        if primes[q]:
            primes[q * q::q] = 0
    primes = np.arange(sq + 1)[primes == 1]
    print(primes.shape)

    sq = int(n ** 0.5 + 10)
    primes = [1] * (sq + 1)
    primes[0] = 0
    primes[1] = 0
    for q in range(sq + 1):
        if primes[q]:
            for r in range(q * q, sq + 1, q):
                primes[r] = 0
    primes = [q for q in range(sq + 1) if primes[q]]
    print(len(primes))


def test():
    assert solve(3) == 4
    assert solve(11) == 64
    assert solve(998244353) == 329133417


if __name__ == "__main__":
    test()
    # test_large()
    main()
