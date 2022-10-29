MOD = 998244353
N = 200
factorial = [1] * (N + 1)
factorial_inv = [1] * (N + 1)
for i in range(1, N + 1):
    factorial[i] = (factorial[i - 1] * i) % MOD

factorial_inv[-1] = pow(factorial[-1], MOD - 2, MOD)

for i in range(N, 0, -1):
    factorial_inv[i - 1] = (factorial_inv[i] * i) % MOD


def ncr(n, k):
    return (factorial[n] * factorial_inv[k] % MOD) * factorial_inv[n - k] % MOD


def solve(n, m, ab_list):
    dp1 = [[0] * 2 * n for _ in range(2 * n)]
    dp2 = [[0] * 2 * n for _ in range(2 * n)]
    abd_list = [(a - 1, b - 1, b - a) for a, b in ab_list if (b - a) % 2 == 1]
    abd_list_s = list(sorted(abd_list, key=lambda x: (x[2], x[0])))
    friend = [[0] * 2 * n for _ in range(2 * n)]
    # print(abd_list_s)
    for a, b, d in abd_list_s:
        if d == 1:
            dp1[a][b] = 1
            dp2[a][b] = 1
        friend[a][b] = 1

    for d in range(3, 2 * n + 1, 2):
        nd = (d + 1) // 2
        for left in range(2 * n - d):
            right = left + d
            if friend[left][right]:
                dp1[left][right] = dp1[left + 1][right - 1]
                dp2[left][right] = dp1[left + 1][right - 1]
            for mid in range(left + 2, right, 2):
                dp1[left][right] += (dp1[left][mid - 1] * dp2[mid][right] % MOD) * ncr(nd, (mid - left) // 2)
            dp1[left][right] %= MOD
    # print(dp1[0][2 * n - 1])
    return dp1[0][2 * n - 1]


def main():
    n, m = map(int, input().split())
    ab_list = [tuple(map(int, input().split())) for _ in range(m)]
    res = solve(n, m, ab_list)
    print(res)


def test():
    assert solve(2, 3, [(1, 2), (1, 4), (2, 3)]) == 1
    assert solve(2, 2, [(1, 2), (3, 4)]) == 2
    assert solve(2, 2, [(1, 3), (2, 4)]) == 0


if __name__ == "__main__":
    test()
    main()
