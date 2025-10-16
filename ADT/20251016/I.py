def solve(n, m, d):

    # dealerの確率計算
    dealer = [0] * (n + 1)
    dealer_bust = 0
    dealer[0] = 1
    s = 0
    for i in range(1, n + 1):
        if i - 1 < m:
            s += dealer[i - 1] / d
        if 0 <= i - (d + 1) < m:
            s -= dealer[i - (d + 1)] / d
        dealer[i] += s
    for i in range(m):
        c = max(0, i + d - n)
        dealer_bust += c * dealer[i] / d
    for i in range(m):
        dealer[i] = 0
    # print(dealer[:(n + 1)])
    # print(dealer_bust)
    # print(sum(dealer[:(n + 1)]) + dealer_bust)

    # playerのアクション決め
    win_rate_list = [0] * (n + 1)
    win_rate_list[0] = dealer_bust
    for i in range(1, n + 1):
        win_rate_list[i] = win_rate_list[i - 1] + dealer[i - 1]
    # print(win_rate_list)

    dp = [0] * (n + 2)
    cum = 0
    for i in range(n, -1, -1):
        dp[i] = max(win_rate_list[i], cum)
        cum += dp[i] / d
        if i + d < n + 2:
            cum -= dp[i + d] / d
    res = dp[0]
    # print(res)
    return res


def main():
    n, m, d = map(int, input().split())
    res = solve(n, m, d)
    print(res)


def test():
    assert abs(solve(3, 2, 2) - 0.46875) < 0.000000001
    assert abs(solve(200000, 200000, 200000) - 0.999986408692793) < 0.000000001


if __name__ == "__main__":
    test()
    main()
