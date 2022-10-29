LARGE = 10 ** 9 + 7


def solve(n, a, b):

    pow_ab = [1] * (b + 1)
    for i in range(b):
        pow_ab[i + 1] = pow_ab[i] * (i + 1) % LARGE
    pow_ab_inv = [1] * (b + 1)
    pow_ab_inv[-1] = pow(pow_ab[-1], LARGE - 2, LARGE)
    for i in range(b - 1, 0, -1):
        pow_ab_inv[i] = pow_ab_inv[i + 1] * (i + 1) % LARGE

    res_all = pow(2, n, LARGE) - 1

    res_ab = 1
    for i in range(a):
        res_ab *= (n - i)
        res_ab %= LARGE
    res_all -= res_ab * pow_ab_inv[a]
    for i in range(a, b):
        res_ab *= (n - i)
        res_ab %= LARGE
    res_all -= res_ab * pow_ab_inv[b]
    return res_all % LARGE


def main():
    n, a, b = map(int, input().split())
    res = solve(n, a, b)
    print(res)


def test():
    assert solve(4, 1, 3) == 7
    assert solve(1000000000, 141421, 173205) == 34076506


if __name__ == "__main__":
    test()
    main()
