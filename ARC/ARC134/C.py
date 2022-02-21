MOD = 998244353


def ncr_child(a, b):
    res = 1
    for r in range(a, a - b, -1):
        res *= r
        res %= MOD
    return res


def solve(n, k, a_list):
    if a_list[0] < sum(a_list[1:]) + k:
        return 0
    if k == 1:
        return 1

    ncr_mom = 1
    for i in range(1, k):
        ncr_mom *= i
    ncr_mom = pow(ncr_mom, MOD - 2, MOD)

    res = ncr_child(a_list[0] - k - sum(a_list[1:]) + k - 1, k - 1)
    res *= ncr_mom
    res %= MOD

    for i in range(1, n):
        res *= ncr_child(a_list[i] + k - 1, k - 1)
        res *= ncr_mom
        res %= MOD
    # print(res)
    return res


def main():
    n, k = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, k, a_list)
    print(res)


def test():
    assert solve(2, 2, [3, 1]) == 2
    assert solve(2, 1, [1, 100]) == 0
    assert solve(20, 100, [
        1073813, 90585, 41323, 52293, 62633, 28788, 1925, 56222, 54989, 2772,
        36456, 64841, 26551, 92115, 63191, 3603, 82120, 94450, 71667, 9325
    ]) == 313918676


def test_large():
    print(solve(100000, 200, [998244350] * 100000))


if __name__ == "__main__":
    test()
    # test_large()
    main()
