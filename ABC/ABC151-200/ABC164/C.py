import numpy as np


def solve(n, s_list):
    return np.unique(s_list).shape[0]


def main():
    n = int(input())
    s_list = [input() for _ in range(n)]
    res = solve(n, s_list)
    print(res)


def test():
    assert solve(3, ["apple", "orange", "apple"]) == 2
    assert solve(5, ["grape", "grape", "grape", "grape", "grape"]) == 1
    assert solve(4, ["aaaa", "a", "aaa", "aa"]) == 4


if __name__ == "__main__":
    test()
    main()
