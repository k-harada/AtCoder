import numpy as np


def solve(x):
    primes_flag = np.ones(10 ** 6).astype(np.int)
    primes_flag[:2] = 0
    for p in range(10 ** 3):
        if primes_flag[p] == 1:
            primes_flag[p ** 2:10 ** 6:p] = 0
    for i in range(x, 10 ** 6):
        if primes_flag[i] == 1:
            return i
    return 0


def main():
    x = int(input())
    res = solve(x)
    print(res)


def test():
    assert solve(20) == 23
    assert solve(2) == 2
    assert solve(99992) == 100003


if __name__ == "__main__":
    test()
    main()
