import math

N, D = map(int, input().split())

X_list = []

for _ in range(N):
    X_list.append(list(map(int, input().split())))

res = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        dist_sq = 0
        for k in range(D):
            dist_sq += (X_list[i][k] - X_list[j][k]) ** 2
        if int(math.sqrt(dist_sq)) ** 2 == dist_sq:
            res += 1

print(res)
