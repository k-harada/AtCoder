import numpy as np


def solve(n):
    res_arr = np.ones(n + 1, dtype=int)
    primes = np.ones(n + 1, dtype=int)
    primes[0] = 0
    primes[1] = 0
    for p in range(2, n + 1):
        if primes[p]:
            primes[p * p::p] = 0
        if p * p > n:
            break
    for p in range(2, n + 1):
        if primes[p]:
            d = p
            while True:
                res_arr[d::d] += 1
                d *= p
                if d > n:
                    break
    # print(res_arr)
    return " ".join([str(r) for r in res_arr[1:]])


def main():
    n = int(input())
    res = solve(n)
    print(res)


def test():
    assert solve(4) == "1 2 2 3"


if __name__ == "__main__":
    test()
    main()
