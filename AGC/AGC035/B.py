from collections import deque
N, M = map(int, input().split())


G = dict()
edge_dict = dict()
count_list = [0] * (N + 1)

for i in range(1, N + 1):
    G[i] = dict()
    edge_dict[i] = dict()

for _ in range(M):
    A, B = map(int, input().split())
    if A > B:
        A, B = B, A
    G[A][B] = 1
    G[B][A] = 1
    edge_dict[A][B] = 1
    edge_dict[B][A] = -1
    count_list[A] += 1

if M % 2 == 1:
    print(-1)
else:
    # minimum spanning tree
    parent = [0] * (N + 1)
    node_list = []
    queue = deque([1])
    visited = [0] * (N + 1)
    # BFS
    while len(queue) > 0:
        p = queue.popleft()
        for q in G[p].keys():
            if visited[q]:
                continue
            else:
                parent[q] = p
                visited[q] = 1
                queue.append(q)
                node_list.append(q)

    while len(node_list) > 0:
        q = node_list.pop()
        p = parent[q]
        if count_list[q] % 2 == 1:
            edge_dict[p][q] *= -1
            edge_dict[q][p] *= -1
            count_list[p] += 1
            count_list[q] += 1

    for i in range(1, N + 1):
        for j in edge_dict[i].keys():
            if edge_dict[i][j] == 1:
                print(i, j)
