from collections import defaultdict, deque

N, M, K = map(int, input().split())
t_list = [0] * N

for i in range(2, N):
    t_list[i] = int(input())

G = defaultdict(dict)

for _ in range(M):
    a, b, c, d = map(int, input().split())
    G[a][b] = (c, d)
    G[b][a] = (c, d)

# dijkstra
time_first = [K + 1] * (N + 1)
time_first[1] = 0

queue = deque([1])

while len(queue) > 0:
    p = queue.popleft()
    s = time_first[p] + t_list[p]
    for q in G[p].keys():
        c, d = G[p][q]
        t = s + ((-s) % d) + c
        if t < time_first[q]:
            time_first[q] = t
            if q != N:
                queue.append(q)

if time_first[N] <= K:
    print(time_first[N])
else:
    print(-1)
