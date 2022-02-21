MOD = 998244353


def solve(l, r, v):

    res = 0

    if v == 0 or v == 1:
        # 4離れた組み合わせの数
        if l % 2 == 0:
            l_ = l
        elif l == 1:
            l_ = 0
        else:
            l_ = l + 1
        if r % 2 == 1:
            r_ = r + 1
        else:
            r_ = r
        c = (r_ - l_) // 4
        d_1 = (c * (c - 1) // 2) % MOD
        c = (r_ - l_ - 2) // 4
        if c < 0:
            c = 0
        d_2 = (c * (c - 1) // 2) % MOD
        c = (r_ - l_) // 2
        d_3 = (c * (c - 1) // 2) % MOD
        if v == 0:
            res += d_1 + d_2
            res %= MOD
        else:
            res += d_3 - d_1 - d_2
            res %= MOD
        return res

    if l <= v <= r:
        # self + 0
        if v % 2 == 1:
            res += 1
            res += (r - v) // 4
            res %= MOD
        else:
            res += 1
            res += (v - l) // 4
            res %= MOD
        # self + 1
        if v % 2 == 1 and v - 1 >= l:
            res += (v - 1 - l) // 2 - (v - 1 - l) // 4
            res %= MOD
        elif v % 2 == 0 and v + 1 <= r:
            res += (r - v - 1) // 2 - (r - v - 1) // 4
            res %= MOD

    # a: 奇数, b: 偶数


    return 0


def main():
    l, r, v = map(int, input().split())
    res = solve(l, r, v)
    print(res)
    # for r in res:
    #     print(r)


def test():
    assert solve() == 0
    assert solve() == 0
    assert solve() == 0


if __name__ == "__main__":
    test()
    main()
