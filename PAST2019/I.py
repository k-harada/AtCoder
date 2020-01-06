def solve(n, m, s_list, c_list):
    dp = [[sum(c_list) + 1] * (2 ** n) for _ in range(m + 1)]
    dp[0][0] = 0

    for i in range(m):
        k = 0
        s = s_list[i]
        for p in range(n):
            if s[- p - 1] == "Y":
                k += 2 ** p
        c = c_list[i]
        for j in range(2 ** n):
            dp[i + 1][j] = dp[i][j]
        for j in range(2 ** n):
            dp[i + 1][j | k] = min(dp[i + 1][j | k], dp[i][j] + c)

    # print(dp)
    res = dp[m][2 ** n - 1]
    if res == sum(c_list) + 1:
        return -1
    else:
        return res


def main():
    n, m = map(int, input().split())
    s_list = [""] * m
    c_list = [0] * m
    for i in range(m):
        s, c = input().split()
        s_list[i] = s
        c_list[i] = int(c)
    res = solve(n, m, s_list, c_list)
    print(res)


def test():
    assert solve(3, 4, ["YYY", "YYN", "YNY", "NYY"], [100, 20, 10, 25]) == 30
    assert solve(5, 4, ["YNNNN", "NYNNN", "NNYNN", "NNNYN"], [10, 10, 10, 10]) == -1


if __name__ == "__main__":
    test()
    main()
