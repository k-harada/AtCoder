from collections import defaultdict

N, Q = map(int, input().split())

G = defaultdict(list)

for _ in range(N - 1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

parents = [0] * (N + 1)
values = [0] * (N + 1)
values_sum = [-1] * (N + 1)

for _ in range(Q):
    p, x = map(int, input().split())
    values[p] += x

# solve
values_sum[1] = values[1]

queue = [1]
while len(queue) > 0:
    p = queue.pop()
    for q in G[p]:
        if values_sum[q] == -1:
            values_sum[q] = values_sum[p] + values[q]
            queue.append(q)

print(*values_sum[1:])
