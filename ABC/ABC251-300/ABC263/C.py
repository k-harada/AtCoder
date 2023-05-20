import math
from itertools import combinations_with_replacement


def solve(n, m):
    k = math.comb(m, m - n)
    res = [list(range(1, n + 1)) for _ in range(k)]
    ind = k - 1
    for c in combinations_with_replacement(range(n + 1), m - n):
        add = 0
        c_count = [0] * (n + 1)
        for i in c:
            c_count[i] += 1
        for j in range(n):
            add += c_count[j]
            res[ind][j] += add
        ind -= 1
    # print(res)
    return res


def main():
    n, m = map(int, input().split())
    res = solve(n, m)
    for r in res:
        print(" ".join([str(i) for i in r]))


def test():
    assert solve(2, 3) == [[1, 2], [1, 3], [2, 3]]
    assert solve(3, 5) == [
        [1, 2, 3], [1, 2, 4], [1, 2, 5], [1, 3, 4], [1, 3, 5], [1, 4, 5], [2, 3, 4], [2, 3, 5], [2, 4, 5], [3, 4, 5]
    ]


if __name__ == "__main__":
    test()
    main()
