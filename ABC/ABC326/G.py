def solve(s, k):
    m = len(s)
    res_len = [[0] * (m + 1) for _ in range(m + 1)]
    for i in range(m):
        for j in range(i + 1, m + 1):
            res_len[i][j] = j - i

    for d in range(2, m + 1):
        for i in range(m - d + 1):
            j = i + d
            for p in range(i, j):
                res_len[i][j] = min(res_len[i][j], res_len[i][p] + res_len[p][j])
            if s[i] == "o":
                for p in range(i + 1, j):
                    if s[p] == "f":
                        if res_len[i + 1][p] == 0:
                            res_len[i][j] = min(res_len[i][j], max(res_len[p + 1][j] - k, 0))
            # print(i, j, res_len[i][j])

    # print(res_len)
    # print(res_len[0][m])
    return res_len[0][m]


def main():
    s = input()
    k = int(input())
    res = solve(s, k)
    print(res)


def test():
    assert solve("keyofscience", 3) == 7
    assert solve("oofsifffence", 3) == 2
    assert solve("ooofff", 5) == 0
    assert solve("okeyencef", 4) == 9


if __name__ == "__main__":
    test()
    main()
