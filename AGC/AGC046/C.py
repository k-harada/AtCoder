MOD = 998244353


def solve(s, k):
    one_count = []
    ones = 0
    for st in s:
        if st == "1":
            ones += 1
        else:
            one_count.append(ones)
            ones = 0
    one_count.append(ones)
    ss = sum(one_count)
    # print(ss)
    m = len(one_count)
    dp = [[[0] * (ss + 1) for _ in range(ss + 1)] for __ in range(m + 1)]
    dp[0][0][0] = 1
    for i in range(m):
        c = one_count[i]
        for j in range(ss + 1):
            for p in range(ss + 1):
                dp[i][j][p] %= MOD
                for q in range(ss + 1 - max(j, p)):
                    dp[i + 1][j + q][p + q] += dp[i][j][p]
                for q in range(-c, 0):
                    if j + q >= 0:
                        dp[i + 1][j + q][p] += dp[i][j][p]

    # print(dp)
    res = sum([dp[m][0][p] for p in range(min(k + 1, ss + 1))])
    # print(res)
    return res % MOD


def main():
    s, k_ = input().split()
    k = int(k_)
    res = solve(s, k)
    print(res)


def test():
    assert solve("0101", 1) == 4
    assert solve("01100110", 2) == 14
    assert solve("1101010010101101110111100011011111011000111101110101010010101010101", 20) == 113434815


if __name__ == "__main__":
    test()
    main()
