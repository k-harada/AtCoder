MOD = 998244353


def solve(n, k, a_list):
    factorial = [1] * (n + k + 1)
    factorial_inv = [1] * (n + k + 1)
    for i in range(1, n + k + 1):
        factorial[i] = (factorial[i - 1] * i) % MOD

    factorial_inv[-1] = pow(factorial[-1], MOD - 2, MOD)

    for i in range(n + k, 0, -1):
        factorial_inv[i - 1] = (factorial_inv[i] * i) % MOD

    res = 0
    a_unique = list(sorted(list(set(a_list))))
    j = 0
    a = a_unique[0]
    m = len(a_unique)
    c = k
    for i in range(n + k):
        if i == a:
            j += 1
            if j < m:
                a = a_unique[j]
            else:
                a = 1000000000
            d = 1
            if c == 0:
                break
        else:
            c -= 1
            d = 0
        if c < 0:
            break
        res += (factorial[c + i - d] * ((factorial_inv[c - d] * factorial_inv[i]) % MOD)) % MOD
        res %= MOD
        # print(c, i, res)
    # print(res)
    return res


def main():
    n, k = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, k, a_list)
    print(res)


def test():
    assert solve(3, 1, [0, 1, 3]) == 3
    assert solve(2, 1, [0, 0]) == 2
    assert solve(5, 10, [3, 1, 4, 1, 5]) == 7109


if __name__ == "__main__":
    test()
    main()
