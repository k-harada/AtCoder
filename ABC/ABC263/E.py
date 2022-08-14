MOD = 998244353


def solve(n, a_list):
    exp = [0] * n
    cum_sum_rev = [0] * (n + 1)
    mod_inv = [1, 1]
    for i in range(2, n):
        mod_inv.append(pow(i, MOD - 2, MOD))

    for i in range(n - 2, -1, -1):
        a = a_list[i]
        exp[i] = 1 + mod_inv[a] + ((cum_sum_rev[i + 1] - cum_sum_rev[i + 1 + a]) * mod_inv[a] % MOD)
        exp[i] %= MOD
        cum_sum_rev[i] = (cum_sum_rev[i + 1] + exp[i]) % MOD
    return exp[0]


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(3, [1, 1]) == 4
    assert solve(5, [3, 1, 2, 1]) == 332748122


if __name__ == "__main__":
    test()
    main()
