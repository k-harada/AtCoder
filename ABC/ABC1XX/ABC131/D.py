from heapq import heappop, heappush

N = int(input())
h = []
res = 'Yes'

for i in range(N):
    A, B = map(int, input().split())
    heappush(h, (B, A))

t = 0
for i in range(N):
    B, A = heappop(h)
    t += A
    if t > B:
        res = 'No'

print(res)
