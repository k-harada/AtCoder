MOD = 998244353


def solve(n, a, b):
    c = 0
    d = 0
    ten = 1
    for i in range(n):
        a_i, b_i = int(a[n - 1 - i]), int(b[n - 1 - i])
        c_i, d_i = min(a_i, b_i), max(a_i, b_i)
        c += c_i * ten
        d += d_i * ten
        ten *= 10
        ten %= MOD

    return ((c % MOD) * (d % MOD)) % MOD


def main():
    n = int(input())
    a = input()
    b = input()
    res = solve(n, a, b)
    print(res)


def test():
    assert solve(2, "13", "22") == 276
    assert solve(8, "20220122", "21002300") == 54558365


if __name__ == "__main__":
    test()
    main()
