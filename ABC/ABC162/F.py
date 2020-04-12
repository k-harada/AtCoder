def solve(n, a_list):
    if n % 2 == 0:
        res_a = [0] * (n // 2 + 1)
        res_b = [0] * (n // 2 + 1)
        for i in range(0, n // 2):
            res_a[i + 1] = res_a[i] + a_list[i * 2]
        for i in range(n // 2 - 1, -1, -1):
            res_b[i] = res_b[i + 1] + a_list[i * 2 + 1]
        return max([res_a[i] + res_b[i] for i in range(n // 2 + 1)])
    else:
        # type a
        dp = [[0] * 3 for _ in range(n)]
        dp[0][0] = a_list[0]
        dp[1][1] = a_list[1]
        dp[2][2] = a_list[2]
        for i in range(n):
            if i % 2 == 0:
                if i >= 2:
                    dp[i][0] = dp[i - 2][0] + a_list[i]
                    dp[i][1] = dp[i - 1][1]
                if i >= 3:
                    dp[i][2] = max(dp[i - 3][1] + a_list[i], dp[i - 2][2] + a_list[i])
            else:
                if i >= 3:
                    dp[i][1] = max(dp[i - 2][1] + a_list[i], dp[i - 3][0] + a_list[i])
                dp[i][0] = dp[i - 1][0]
                dp[i][2] = dp[i - 1][2]
        res_a = max(dp[-1])
        # print(dp)

        # type b
        even = [a_list[i] for i in range(0, n, 2)]
        res_b = sum(even) - min(even)

        return max(res_a, res_b)


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(6, [1, 2, 3, 4, 5, 6]) == 12
    assert solve(5, [-1000, -100, -10, 0, 10]) == 0
    assert solve(10, [1000000000] * 10) == 5000000000


if __name__ == "__main__":
    test()
    main()
