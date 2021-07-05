from collections import deque

N = int(input())
G = dict()

# Graph
for i in range(1, N + 1):
    G[i] = dict()

for _ in range(N - 1):
    u, v, w = map(int, input().split())
    G[u][v] = w
    G[v][u] = w

# start from 1
res = [2]*(N+1)
res[1] = 0
queue = deque([1])

while len(queue) > 0:
    u = queue.popleft()
    for v in G[u].keys():
        if res[v] == 2:
            if G[u][v] % 2 == 1:
                res[v] = 1 - res[u]
            else:
                res[v] = res[u]
            queue.append(v)

for i in range(1, N + 1):
    print(res[i])
