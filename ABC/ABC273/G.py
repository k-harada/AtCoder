MOD = 998244353


def solve(n, r_list, c_list):
    # そもそも矛盾
    if sum(r_list) != sum(c_list):
        return 0
    # 0の行と列は最初からなかったことにする
    r1 = 0
    r2 = 0
    c1 = 0
    c2 = 0
    for r in r_list:
        if r == 1:
            r1 += 1
        elif r == 2:
            r2 += 1
    for c in c_list:
        if c == 1:
            c1 += 1
        elif c == 2:
            c2 += 1

    factorial = [1] * (2 * n + 1)
    factorial_inv = [1] * (2 * n + 1)
    for i in range(1, 2 * n + 1):
        factorial[i] = (factorial[i - 1] * i) % MOD

    factorial_inv[-1] = pow(factorial[-1], MOD - 2, MOD)

    for i in range(2 * n, 0, -1):
        factorial_inv[i - 1] = (factorial_inv[i] * i) % MOD

    def conv(n_, r_):
        return ((factorial[n_] * factorial_inv[n_ - r_]) % MOD * factorial_inv[r_]) % MOD

    # 行のアサインはもう決まってる
    # 22221111111111に並べ替える
    # ただし何回か数えるやつがいるのでそれに対処
    m = sum(r_list)
    res = 0
    # 大きい方から出す
    r2, c2 = max(r2, c2), min(r2, c2)
    # 何個被ったか
    res_dup_list = [0] * (c2 + 1)
    half = pow(2, MOD - 2, MOD)
    for k in range(c2 + 1):
        res_dup_list[k] = (((conv(r2, k) * conv(c2, k)) % MOD) * ((factorial[k] * factorial[m - 2 * k]) % MOD)) % MOD
        res_dup_list[k] *= pow(half, r2 - k, MOD)
        res_dup_list[k] %= MOD
    # print(res_dup_list)
    # 重複の排除
    for k in range(c2 - 1, -1, -1):
        for j in range(k + 1, c2 + 1):
            res_dup_list[k] -= conv(j, k) * res_dup_list[j]
            res_dup_list[k] %= MOD
    # 違うものが入ってるペアの同一視
    for k in range(c2 + 1):
        res_dup_list[k] *= pow(half, c2 - k, MOD)
        res_dup_list[k] %= MOD
    res = sum(res_dup_list) % MOD
    # print(res_dup_list)
    # print(res)

    return res


def main():
    n = int(input())
    r_list = list(map(int, input().split()))
    c_list = list(map(int, input().split()))
    res = solve(n, r_list, c_list)
    print(res)


def test():
    assert solve(3, [1, 1, 1], [0, 1, 2]) == 3
    assert solve(3, [1, 1, 1], [2, 2, 2]) == 0
    assert solve(3, [2, 2, 0], [2, 1, 1]) == 4
    assert solve(18, [
        2, 0, 1, 2, 0, 1, 1, 2, 1, 1, 2, 0, 1, 2, 2, 1, 0, 0
    ], [
        1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 0, 2, 2
    ]) == 968235177


if __name__ == "__main__":
    test()
    main()
