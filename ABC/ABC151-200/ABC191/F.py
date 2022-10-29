import numpy as np


def calc_div(n):
    sq = int(n ** 0.5 + 10)
    x = np.arange(1, sq)
    x = x[n % x == 0]
    x = np.concatenate((x, n // x))
    return np.unique(x)


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def solve(n, a_list):
    f_dict = dict()
    m = min(a_list)
    a_list = np.unique(a_list)
    n = a_list.shape[0]
    for i in range(n):
        a = a_list[i]
        for b in calc_div(a):
            if b in f_dict.keys():
                f_dict[b] = gcd(f_dict[b], a)
            else:
                f_dict[b] = a
    res = 0
    for d in f_dict.keys():
        if f_dict[d] == d <= m and f_dict[d]:
            res += 1
    return res


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(3, [6, 9, 12]) == 2
    assert solve(4, [8, 2, 12, 6]) == 1
    assert solve(7, [30, 28, 33, 49, 27, 37, 48]) == 7


if __name__ == "__main__":
    test()
    main()
