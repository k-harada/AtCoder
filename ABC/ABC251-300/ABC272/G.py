import numpy as np
from collections import defaultdict


def calc_div(n):
    sq = int(n ** 0.5 + 10)
    x = np.arange(1, sq)
    x = x[n % x == 0]
    x = np.concatenate((x, n // x))
    return np.unique(x)


def solve(n, a_list):

    failed = defaultdict(int)
    failed[1] = 1
    failed[2] = 1

    for _ in range(50):
        i, j = np.random.choice(n, 2, replace=False)
        d_ij = abs(a_list[i] - a_list[j])
        divisors = calc_div(d_ij)
        for d in divisors:
            if failed[d]:
                continue
            a_count = defaultdict(int)
            for a in a_list:
                a_count[a % d] += 1
            c = max(a_count.values())
            if c > n - c:
                return d
            else:
                failed[d] = 1

    return -1


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)


def test():
    # assert solve(5, [3, 17, 8, 14, 10]) == 7
    # assert solve(10, [822848257, 553915718, 220834133, 692082894, 567771297, 176423255, 25919724, 849988238, 85134228, 235637759]) == 37
    assert solve(10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == -1


def test_large():
    print(solve(5000, list(range(1, 2501)) + list(range(10 ** 9 + 1, 10 ** 9 + 2501))))


if __name__ == "__main__":
    # test()
    # test_large()
    main()
