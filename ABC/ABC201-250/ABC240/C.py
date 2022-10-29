def solve(n, x, ab_list):
    dp = [[0] * 10001 for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(n):
        a, b = ab_list[i]
        for j in range(10001):
            if dp[i][j] == 1:
                dp[i + 1][j + a] = 1
                dp[i + 1][j + b] = 1
    if dp[n][x] == 1:
        return "Yes"
    else:
        return "No"


def main():
    n, x = map(int, input().split())
    ab_list = [tuple(map(int, input().split())) for _ in range(n)]
    res = solve(n, x, ab_list)
    print(res)


def test():
    assert solve(2, 10, [(3, 6), (4, 5)]) == "Yes"
    assert solve(2, 10, [(10, 100), (10, 100)]) == "No"
    assert solve(4, 12, [(1, 8), (5, 7), (3, 4), (2, 6)]) == "Yes"


if __name__ == "__main__":
    # test()
    main()
