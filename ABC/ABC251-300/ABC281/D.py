def solve(n, k, d, a_list):
    dp = [[-1] * d for _ in range(k + 1)]
    dp[0][0] = 0
    for i in range(n):
        a = a_list[i]
        for c in range(k - 1, -1, -1):
            for v in range(d):
                if dp[c][v] >= 0:
                    dp[c + 1][(v + a) % d] = max(dp[c + 1][(v + a) % d], dp[c][v] + a)
    return dp[k][0]


def main():
    n, k, d = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, k, d, a_list)
    print(res)


def test():
    assert solve(4, 2, 2, [1, 2, 3, 4]) == 6
    assert solve(3, 1, 2, [1, 3, 5]) == -1


if __name__ == "__main__":
    test()
    main()
