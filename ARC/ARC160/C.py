MOD = 998244353


def solve(n, a_list):
    mm = min(a_list)
    m = max(a_list) - mm + 1
    count = [0] * m
    for a in a_list:
        count[a - mm] += 1
    dp = [[1]]
    for i in range(10 ** 9):
        c = len(dp[i]) - 1
        if i < m:
            c += count[i]
        c //= 2
        if i > m and c == 0:
            break
        dp.append([0] * (c + 1))
    count = count + [0] * (len(dp) - len(count))
    for i in range(len(dp) - 1):
        t = len(dp[i + 1]) - 1
        v = 0
        for j in range(len(dp[i]) - 1, -1, -1):
            v += dp[i][j]
            v %= MOD
            q = j + count[i]
            if q % 2 == 0:
                dp[i + 1][t] = v
                t -= 1
        for j in range(t + 1):
            if dp[i + 1][j] == 0:
                dp[i + 1][j] = v

    # print(dp)

    return sum(dp[-1]) % MOD


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(4, [1, 1, 2, 4]) == 3
    assert solve(5, [1, 2, 3, 4, 5]) == 1
    assert solve(13, [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9]) == 66


def test_large():
    print(solve(200000, [200000] * 200000))


if __name__ == "__main__":
    test()
    # test_large()
    main()
