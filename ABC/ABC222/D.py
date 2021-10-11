MOD = 998244353


def solve(n, a_list, b_list):
    dp = [[0] * 3001 for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(n):
        a = a_list[i]
        b = b_list[i]
        s = 0
        for j in range(b + 1):
            s += dp[i][j]
            s %= MOD
            if j >= a:
                dp[i + 1][j] = s
    return sum(dp[-1]) % MOD


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    res = solve(n, a_list, b_list)
    print(res)


def test():
    assert solve(2, [1, 1], [2, 3]) == 5
    assert solve(3, [2, 2, 2], [2, 2, 2]) == 1
    assert solve(10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]) == 978222082


if __name__ == "__main__":
    test()
    main()
