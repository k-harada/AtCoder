def solve(n, m, ab_list, k, cd_list):
    res = 0
    for i in range(2 ** k):
        judge = [0] * (n + 1)
        for j in range(k):
            judge[cd_list[j][i % 2]] = 1
            i = i // 2
        r = 0
        for a, b in ab_list:
            r += judge[a] * judge[b]
        res = max(res, r)
    return res


def main():
    n, m = map(int, input().split())
    ab_list = [tuple(map(int, input().split())) for _ in range(m)]
    k = int(input())
    cd_list = [tuple(map(int, input().split())) for _ in range(k)]
    res = solve(n, m, ab_list, k, cd_list)
    print(res)


def test():
    assert solve(4, 4, [(1, 2), (1, 3), (2, 4), (3, 4)], 3, [(1, 2), (1, 3), (2, 3)]) == 2
    assert solve(4, 4, [(1, 2), (1, 3), (2, 4), (3, 4)], 4, [(3, 4), (1, 2), (2, 4), (2, 4)]) == 4


def test_large():
    assert solve(100, 100, [(1, 2)] * 100, 16, [(1, 2)] * 16) == 100


if __name__ == "__main__":
    test()
    main()
