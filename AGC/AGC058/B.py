MOD = 998244353


def solve(n, p_list):
    left_limit = [0] * n
    right_limit = [n + 1] * n
    for i in range(n):
        for j in range(i - 1, -1, -1):
            if p_list[j] > p_list[i]:
                left_limit[i] = j + 1
                break
        for j in range(i + 1, n):
            if p_list[j] > p_list[i]:
                right_limit[i] = j + 1
                break
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(n):
        right = right_limit[i] - 1
        left = left_limit[i]
        s = sum(dp[i][left:right + 1])
        # print(left, right, s)
        for j in range(right, left - 1, -1):
            s -= dp[i][j]
            dp[i + 1][j] += s
        for j in range(n + 1):
            dp[i + 1][j] += dp[i][j]
            dp[i + 1][j] %= MOD

    # print(dp)

    return dp[-1][-1]


def main():
    n = int(input())
    p_list = list(map(int, input().split()))
    res = solve(n, p_list)
    print(res)


def test():
    assert solve(3, [1, 3, 2]) == 4
    assert solve(4, [2, 1, 3, 4]) == 11
    assert solve(10, [4, 9, 6, 3, 8, 10, 1, 2, 7, 5]) == 855


if __name__ == "__main__":
    test()
    main()
