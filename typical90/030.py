import numpy as np
import numba


@numba.jit
def pre_solve():
    n = 10 ** 7
    primes = np.ones(n + 1, dtype=np.int32)
    primes[:2] = 0
    for p in range(n + 1):
        if p * p > n:
            break
        if primes[p]:
            primes[p * p::p] = 0

    res_array = np.zeros(n + 1, dtype=np.int32)
    for p in range(n + 1):
        if primes[p]:
            res_array[p::p] += 1
    return res_array


res_array = pre_solve()


def solve(n, k):
    res = (res_array[:n + 1] >= k).astype(np.int32).sum()
    return res


def main():
    n, k = map(int, input().split())
    res = solve(n, k)
    print(res)


def test():
    assert solve(15, 2) == 5
    assert solve(30, 2) == 13
    assert solve(200, 4) == 0
    assert solve(869120, 1) == 869119
    assert solve(10000000, 3) == 6798027


if __name__ == "__main__":
    test()
    main()
