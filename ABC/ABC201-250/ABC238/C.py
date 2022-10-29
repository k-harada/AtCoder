MOD = 998244353


def solve(n):
    res = 0
    # 桁数を求める
    length = 0
    for i in range(19):
        if n < 10 ** i:
            length = i
            break
    half = pow(2, MOD - 2, MOD)
    # lengthより短いものを全部足す
    for i in range(1, length):
        c = pow(10, i, MOD) - pow(10, i - 1, MOD)
        c %= MOD
        res += (c * (c + 1) % MOD) * half
        res %= MOD
    # nと同じ桁のものを足す
    c = n - pow(10, length - 1, MOD) + 1
    c %= MOD
    res += (c * (c + 1) % MOD) * half
    res %= MOD
    return res


def main():
    n = int(input())
    res = solve(n)
    print(res)


def test():
    assert solve(16) == 73
    assert solve(238) == 13870
    assert solve(999999999999999999) == 762062362


if __name__ == "__main__":
    test()
    main()
