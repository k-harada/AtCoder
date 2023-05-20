from bisect import bisect_right


MOD = 998244353


def solve(s):
    res = 0
    places = dict()
    for c in "abcdefghijklmnopqrstuvwxyz":
        places[c] = []
    for i, c in enumerate(s):
        places[c].append(i)

    # (p + 1)文字目から使われる文字列
    for p in range(1, len(s)):
        dp = [[0] * (len(s) + 1) for _ in range(p)]
        c = s[p]
        ii = places[c][0]
        if ii == p:
            continue
        dp[ii][p] = 1
        for k in range(ii + 1, p):
            c = s[k]
            for i0 in range(k):
                i1_ = bisect_right(places[c], i0)
                i1 = places[c][i1_]
                if i1 < k:
                    continue
                for j0 in range(len(s) + 1):
                    j1_ = bisect_right(places[c], j0)
                    if j1_ == len(places[c]):
                        continue
                    j1 = places[c][j1_]

                    dp[i1][j1] += dp[i0][j0]
                    dp[i1][j1] %= MOD
        for i in range(p):
            i_ = bisect_right(places[s[p]], i)
            if places[s[p]][i_] != p:
                # print("fail", i, p)
                continue
            for j in range(len(s) + 1):
                res += dp[i][j]
        res %= MOD
        # print(p)
        # print(dp)
        # print(p, res)
    # print(res)
    return res


def main():
    s = input()
    res = solve(s)
    print(res)


def test():
    assert solve("ababbaba") == 8
    assert solve("zzz") == 1
    assert solve("ppppqqppqqqpqpqppqpqqqqpppqppq") == 580


if __name__ == "__main__":
    test()
    main()
