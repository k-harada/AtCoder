# 解説みた
N, A, B = map(int, input().split())

LARGE = 10**9 + 7
DP = [[[0] * (N + 1) for _ in range(N + 1)] for _ in range(N + 1)]

DP[1][0][0] = 1


for n in range(1, N):
    for i in range(n + 1):
        for j in range(n + 1):
            DP[n + 1][i][j] = (DP[n + 1][i][j] + DP[n][i][j]) % LARGE
            DP[n + 1][i][j + 1] = (DP[n + 1][i][j + 1] + DP[n][i][j] * i) % LARGE
            DP[n + 1][i + 1][j] = (DP[n + 1][i + 1][j] + DP[n][i][j] * j) % LARGE
            DP[n + 1][i + 1][j + 1] = (DP[n + 1][i + 1][j + 1] + DP[n][i][j] * (n - i - j)) % LARGE

print(DP[N][A][B])
