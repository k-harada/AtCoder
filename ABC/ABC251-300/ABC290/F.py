MOD = 998244353


def solve(t, case_list):
    n = 2 * max(case_list)
    factorial = [1] * (n + 1)
    factorial_inv = [1] * (n + 1)
    for i in range(1, n + 1):
        factorial[i] = (factorial[i - 1] * i) % MOD

    factorial_inv[-1] = pow(factorial[-1], MOD - 2, MOD)
    for i in range(n, 0, -1):
        factorial_inv[i - 1] = (factorial_inv[i] * i) % MOD

    res_list = []
    for k in case_list:
        if k >= 3:
            res = factorial[2 * k - 3] * factorial_inv[k - 1] * factorial_inv[k - 2]
            res %= MOD
            res += k * factorial[2 * k - 4] * factorial_inv[k - 1] * factorial_inv[k - 3]
            res %= MOD
            res_list.append(res)
        else:
            res_list.append(1)
    # print(res_list)
    return res_list


def main():
    t = int(input())
    case_list = [int(input()) for _ in range(t)]
    res = solve(t, case_list)
    for r in res:
        print(r)


def test():
    assert solve(10, [2, 3, 5, 8, 13, 21, 34, 55, 89, 144]) == [
        1, 6, 110, 8052, 9758476, 421903645, 377386885, 881422708, 120024839, 351256142
    ]


if __name__ == "__main__":
    test()
    main()
