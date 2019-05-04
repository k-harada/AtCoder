from collections import deque

H, W = map(int, input().split())

# input black cells
black_cells = []

for h in range(H):
    line = list(input())
    for w in range(W):
        if line[w] == "#":
            black_cells.append(h * W + w)


# Graph
def r(p):
    q_list = []
    h = p // W
    w = p % W
    if h != 0:
        q_list.append(p - W)
    if h != H-1:
        q_list.append(p + W)
    if w != 0:
        q_list.append(p - 1)
    if w != W-1:
        q_list.append(p + 1)
    return q_list


queue = deque(black_cells)
d = [10000] * (H * W)
for i in black_cells:
    d[i] = 0

# dijkstra
while len(queue) > 0:
    p = queue.popleft()
    for q in r(p):
        if d[q] > d[p] + 1:
            d[q] = d[p] + 1
            queue.append(q)

print(max(d))