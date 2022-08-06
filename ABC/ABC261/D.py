def solve(n, m, x_list, cy_list):
    dp = [[-1] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    for i in range(n):
        dp[i + 1][0] = max(dp[i])
        for j in range(n):
            if dp[i][j] >= 0:
                dp[i + 1][j + 1] = dp[i][j] + x_list[i]
        for c, y in cy_list:
            if dp[i + 1][c] >= 0:
                dp[i + 1][c] += y
    # print(dp)
    return max(dp[-1])


def main():
    n, m = map(int, input().split())
    x_list = list(map(int, input().split()))
    cy_list = [tuple(map(int, input().split())) for _ in range(m)]
    res = solve(n, m, x_list, cy_list)
    print(res)


def test():
    assert solve(6, 3, [2, 7, 1, 8, 2, 8], [(2, 10), (3, 1), (5, 5)]) == 48
    assert solve(3, 2, [1000000000, 1000000000, 1000000000], [(1, 1000000000), (3, 1000000000)]) == 5000000000


def test_large():
    print(solve(5000, 5000, list(range(100000, 105000)), [(i, i * i) for i in range(1, 5001)]))


if __name__ == "__main__":
    test()
    # test_large()
    main()
