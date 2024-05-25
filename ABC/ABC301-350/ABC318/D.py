def solve(n, d):
    res_min = n * (10 ** 9)
    if n % 2 == 1:
        d = [[0] * n] + d
        n += 1
    dp = [0] * (2 ** n)
    for i in range(n - 1):
        for j in range(i + 1, n):
            b = (2 ** i) + (2 ** j)
            for x in range(2 ** n):
                if b ^ x == b + x:
                    dp[b + x] = max(dp[b + x], dp[x] + d[i][j - i - 1])
    # print(dp)
    return dp[-1]


def main():
    n = int(input())
    d = [list(map(int, input().split())) for _ in range(n - 1)]
    res = solve(n, d)
    print(res)


def test():
    assert solve(4, [[1, 5, 4], [7, 8], [6]]) == 13
    assert solve(3, [[1, 2], [3]]) == 3


if __name__ == "__main__":
    test()
    main()
