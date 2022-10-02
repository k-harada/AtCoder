MOD = 998244353


def solve(n, m, k, b_list):
    # ある回数やるとひたすら左にずれていくだけ
    # 終わった時点で影響範囲内の一番大きいM-1個が並んでるはず
    # 最終のM - 1個
    last_l = (k - 1 + 1) % n
    last_r = (last_l - 1 + m - 1) % n
    if k - 1 + m - 1 <= n - 1:
        last_a = b_list[:last_l]
        last_b = b_list[last_l:(last_r + 1)]
    else:
        if last_l <= last_r:
            last_b = b_list[last_l:(last_r + 1)]
            last_a = b_list[(last_r + 1):] + b_list[:last_l]
        else:
            last_b = b_list[last_l:] + b_list[:(last_r + 1)]
            last_a = b_list[(last_r + 1):last_l]
    # そもそも綺麗に並んでいないとおかしい
    target_s = list(sorted(b_list[:min(k - 1 + m - 1, n - 1) + 1]))
    # print(last_a)
    # print(last_b)
    if last_b != target_s[-(m - 1):]:
        return 0
    # 過剰な操作がある場合にlast_aを復元
    r = len(last_a)
    if k - 1 + m - 1 >= n - 1:
        d = k - 1 + m - 1 - (n - 1)
        d %= r
        last_a = last_a[-d:] + last_a[:-d]
    # print(last_a)
    # print(last_b)
    v = r
    i = 0
    j = 1
    while j < r:
        # print(i, j)
        if last_a[i] > last_a[j]:
            v -= 1
            j += 1
        else:
            i, j = j, j + 1
    res = pow(m, v, MOD)
    # print(res, v)
    for i in range(1, m):
        res *= i
        res %= MOD
    # print(res)
    return res


def main():
    n, m, k = map(int, input().split())
    b_list = list(map(int, input().split()))
    res = solve(n, m, k, b_list)
    print(res)


def test():
    assert solve(6, 3, 5, [6, 4, 2, 3, 1, 5]) == 18
    assert solve(6, 3, 5, [6, 5, 4, 3, 2, 1]) == 0
    assert solve(20, 20, 149, [13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 401576539


if __name__ == "__main__":
    test()
    main()
