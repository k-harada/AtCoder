MOD = 998244353


def solve(n, m):
    d = max(2 * n + 3, n + m // 3) + 1
    factorial = [1] * d
    factorial_inv = [1] * d
    for i in range(1, d):
        factorial[i] = (factorial[i - 1] * i) % MOD

    factorial_inv[-1] = pow(factorial[-1], MOD - 2, MOD)

    for i in range(d - 1, 0, -1):
        factorial_inv[i - 1] = (factorial_inv[i] * i) % MOD

    def ncr(a, b):
        if a <= b:
            return 1
        return (((factorial[a] * factorial_inv[a - b]) % MOD) * factorial_inv[b]) % MOD

    cnt = [0] * (2 * n + 3)

    for i in range(n):
        # (n - 1)箇所に1 or 2を挟む問題
        k = (n - 1) + i
        v = ncr(n - 1, i)
        # 両端に0 or 1 or 2を挟む問題
        cnt[k] += v
        cnt[k + 1] += v
        cnt[k + 2] += v
    # print(cnt)
    # n + 1箇所に3を挟む問題
    res = 0
    k = (m - (n - 1)) // 3
    c = ncr(n + k, n)
    for i in range(n - 1, 2 * n + 3):
        if i > m:
            break
        k = (m - i) // 3
        if (m - i) % 3 == 2:
            c = ncr(n + k, n)
        res += c * cnt[i]
        res %= MOD
    # print(res)
    return res


def main():
    n, m = map(int, input().split())
    res = solve(n, m)
    print(res)


def test():
    assert solve(3, 4) == 8
    # assert solve(276, 10000000) == 909213205


if __name__ == "__main__":
    test()
    main()
