MOD = 998244353


def solve(n, m, k):
    # corner
    if n == 1 and m == 1:
        return k
    elif min(n, m) == 1:
        return pow(k, max(n, m), MOD)
    # normal
    # d = max(min)
    res = 0
    for d in range(1, k + 1):
        a = pow(d, n, MOD) - pow(d - 1, n, MOD)
        b = pow(k - d + 1, m, MOD)
        res += a * b % MOD
    # print(res % MOD)
    return res % MOD


def main():
    n, m, k = map(int, input().split())
    res = solve(n, m, k)
    print(res)


def test():
    assert solve(2, 2, 2) == 7
    assert solve(1, 1, 100) == 100
    assert solve(31415, 92653, 58979) == 469486242


if __name__ == "__main__":
    test()
    main()
