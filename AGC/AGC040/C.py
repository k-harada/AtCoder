LARGE = 998244353


def solve(n):
    r = 0
    mck = 1
    factorial_n = 1
    factorial_inv = [0] * (n + 1)
    factorial_inv[0] = 1
    for i in range(1, n + 1):
        factorial_n *= i
        factorial_n %= LARGE
    factorial_inv[-1] = pow(factorial_n, LARGE - 2, LARGE)
    for i in range(n):
        factorial_inv[n - i - 1] = (factorial_inv[n - i] * (n - i)) % LARGE
    pow_2 = 1
    for k in range(n // 2):
        r += factorial_n * factorial_inv[n - k] * factorial_inv[k] * pow_2
        r %= LARGE
        pow_2 *= 2
        pow_2 %= LARGE
    res = (pow(3, n, LARGE) - (2 * r)) % LARGE
    return res


def main():
    n = int(input())
    res = solve(n)
    print(res)


def test():
    assert solve(2) == 7
    assert solve(10) == 50007
    # assert solve(1000000) == 210055358


if __name__ == "__main__":
    test()
    main()
