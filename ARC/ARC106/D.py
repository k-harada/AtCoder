MOD = 998244353


def solve(n, k, a_list):

    # factorial
    factorial = [1] * (k + 1)
    for i in range(k):
        factorial[i + 1] = (factorial[i] * (i + 1)) % MOD
    # factorial inverse
    factorial_inv = [1] * (k + 1)
    factorial_inv[-1] = pow(factorial[-1], MOD - 2, MOD)
    for i in range(k - 1, -1, -1):
        factorial_inv[i] = (factorial_inv[i + 1] * (i + 1)) % MOD
    # print(factorial, factorial_inv)

    # a^p
    powers_list = [0] * (k + 1)
    powers_list[0] = n
    for i in range(n):
        r = 1
        for p in range(k):
            r *= a_list[i]
            r %= MOD
            powers_list[p + 1] += r
    for i in range(k + 1):
        powers_list[i] %= MOD

    res_list = []
    for x in range(1, k + 1):
        res = 0
        for i in range(x + 1):
            res += ((factorial_inv[i] * powers_list[i]) % MOD) * ((factorial_inv[x - i] * powers_list[x - i]) % MOD)
            res %= MOD
        res *= factorial[x]
        res %= MOD
        res -= pow(2, x, MOD) * powers_list[x]
        res %= MOD
        res *= factorial_inv[2]
        res %= MOD
        res_list.append(res)
    # print(res_list)
    return res_list


def main():
    n, k = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, k, a_list)
    for r in res:
        print(r)


def test():
    assert solve(3, 3, [1, 2, 3]) == [12, 50, 216]
    assert solve(10, 10, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [90, 180, 360, 720, 1440, 2880, 5760, 11520, 23040, 46080]
    assert solve(2, 5, [1234, 5678]) == [6912, 47775744, 805306038, 64822328, 838460992]


if __name__ == "__main__":
    test()
    main()
