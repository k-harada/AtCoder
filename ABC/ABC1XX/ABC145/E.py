def solve(n, t, ab_list):
    ab_list_s = sorted(ab_list, key=lambda x: x[0])
    res = 0
    dp = [0] * t
    for i in range(n):
        for s in range(t - 1, -1, -1):
            if dp[s] > 0 or s == 0:
                u = s + ab_list_s[i][0]
                r = dp[s] + ab_list_s[i][1]
                if u >= t:
                    res = max(res, r)
                else:
                    dp[u] = max(dp[u], r)
    return max(res, max(dp))


def main():
    n, t = map(int, input().split())
    ab_list = []
    for _ in range(n):
        a, b = map(int, input().split())
        ab_list.append([a, b])
    res = solve(n, t, ab_list)
    print(res)


def test():
    assert solve(2, 60, [[10, 10], [100, 100]]) == 110
    assert solve(3, 60, [[10, 10], [10, 20], [10, 30]]) == 60
    assert solve(3, 60, [[30, 10], [30, 20], [30, 30]]) == 50


if __name__ == "__main__":
    test()
    main()
