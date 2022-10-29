from collections import deque

N, Q = map(int, input().split())

a_list = [0] * (N - 1)
b_list = [0] * (N - 1)
c_list = [0] * (N - 1)
d_list = [0] * (N - 1)

G = dict()
for i in range(1, N + 1):
    G[i] = dict()

for i in range(N - 1):
    a, b, c, d = map(int, input().split())

    a_list[i] = a
    b_list[i] = b
    c_list[i] = c
    d_list[i] = d

    G[a][b] = 1
    G[b][a] = 1


K = 0
while 2**K <= N:
    K += 1

# pre_compute
root = 1
depth = [N + 1] * (N + 1)
parent = [[-1] * (N + 1) for _ in range(K + 1)]
depth[root] = 0

queue = deque([root])

while len(queue) > 0:
    p = queue.popleft()
    for q in G[p].keys():
        if depth[q] == N + 1:
            depth[q] = depth[p] + 1
            parent[0][q] = p

for k in range(K):
    for p in range(1, N + 1):
        if parent[k][p] < 0:
            parent[k + 1][p] = -1
        else:
            parent[k + 1][p] = parent[k][parent[k][p]]


# LCA
def find_lca(u, v):
    if depth[u] > depth[v]:
        u, v = v, u
    for k in range(K, -1, -1):
        if depth[v] - depth[u] >= 2**k:
            v = parent[k][v]
    if u == v:
        return u

    for k in range(K, -1, -1):
        if parent[k][u] != parent[k][v]:
            u = parent[k][u]
            v = parent[k][v]
    return parent[0][u]


