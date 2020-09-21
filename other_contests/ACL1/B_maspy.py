import numpy as np
from collections import defaultdict
from itertools import chain, combinations


def ext_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = ext_gcd(b % a, a)
        return g, x - (b // a) * y, y


def calc_div(n):
    sq = int(n**.5 + 10)
    x = np.arange(1, sq)
    x = x[n % x == 0]
    x = np.concatenate((x, n // x))
    return np.unique(x)


def solve(n):
    if n == 1:
        return 1
    factors = calc_div(2 * n)
    # print(factors)
    # trivial answer
    res = 2 * n - 1

    # power set
    for p in factors:
        q = (2 * n) // p
        if p == 1 or q == 1:
            continue
        a, x, y = ext_gcd(p, q)
        if a > 1:
            continue
        if x < 0:
            res = min(res, abs(p * x))
        else:
            res = min(res, abs(q * y))
        # print(p, q, p * x, q * y)
    # print(res)
    return res


def main():
    n = int(input())
    res = solve(n)
    print(res)


def test():
    assert solve(11) == 10
    assert solve(20200920) == 1100144


if __name__ == "__main__":
    test()
    main()
