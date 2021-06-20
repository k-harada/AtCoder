import numpy as np


def solve(l, r):
    res = 0
    factors_count = - np.ones(r + 1, dtype=int)
    primes = np.ones(r + 1, dtype=int)
    primes[:2] = 0
    for p in range(2, r + 1):
        if p * p > r:
            break
        primes[p * p::p] = 0
    for d in range(2, r + 1):
        if primes[d]:
            factors_count[d::d] *= -1
    for d in range(2, r + 1):
        factors_count[d * d::d * d] = 0
    # print(factors_count[:100])
    # l < r, i != r, g > 1
    for d in range(2, r - l + 1):
        left = (l // d) * d
        right = (r // d) * d
        if left < l:
            left += d
        if right <= left:
            c = 0
        else:
            c = (right - left) // d + 1
            c = c * (c - 1) // 2
        pc = factors_count[d]
        res += c * pc
    # print(res)
    # avoid l == d
    for d in range(max(2, l), r // 2 + 1):
        right = (r // d) * d
        res -= (right - d) // d
    res *= 2
    # print(res)
    return res


def main():
    l, r = map(int, input().split())
    res = solve(l, r)
    print(res)


def test():
    assert solve(3, 7) == 2
    assert solve(4, 10) == 12
    assert solve(1, 1000000) == 392047955148


if __name__ == "__main__":
    test()
    main()
