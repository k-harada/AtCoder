from collections import deque

# input
N = int(input())
G = dict()
for i in range(N):
    G[i] = dict()

for _ in range(N - 1):
    a, b = map(int, input().split())
    G[a-1][b-1] = 1
    G[b-1][a-1] = 1

# find diameter of the tree
# 2 times dijkstra
queue1 = deque([0])
d1 = [1000000] * N
d1[0] = 0

while len(queue1) > 0:
    p = queue1.popleft()
    for q in G[p].keys():
        if d1[q] > d1[p] + 1:
            d1[q] = d1[p] + 1
            queue1.append(q)
# find farthest
far = 0
dd = 0
for i in range(N):
    if d1[i] > dd:
        far = i
        dd = d1[i]

queue2 = deque([far])
d2 = [1000000] * N
d2[far] = 0

while len(queue2) > 0:
    p = queue2.popleft()
    for q in G[p].keys():
        if d2[q] > d2[p] + 1:
            d2[q] = d2[p] + 1
            queue2.append(q)
diam = max(d2)
# print(diam)
if diam % 3 == 1:
    print("Second")
else:
    print("First")