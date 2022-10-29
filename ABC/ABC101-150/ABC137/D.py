from collections import defaultdict
from heapq import heappush, heappop

N, M = map(int, input().split())
d = defaultdict(list)

for _ in range(N):
    a, b = map(int, input().split())
    d[a].append(b)

h = []
res = 0
for a in range(1, M + 1):
    for b in d[a]:
        heappush(h, -b)
    if len(h) > 0:
        c = heappop(h)
        res -= c

print(res)
