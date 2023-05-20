MOD = 998244353


def solve(r, g, b, k):
    n = r + g + b
    mod_list = [0] * (n + 1)
    mod_inv_list = [0] * (n + 1)
    mod_list[0] = 1
    for i in range(1, n + 1):
        mod_list[i] = (mod_list[i - 1] * i) % MOD
    mod_inv_list[-1] = pow(mod_list[-1], MOD - 2, MOD)
    for i in range(n - 1, -1, -1):
        mod_inv_list[i] = (mod_inv_list[i + 1] * (i + 1)) % MOD
    # RBを並べる
    res = (((mod_list[r + b] * mod_inv_list[r]) % MOD) * mod_inv_list[b]) % MOD
    # Rからk個選ぶ
    res *= (((mod_list[r] * mod_inv_list[k]) % MOD) * mod_inv_list[r - k]) % MOD
    res %= MOD
    # 選んだk個の右にGを置く
    # 残りのG(g - k)を置ける場所は(１番左 + 既にGを置いてるk箇所 + bの右)
    res *= (((mod_list[k + b + g - k] * mod_inv_list[k + b]) % MOD) * mod_inv_list[g - k]) % MOD
    res %= MOD
    return res


def main():
    r, g, b, k = map(int, input().split())
    res = solve(r, g, b, k)
    print(res)
    # for r in res:
    #     print(r)


def test():
    assert solve(2, 1, 1, 1) == 6
    assert solve(1000000, 1000000, 1000000, 1000000) == 80957240


if __name__ == "__main__":
    test()
    main()
