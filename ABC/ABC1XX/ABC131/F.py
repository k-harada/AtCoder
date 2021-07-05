# 答えみた
from collections import deque

N = int(input())

x_list = [0] * N
y_list = [0] * N

for i in range(N):
    x, y = map(int, input().split())
    x_list[i] = x + 1000000
    y_list[i] = y

# graph
G = dict()
for i in range(N):
    x = x_list[i]
    y = y_list[i]
    G[x] = dict()
    G[y] = dict()

for i in range(N):
    x = x_list[i]
    y = y_list[i]
    G[x][y] = 1
    G[y][x] = 1

x_su = list(set(x_list))
Lx = len(x_su)
x_su_ind = dict()
for i in range(Lx):
    x_su_ind[x_su[i]] = i

y_su = list(set(y_list))
Ly = len(y_su)
y_su_ind = dict()
for i in range(Ly):
    y_su_ind[y_su[i]] = i

done_x = [0]*Lx
done_y = [0]*Ly

res = 0

id_0 = 0
while True:
    while done_x[id_0] == 1:
        id_0 += 1
        if id_0 == Lx:
            break
    if id_0 == Lx:
        break
    # BFS
    cx = 1
    cy = 0
    queue = deque([x_su[id_0]])
    done_x[id_0] = 1
    while len(queue) > 0:
        p = queue.popleft()
        for q in G[p].keys():
            if q < 1000000:
                if done_y[y_su_ind[q]] == 0:
                    queue.append(q)
                    done_y[y_su_ind[q]] = 1
                    cy += 1
            else:
                if done_x[x_su_ind[q]] == 0:
                    queue.append(q)
                    done_x[x_su_ind[q]] = 1
                    cx += 1
    res += cx * cy

print(res - N)
