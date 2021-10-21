def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def solve(n, a_list):
    dp = [[0] * 2 for _ in range(n + 1)]
    dp[0][1] = 1
    div = [[1] * 2 for _ in range(n + 1)]
    choice = [[0] * 2 for _ in range(n + 1)]
    for i in range(n):
        a = a_list[i]
        if dp[i][0] * div[i + 1][1] >= a * dp[i][1]:
            dp[i + 1][0] = dp[i][0]
            choice[i + 1][0] = 0
        else:
            dp[i + 1][0] = a * dp[i][1]

            choice[i + 1][0] = 1
        if a * dp[i][1] >= dp[i][0]:
            dp[i + 1][1] = dp[i][1]
            choice[i + 1][1] = 0
        else:
            dp[i + 1][1] = dp[i][0]
            div[i + 1][1] = a
            choice[i + 1][1] = 1
        d = gcd(dp[i + 1][0], dp[i + 1][1])
    res = ["0"] * n
    k = 1
    for i in range(n, 0, -1):
        if choice[i][k] == 1:
            k = 1 - k
            res[i - 1] = "1"
    return " ".join(res)


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(3, [3, 5, 2]) == "0 1 1"
    assert solve(4, [1, 1, 1, 1]) == "0 0 0 0"
    assert solve(10, [
        426877385, 186049196, 624834740, 836880476, 19698398, 709113743, 436942115, 436942115, 436942115, 503843678
    ]) == "1 1 0 1 1 1 1 0 0 0"


if __name__ == "__main__":
    test()
    main()
