from collections import deque

N, M = map(int, input().split())

G = dict()

for i in range(1, 3 * N + 1):
    G[i] = dict()

for _ in range(M):
    u, v = map(int, input().split())
    G[u][N + v] = 1
    G[N + u][2 * N + v] = 1
    G[2 * N + u][v] = 1

S, T = map(int, input().split())

dist_S = [3 * N + 1] * (3 * N + 1)
dist_S[S] = 0

# BFS
queue = deque([S])
while len(queue) > 0:
    p = queue.popleft()
    for q in G[p].keys():
        if dist_S[p] + 1 < dist_S[q]:
            dist_S[q] = dist_S[p] + 1
            queue.append(q)

if dist_S[T] < 3 * N + 1:
    print(dist_S[T] // 3)
else:
    print(-1)
