from subprocess import Popen, PIPE

MOD = 998244353


# from nagiss-san's AC
def fast_prime_factorization(n):
    # 素因数分解（ロー法）  O(n^(1/4) polylog(n))
    return list(map(int, Popen(["factor", str(n)], stdout=PIPE).communicate()[0].split()[1:]))


def prime_factorization(n):
    res = []
    x = n
    for i in range(2, int(n ** 0.5) + 1):
        while x % i == 0:
            x //= i
            res.append(i)
    if x != 1:
        res.append(x)
    return res


def solve(n, m, a_list):
    if m == 1:
        c = a_list.count(1)
        return (pow(2, c, MOD) - 1) % MOD

    r = prime_factorization(m)
    factor_list = []
    for p in set(r):
        factor_list.append(p ** r.count(p))
    # print(factor_list)
    k = len(set(r))
    count = [0] * (2 ** k)
    for a in a_list:
        if m % a != 0:
            continue
        x = 0
        for i, v in enumerate(factor_list):
            if a % v == 0:
                x += 2 ** i
        count[x] += 1
    # print(count)
    dp = [[0] * (2 ** k) for _ in range(2 ** k)]
    dp[0][0] = pow(2, count[0], MOD)
    for i in range(1, 2 ** k):
        w = pow(2, count[i], MOD) - 1
        for j in range(2 ** k):
            dp[i][j] = dp[i - 1][j]
        for j in range(2 ** k):
            dp[i][i | j] += (dp[i - 1][j] * w) % MOD
            dp[i][i | j] %= MOD
        # print(dp[i])
    # print(dp[-1][-1])
    return dp[-1][-1]


def main():
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, m, a_list)
    print(res)


def test():
    assert solve(4, 6, [2, 3, 4, 6]) == 5
    assert solve(5, 349, [1, 1, 1, 1, 349]) == 16
    assert solve(16, 720720, [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16
    ]) == 2688


if __name__ == "__main__":
    test()
    main()
