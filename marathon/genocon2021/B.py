# ref: https://tjkendev.github.io/procon-library/python/dp/lcs.html


def solve(s, t):
    m = len(s)
    n = len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m - 1, -1, -1):
        dp[i][n] = dp[i + 1][n] - 5

    for j in range(n - 1, -1, -1):
        dp[m][j] = dp[m][j + 1] - 5

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            # skip
            r = max(dp[i + 1][j], dp[i][j + 1]) - 5
            # accept
            if s[i] == t[j]:
                r = max(r, dp[i + 1][j + 1] + 1)
            else:
                r = max(r, dp[i + 1][j + 1] - 3)
            dp[i][j] = r

    # print(dp)
    # print(dp[0][0])

    new_s_list = []
    new_t_list = []
    i = 0
    j = 0
    while i < m and j < n:
        if dp[i][j] > max(dp[i + 1][j], dp[i][j + 1]) - 5:
            new_s_list.append(s[i])
            new_t_list.append(t[j])
            # print(i, j, s[i], t[j])
            i += 1
            j += 1
        elif dp[i + 1][j] > dp[i][j + 1]:
            new_s_list.append(s[i])
            new_t_list.append("-")
            i += 1
        else:
            new_s_list.append("-")
            new_t_list.append(t[j])
            j += 1

    while i < m:
        new_s_list.append(s[i])
        new_t_list.append("-")
        i += 1

    while j < n:
        new_s_list.append("-")
        new_t_list.append(t[j])
        j += 1

    new_s = "".join(new_s_list)
    new_t = "".join(new_t_list)
    # print(new_s, new_t)
    return new_s, new_t


def main():
    s = input()
    t = input()
    res_1, res_2 = solve(s, t)
    print(res_1)
    print(res_2)


def test():
    assert solve("AGTTGAATTT", "GTCGGACTTT") == ("AGT-TGAATTT", "-GTCGGACTTT")


if __name__ == "__main__":
    test()
    main()
