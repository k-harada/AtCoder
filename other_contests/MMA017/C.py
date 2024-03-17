MOD = 998244353


def solve(n, a_list):
    # k段目にm回目のジャンプで到達する方法 = (k - 1)C(m - 1)
    # そのあとの方法 = 2 ** (n - k - 1)
    # k段目が起因の得点の合計 = a_k * sum_{m = 1}^{k} m * (k - 1)C(m - 1)
    # = a_k * (2 ** (k - 1) + sum_{m = 1}^{k} (m - 1) * (k - 1)C(m - 1))
    # = a_k * (2 ** (k - 1) + (k - 1) * 2 ** (k - 2))
    if n == 1:
        return a_list[0]
    res = 0
    pow2_list = [1]
    for _ in range(n):
        pow2_list.append((pow2_list[-1] * 2) % MOD)
    for i in range(1, n + 1):
        if 2 <= i < n:
            res += a_list[i - 1] * ((pow2_list[i - 1] + (i - 1) * pow2_list[i - 2]) % MOD) * pow2_list[n - i - 1]
        elif i == 1:
            res += a_list[i - 1] * ((pow2_list[i - 1] + (i - 1)) * pow2_list[n - i - 1] % MOD)
        elif i == n:
            res += a_list[i - 1] * ((pow2_list[i - 1] + (i - 1) * pow2_list[i - 2]) % MOD)
        res %= MOD
    # print(res)
    return res


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(3, [5, 7, 8]) == 95
    assert solve(7, [
        376873723, 252623151, 856139513, 29843394, 373100489, 753241875, 92750716
    ]) == 686211551


if __name__ == "__main__":
    test()
    main()
