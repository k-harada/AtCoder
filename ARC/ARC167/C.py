MOD = 998244353



def solve(n, k, a_list):

    size = n
    factorial = [1] * (size + 1)
    factorial_inv = [1] * (size + 1)
    for i in range(1, size + 1):
        factorial[i] = (factorial[i - 1] * i) % MOD

    factorial_inv[-1] = pow(factorial[-1], MOD - 2, MOD)

    for i in range(size, 0, -1):
        factorial_inv[i - 1] = (factorial_inv[i] * i) % MOD

    a_list_s = list(sorted(a_list, reverse=True))
    count_place = [0] * n
    for i in range(n):
        right = min(n - 1, i + k)
        left = max(0, i - k)
        count_place[i] = right - left
    print(count_place)

    dp = [[0] * n for _ in range(n)]
    # dp[i][j]: j番目の場所に入れたときに大きい方からi番の値を要求される場合の数
    for i in range(n):
        # 自分の値が使われるかどうか
        for j in range(n):
            if i >= count_place[j] - 1:
                dp[i][j] = 1 * (
                        (factorial[i] * factorial_inv[i - count_place[j] + 1] * count_place[j]) % MOD  # i以下で埋める
                ) * (
                    factorial[n - count_place[j] - 1]  # 残りの場所を埋める
                ) % MOD
    print(dp)
    # 全パターン
    d_all = factorial[n - 1]
    print(d_all)
    dc = [0] * n
    ds = [0] * n
    res = 0
    for i, a in enumerate(a_list_s):
        if i == n - 1:
            break
        print(i, dc, ds)
        for j in range(n):
            # 自分の値が使えるパターン
            res += a * (d_all - dc[j])
            # 自分の値が使えないパターン
            res += ds[j]
            print(a, j, a * (d_all - dc[j]), ds[j])
            dc[j] += dp[i][j]
            ds[j] += a * dp[i][j]
            dc[j] %= MOD
            ds[j] %= MOD
        res %= MOD
    print(res)
    return res


def main():
    n, k = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, k, a_list)
    print(res)


def test():
    assert solve(5, 2, [1, 1, 1, 1, 1]) == 480
    assert solve(3, 1, [1, 2, 3]) == 32
    assert solve(3, 2, [1, 2, 3]) == 30
    assert solve(4, 1, [1, 2, 3, 4]) == 240
    assert solve(4, 2, [1, 2, 3, 4]) == 30
    assert solve(5, 2, [3, 4, 5, 2, 1]) == 1740
    assert solve(2, 1, [167, 924]) == 1848
    assert solve(12, 9, [
        22847, 98332, 854, 68844, 81080, 46058, 40949, 62493, 76561, 52907, 88628, 99740
    ]) == 660459584


if __name__ == "__main__":
    test()
    main()
