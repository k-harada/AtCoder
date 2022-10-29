from collections import defaultdict, deque

N, M, P = map(int, input().split())
G = defaultdict(lambda: defaultdict(lambda: 10000000))
G_rev = defaultdict(lambda: defaultdict(lambda: 10000000))

for _ in range(M):
    A, B, C = map(int, input().split())
    G[A][B] = min(G[A][B], P - C)
    G_rev[B][A] = 1

reachable_N = [0] * (N + 1)
reachable_N[N] = 1
queue = deque([N])

while len(queue) > 0:
    p = queue.popleft()
    for q in G_rev[p].keys():
        if reachable_N[q] == 0:
            reachable_N[q] = 1
            queue.append(q)

reachable_1 = [0] * (N + 1)
reachable_1[1] = 1
queue = deque([1])

while len(queue) > 0:
    p = queue.popleft()
    for q in G[p].keys():
        if reachable_1[q] == 0:
            reachable_1[q] = 1
            queue.append(q)

reachable = [reachable_1[i] * reachable_N[i] for i in range(N + 1)]

dist = [10000000000 for i in range(N + 1)]
res = 0
dist[1] = 0
queue = deque([1])
cnt = 0

update = True

while update:
    update = False
    for p in range(1, N + 1):
        if reachable[p] == 0:
            continue
        for q in G[p].keys():
            if reachable[q] == 0:
                pass
            elif dist[p] + G[p][q] < dist[q]:
                dist[q] = dist[p] + G[p][q]
                update = True
    cnt += 1
    if cnt > N:
        res = -1
        break

if res == -1:
    print(res)
else:
    print(max(0, -dist[N]))
