MOD = 998244353


def solve(n):
    dp = [0] * (n + 2)
    n_inv = pow(n, MOD - 2, MOD)
    for i in range(n - 1, -1, -1):
        # dp[i]
        # (n - i) ** 2 / (n ** 2) * (1 + dp[i]) 両方失敗
        # (i / n) * ((n - i - 1) / n) * (dp[i + 1]) 自分は成功相手は失敗
        # ((n - i) / n) * (i / n) * (1 + dp[i + 1]) 自分は失敗相手は成功
        # (i / n) * ((i - 1) / n) * (1 + dp[i + 2]) 自分は成功相手は成功
        p1 = (i * i) % MOD
        p1 *= (n_inv * n_inv) % MOD
        p1 %= MOD
        p2 = ((n - i) * (i + 1) * dp[i + 1]) % MOD
        p2 *= (n_inv * n_inv) % MOD
        p2 %= MOD
        p3 = (i * (n - i) * (1 + dp[i + 1])) % MOD
        p3 *= (n_inv * n_inv) % MOD
        p3 %= MOD
        p4 = ((n - i) * (n - i - 1) * dp[i + 2]) % MOD
        p4 *= (n_inv * n_inv) % MOD
        p4 %= MOD
        if i > 0:
            q = (p1 + p2 + p3 + p4) % MOD
            r = (n * n - (i * i)) % MOD
            r *= (n_inv * n_inv) % MOD
            dp[i] = (q * pow(r, MOD - 2, MOD)) % MOD
        else:
            # print(p2, p4)
            dp[i] = (p2 + p4) % MOD
    # print(dp)
    return str(dp[0]) + " " + str(dp[1])


def main():
    n = int(input())
    res = solve(n)
    print(res)


def test():
    assert solve(1) == "0 0"
    assert solve(2) == "332748118 665496236"
    assert solve(3) == "174692763 324429416"


if __name__ == "__main__":
    test()
    main()
