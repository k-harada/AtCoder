MOD = 10 ** 9 + 7


def solve(n, h_list):

    dp = [[0] * n for _ in range(n)]
    dp[0][0] = 1
    for i in range(n - 1):
        if h_list[i + 1] < h_list[i]:
            r = 0
            for k in range(i + 2):
                dp[i + 1][k] = r
                r += dp[i][k]
                r %= MOD
        elif h_list[i + 1] == h_list[i]:
            r = sum(dp[i]) % MOD
            for k in range(i + 2):
                dp[i + 1][k] = r
        else:
            r = 0
            for k in range(i + 1, -1, -1):
                r += dp[i][k]
                r %= MOD
                dp[i + 1][k] = r

    # print(dp)
    return sum(dp[-1]) % MOD


def main():
    n = int(input())
    h_list = list(map(int, input().split()))
    res = solve(n, h_list)
    print(res)


def test():
    assert solve(3, [4, 2, 4]) == 2
    assert solve(3, [100, 100, 100]) == 6
    assert solve(15, [
        804289384, 846930887, 681692778, 714636916, 957747794, 424238336, 719885387, 649760493, 596516650, 189641422,
        25202363, 350490028, 783368691, 102520060, 44897764]) == 54537651


if __name__ == "__main__":
    test()
    main()
