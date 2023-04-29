from collections import defaultdict


MOD = 998244353


def solve(n):
    cnt_2 = 0
    cnt_3 = 0
    cnt_5 = 0
    x = n
    while x % 2 == 0:
        cnt_2 += 1
        x //= 2
    while x % 3 == 0:
        cnt_3 += 1
        x //= 3
    while x % 5 == 0:
        cnt_5 += 1
        x //= 5
    if x != 1:
        return 0

    factors = []
    for i in range(cnt_2 + 1):
        y2 = 2 ** i
        for j in range(cnt_3 + 1):
            y3 = y2 * (3 ** j)
            for k in range(cnt_5 + 1):
                y5 = y3 * (5 ** k)
                factors.append(y5)
    # print(factors)
    # print(len(factors))
    # print(cnt_2, cnt_3, cnt_5)
    index_dict = defaultdict(int)
    for j, x in enumerate(factors):
        index_dict[x] = j
    m = cnt_2 + cnt_3 + cnt_5
    dp = [[0] * len(factors) for _ in range(m + 1)]
    dp[0][0] = 1
    for i in range(m):
        for j, x in enumerate(factors):
            for r in range(2, 7):
                if index_dict[r * x] == 0:
                    continue
                dp[i + 1][index_dict[r * x]] += dp[i][j]
        for j in range(len(factors)):
            dp[i + 1][j] %= MOD
    # print(dp)
    res = 0
    five = 1
    five_inv = pow(5, MOD - 2, MOD)
    for i in range(m + 1):
        res += dp[i][-1] * five
        res %= MOD
        five *= five_inv
        five %= MOD

    return res


def main():
    n = int(input())
    res = solve(n)
    print(res)


def test():
    assert solve(6) == 239578645
    assert solve(7) == 0
    assert solve(300) == 183676961
    assert solve(979552051200000000) == 812376310


if __name__ == "__main__":
    test()
    main()
