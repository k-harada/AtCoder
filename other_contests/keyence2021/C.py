MOD = 998244353


def solve(h, w, k, ijc_list):
    div3 = pow(3, MOD - 2, MOD)
    dp = [[0] * w for _ in range(h)]
    flag = [["F"] * w for _ in range(h)]
    dp[0][0] = pow(3, h * w - k, MOD)
    for i, j, c in ijc_list:
        flag[int(i) - 1][int(j) - 1] = c
    for i in range(h):
        for j in range(w):
            r = 0
            if i > 0:
                if flag[i - 1][j] == "F":
                    r += dp[i - 1][j] * 2 * div3
                elif flag[i - 1][j] == "X" or flag[i - 1][j] == "D":
                    r += dp[i - 1][j]
            if j > 0:
                if flag[i][j - 1] == "F":
                    r += dp[i][j - 1] * 2 * div3
                elif flag[i][j - 1] == "X" or flag[i][j - 1] == "R":
                    r += dp[i][j - 1]
            r %= MOD
            dp[i][j] += r
    # print(dp)
    return dp[h - 1][w - 1]


def main():
    h, w, k = map(int, input().split())
    ijc_list = [tuple(input().split()) for _ in range(k)]
    res = solve(h, w, k, ijc_list)
    print(res)


def test():
    assert solve(2, 2, 3, [(1, 1, "X"), (2, 1, "R"), (2, 2, "R")]) == 5
    assert solve(3, 3, 5, [(2, 3, "D"), (1, 3, "D"), (2, 1, "D"), (1, 2, "X"), (3, 1, "R")]) == 150


if __name__ == "__main__":
    test()
    main()
