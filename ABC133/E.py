from collections import deque

LARGE = 10 ** 9 + 7
N, K = map(int, input().split())

G = dict()
for i in range(1, N + 1):
    G[i] = dict()

for _ in range(N - 1):
    a, b = map(int, input().split())
    G[a][b] = 1
    G[b][a] = 1

root = 1
queue = deque([root])

depth = [N + 1] * (N + 1)
depth[root] = 0

c_list = [root]

while len(queue) > 0:

    p = queue.popleft()

    for q in G[p].keys():
        if depth[q] == N + 1:
            depth[q] = depth[p] + 1
            c_list.append(q)
            queue.append(q)


perm = [1]
for i in range(K - 2):
    perm.append((perm[-1] * (K - 2 - i)) % LARGE)


res = 1
for i in range(len(G[root].keys()) + 1):
    res = res * (K - i) % LARGE

for c in c_list[1:]:
    if len(G[c].keys()) >= K:
        res = 0
    else:
        res = res * perm[len(G[c].keys()) - 1] % LARGE

print(res)
