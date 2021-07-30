MOD = 10 ** 9 + 7


def solve(n):
    res = [n] * n
    factorial = [1] * (n + 1)
    factorial_inv = [1] * (n + 1)
    for i in range(1, n + 1):
        factorial[i] = (factorial[i - 1] * i) % MOD

    factorial_inv[-1] = pow(factorial[-1], MOD - 2, MOD)

    for i in range(n, 0, -1):
        factorial_inv[i - 1] = (factorial_inv[i] * i) % MOD

    res[0] = pow(2, n, MOD) - 1
    for i in range(1, n):
        p = n - i
        q = 2
        while p >= q:
            res[i] += ((factorial[p] * factorial_inv[q]) % MOD) * factorial_inv[p - q] % MOD
            p -= i
            q += 1
        res[i] %= MOD
    return res


def main():
    n = int(input())
    res = solve(n)
    for r in res:
        print(r)


def test():
    assert solve(1) == [1]
    assert solve(2) == [3, 2]
    assert solve(3) == [7, 4, 3]


if __name__ == "__main__":
    test()
    main()
