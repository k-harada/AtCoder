def solve(n, m, cs_list):
    res = [-1] * m
    for c, s in cs_list:
        res[c - 1] = max(res[c - 1], s)
    return res


def main():
    n, m = map(int, input().split())
    cs_list = [tuple(map(int, input().split())) for _ in range(n)]
    res = solve(n, m, cs_list)
    print(" ".join([str(r) for r in res]))


def test():
    assert solve(4, 5, [(1, 3), (2, 10), (1, 7), (4, 9)]) == [7, 10, -1, 9, -1]
    assert solve(5, 5, [(2, 6), (5, 12), (5, 2), (5, 9), (2, 7)]) == [-1, 7, -1, -1, 12]


if __name__ == "__main__":
    test()
    main()
