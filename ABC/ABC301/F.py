MOD = 998244353


def solve(s):
    alphabet_cnt = dict()
    for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        alphabet_cnt[c] = 0
    m = len(s)
    npr = [[0] * 27 for _ in range(27)]
    for i in range(27):
        npr[i][0] = 1
        for j in range(i):
            npr[i][j + 1] = (npr[i][j] * (i - j)) % MOD
    # print(npr)
    # DDが最初に出た時点
    res_1 = [0] * m
    # ?で作る大文字の種類数
    dp_1 = [[0] * 27 for _ in range(m + 1)]
    dp_1[0][0] = 1
    used_cap = 0
    break_flag = 0
    for i, c in enumerate(s):
        if c == "?":
            # 小文字にして逃げる
            for j in range(27):
                dp_1[i + 1][j] = (dp_1[i][j] * 26) % MOD
            # かぶらない大文字にする
            for j in range(26):
                dp_1[i + 1][j + 1] += dp_1[i][j]
                dp_1[i + 1][j + 1] %= MOD
            # かぶせる
            for j in range(27):
                if used_cap + j <= 26:
                    res_1[i] += dp_1[i][j] * (used_cap + j) * npr[26 - used_cap][j]
                    res_1[i] %= MOD
        elif c.upper() == c:
            if alphabet_cnt[c] == 0:
                for j in range(27):
                    dp_1[i + 1][j] = dp_1[i][j]
                used_cap += 1
                alphabet_cnt[c] += 1
                # かぶってた場合
                for j in range(1, 27):
                    res_1[i] += dp_1[i][j] * j * npr[26 - used_cap][j - 1]
                    res_1[i] %= MOD
            else:
                # 固定の大文字が2回出たのでここが最後
                # これ以降が最初のDDになることはない
                for j in range(27):
                    if j > 26 - used_cap:
                        continue
                    res_1[i] += dp_1[i][j] * npr[26 - used_cap][j]
                    res_1[i] %= MOD
                break
        else:
            for j in range(27):
                dp_1[i + 1][j] = dp_1[i][j]
    # そもそもDDがない
    res = 0
    if max(alphabet_cnt.values()) <= 1:
        for j in range(27):
            if j <= 26 - used_cap:
                res += dp_1[m][j] * npr[26 - used_cap][j]
                res %= MOD
    # print(res)
    # print(dp_1)
    # print(res_1)

    # oSが出てこない数
    dp_2 = [[0] * 2 for _ in range(m + 1)]
    dp_2[m][0] = 1
    c = s[-1]
    if c == "?":
        dp_2[m - 1][0] = 26
        dp_2[m - 1][1] = 26
    elif c.upper() == c:
        dp_2[m - 1][1] = 1
    else:
        dp_2[m - 1][0] = 1

    for i in range(m - 2, -1, -1):
        c = s[i]
        if c == "?":
            dp_2[i][0] = dp_2[i + 1][0] * 26
            dp_2[i][1] = (dp_2[i + 1][0] + dp_2[i + 1][1]) * 26
        elif c.upper() == c:
            dp_2[i][0] = 0
            dp_2[i][1] = dp_2[i + 1][0] + dp_2[i + 1][1]
        else:
            dp_2[i][0] = dp_2[i + 1][0]
            dp_2[i][1] = 0
        dp_2[i][0] %= MOD
        dp_2[i][1] %= MOD
    # print(dp_2)
    for i in range(m):
        res += res_1[i] * (dp_2[i + 1][0] + dp_2[i + 1][1])
        res %= MOD
    return res


def main():
    s = input()
    res = solve(s)
    print(res)


def test():
    assert solve("DD??S") == 676
    assert solve("????????????????????????????????????????") == 858572093
    assert solve("?D??S") == 136604


if __name__ == "__main__":
    test()
    main()
