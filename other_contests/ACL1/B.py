from collections import defaultdict
from subprocess import Popen, PIPE
from itertools import chain, combinations
import numpy as np


def ext_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = ext_gcd(b % a, a)
        return g, x - (b // a) * y, y


# from nagiss-san's AC
def fast_prime_factorization(n):
    # 素因数分解（ロー法）  O(n^(1/4) polylog(n))
    return list(map(int, Popen(["factor", str(n)], stdout=PIPE).communicate()[0].split()[1:]))


def solve(n):
    factorization_acl = fast_prime_factorization(2 * n)
    factorization = defaultdict(int)
    for f in factorization_acl:
        factorization[f] += 1
    # print(factorization)
    factor_list = []
    for k in factorization.keys():
        factor_list.append(k ** factorization[k])

    # trivial answer
    res = 2 * n - 1

    # power set
    for s in chain.from_iterable(combinations(factor_list, r) for r in range(len(factor_list) + 1)):
        p = np.int(np.prod(s))
        q = 2 * n // p
        if p == 1 or q == 1:
            continue
        a, x, y = ext_gcd(p, q)
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
