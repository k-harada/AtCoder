MOD = 998244353


def solve(n, p):
    if n == 1:
        return 1
    inv100 = pow(100, MOD - 2, MOD)
    p100 = (p * inv100) % MOD
    q100 = ((100 - p) * inv100) % MOD
    e_list = [0] * (n + 1)
    e_list[1] = 1
    for i in range(2, n + 1):
        e_list[i] = 1 + e_list[i - 2] * p100 + e_list[i - 1] * q100
        e_list[i] %= MOD
    return e_list[n]


def main():
    n, p = map(int, input().split())
    res = solve(n, p)
    print(res)


def test():
    assert solve(3, 10) == 229596204
    assert solve(5, 100) == 3
    assert solve(280, 59) == 567484387


if __name__ == "__main__":
    test()
    main()
