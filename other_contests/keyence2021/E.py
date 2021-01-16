from functools import lru_cache


def solve(n, a_list):
    dp = [[[0] * (n + 2) for _ in range(n + 2)] for _ in range(n + 1)]
    dp[0][0][0] = 0
    a_list_add = [0] + a_list + [0]

    for d in range(n, 0, -1):
        for i in range(n - d + 2):
            j = i + d
            # pass
            if a_list_add[i] > a_list_add[j]:
                for k in range(n - 1):
                    dp[i][j][k] = max(dp[i - 1][j][k + 1], dp[i][j][k])
            elif j < n + 1:
                for k in range(n - 1):
                    dp[i][j][k] = max(dp[i][j + 1][k + 1], dp[i][j][k])
            # take left usual way
            if i > 0:
                if a_list_add[i - 1] > a_list_add[j]:
                    for k in range(n):
                        dp[i][j][k] = max(dp[i - 2][j][k] + a_list_add[i], dp[i][j][k])
                elif j < n + 1:
                    for k in range(n):
                        dp[i][j][k] = max(dp[i - 1][j + 1][k] + a_list_add[i], dp[i][j][k])
                else:
                    for k in range(n):
                        dp[i][j][k] = max(dp[i - 1][j][k] + a_list_add[i], dp[i][j][k])
            # take left using coin
            if i > 0:
                for k in range(1, n):
                    dp[i][j][k] = max(dp[i - 1][j][k - 1] + a_list_add[i], dp[i][j][k])
            # take right usual way
            if j < n + 1:
                if a_list_add[i] < a_list_add[j + 1]:
                    for k in range(n):
                        dp[i][j][k] = max(dp[i][j + 2][k] + a_list_add[j], dp[i][j][k])
                elif i > 0:
                    for k in range(n):
                        dp[i][j][k] = max(dp[i - 1][j + 1][k] + a_list_add[j], dp[i][j][k])
                else:
                    for k in range(n):
                        dp[i][j][k] = max(dp[i][j + 1][k] + a_list_add[j], dp[i][j][k])
            # take right using coin
            if j < n + 1:
                for k in range(1, n):
                    dp[i][j][k] = max(dp[i][j + 1][k - 1] + a_list_add[j], dp[i][j][k])
    res_list = []
    for i in range(n + 1):
        res_list.append(dp[i][i + 1][0])
    # print(res_list)
    return res_list


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res_list = solve(n, a_list)
    for res in res_list:
        print(res)


def test():
    assert solve(7, [4, 3, 1, 2, 1000, 2000, 3000]) == [6004, 6004, 6004, 6001, 5007, 4007, 4007, 4007]


if __name__ == "__main__":
    test()
    main()
