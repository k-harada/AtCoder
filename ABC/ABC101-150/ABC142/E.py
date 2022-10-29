def solve_e(n, m, a_list, k_list):
    dp = [[10 ** 9] * (2 ** n) for _ in range(m + 1)]
    dp[0][0] = 0

    # update
    for i in range(m):
        k = k_list[i]
        for j in range(2 ** n):
            ll = (k ^ j) + ((k + j - (k ^ j)) // 2) - k
            dp[i + 1][j] = min(dp[i][j], dp[i][ll] + a_list[i])

    # print(dp)
    if dp[m][2 ** n - 1] == 10 ** 9:
        return -1
    else:
        return dp[m][2 ** n - 1]


def main():
    n, m = map(int, (input().split()))
    a_list = [0] * m
    k_list = [0] * m
    for i in range(m):
        a, b = map(int, (input().split()))
        a_list[i] = a
        c_list = list(map(int, (input().split())))
        k_list[i] = sum([2 ** (c - 1) for c in c_list])

    res = solve_e(n, m, a_list, k_list)
    print(res)


if __name__ == "__main__":
    main()