from heapq import heappush, heappop

N = int(input())
v_list = list(map(int, input().split()))

h = []

for v in v_list:
    heappush(h, v)

while len(h) >= 2:
    a = heappop(h)
    b = heappop(h)
    heappush(h, (a + b) / 2)

print(heappop(h))
