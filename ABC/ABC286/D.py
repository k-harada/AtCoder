def solve(n, x, ab_list):
    dp = [[0] * (x + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i, (a, b) in enumerate(ab_list):
        for s in range(x + 1):
            if dp[i][s] == 1:
                for u in range(b + 1):
                    if s + a * u > x:
                        break
                    dp[i + 1][s + a * u] = 1
    if dp[-1][x] == 1:
        return "Yes"
    else:
        return "No"


def main():
    n, x = map(int, input().split())
    ab_list = [tuple(map(int, input().split())) for _ in range(n)]
    res = solve(n, x, ab_list)
    print(res)


def test():
    assert solve(2, 19, [(2, 3), (5, 6)]) == "Yes"
    assert solve(2, 18, [(2, 3), (5, 6)]) == "No"
    assert solve(3, 1001, [(1, 1), (2, 1), (100, 10)]) == "Yes"


def test_large():
    print(solve(50, 10000, [(i + 1, 50) for i in range(50)]))


if __name__ == "__main__":
    test()
    # test_large()
    main()
