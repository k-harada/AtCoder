from heapq import heappop, heappush

N = int(input())
h = []
for _ in range(N):
    s, t = map(int, input().split())
    heappush(h, (s, t))

res = 0
T = 0

while len(h) > 0:
    s, t = heappop(h)
    if s > T:
        res += 1
    T = max(T, t)

print(res)
