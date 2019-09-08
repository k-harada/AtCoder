N, M = map(int, input().split())

A = [[0] * M for _ in range(N)]
B = [[0] * M for _ in range(N)]

for i in range(N):
    A[i] = list(map(int, input().split()))

for i in range(N):
    B[i] = list(map(int, input().split()))

t_list = [10 ** 8] * (N + 1)
t_list[0] = 0

for i in range(N):
    s = t_list[i]
    for j in range(M):
        t = s + ((-s) % A[i][j]) + B[i][j]
        if t < t_list[i + 1]:
            t_list[i + 1] = t

print(t_list[-1])
