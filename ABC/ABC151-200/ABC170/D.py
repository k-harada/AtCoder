from collections import Counter
import numpy as np


def solve(n, a_list):
    count_a = Counter(a_list)
    res = 0
    # sieve
    sieve = np.ones(10 ** 6 + 1)
    for i in range(10 ** 6 + 1):
        if sieve[i]:
            if count_a[i] > 0:
                sieve[i::i] = 0
            if count_a[i] == 1:
                res += 1
    return res


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(5, [24, 11, 8, 3, 16]) == 3
    assert solve(4, [5, 5, 5, 5]) == 0
    assert solve(10, [33, 18, 45, 28, 8, 19, 89, 86, 2, 4]) == 5


if __name__ == "__main__":
    test()
    main()
