def solve(n, m, a_list):
    # dp
    dp_on = [[n + 1] * (m + 1) for _ in range(n + 1)]
    dp_off = [[n + 1] * (m + 1) for _ in range(n + 1)]
    dp_on[0][0] = 0

    for i in range(n):
        # on
        a = a_list[i]
        for j in range(m + 1 - a):
            dp_on[i + 1][j + a] = min(dp_on[i + 1][j + a], dp_on[i][j])
            dp_on[i + 1][j + a] = min(dp_on[i + 1][j + a], dp_off[i][j])
        # off
        for j in range(m + 1):
            dp_off[i + 1][j] = min(dp_off[i + 1][j], dp_on[i][j] + 1)
            dp_off[i + 1][j] = min(dp_off[i + 1][j], dp_off[i][j])
    res = [n + 1] * m
    for i in range(m):
        res[i] = min(res[i], dp_on[n][i + 1])
        res[i] = min(res[i], dp_off[n][i + 1])
        if res[i] > n:
            res[i] = -1
    return res


def main():
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, m, a_list)
    for r in res:
        print(r)


def test():
    assert solve(4, 5, [1, 2, 3, 4]) == [1, 2, 1, 1, 1]
    assert solve(1, 5, [3]) == [-1, -1, 0, -1, -1]
    assert solve(12, 20, [2, 5, 6, 5, 2, 1, 7, 9, 7, 2, 5, 5]) == [
        2, 1, 2, 2, 1, 2, 1, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1, 1, 1, 1,
    ]


def test_large():
    print(solve(3000, 3000, [1] * 3000))


if __name__ == "__main__":
    test()
    # test_large()
    main()
