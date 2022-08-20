MOD = 998244353


def solve(n, p_list):

    right_invader_list = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i - 1, -1, -1):
            # print(i, j, p_list[j] > p_list[i])
            if p_list[j] > p_list[i]:
                break
            else:
                right_invader_list[j].append(p_list[i])
    # print(right_invader_list)
    # dp
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    # dp[i + 1][j] i番目の数字がjのパターン
    for i in range(n):
        # initial
        if i == 0:
            dp[i + 1][p_list[i]] += dp[0][0]
        # from left
        for j in p_list[:i + 1]:
            # p_list[i] survive
            dp[i + 1][p_list[i]] += dp[i][j]
            # invaded from left
            if j > p_list[i]:
                dp[i + 1][j] += dp[i][j]
        # already invaded from right
        for j in right_invader_list[i]:
            dp[i + 1][j] += dp[i][j]
        # newly invaded from right
        s = dp[i + 1][p_list[i]]
        for j in sorted(right_invader_list[i]):
            dp[i + 1][j] += s
            s += dp[i][j]
        for j in range(n + 1):
            dp[i + 1][j] %= MOD
    print(dp)
    print(sum(dp[-1]))
    return sum(dp[-1]) % MOD


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
