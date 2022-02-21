MOD = 998244353


def solve(n, x, y, z):
    c = abs(x) + abs(y) + abs(z)
    if c > n:
        return 0
    if (n - c) % 2 == 1:
        return 0
    d = (n - c) // 2

    # 下準備
    factorial = [1] * (n + 1)
    factorial_inv = [1] * (n + 1)
    for i in range(1, n + 1):
        factorial[i] = (factorial[i - 1] * i) % MOD

    factorial_inv[-1] = pow(factorial[-1], MOD - 2, MOD)

    for i in range(n, 0, -1):
        factorial_inv[i - 1] = (factorial_inv[i] * i) % MOD

    # とりあえず全部の無駄をx方向で消費する
    res = 0
    return res


def main():
    n, x, y, z = map(int, input().split())
    res = solve(n, x, y, z)
    print(res)


def test():
    assert solve() == 0
    assert solve() == 0
    assert solve() == 0


if __name__ == "__main__":
    test()
    main()
