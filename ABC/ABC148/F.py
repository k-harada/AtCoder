from collections import deque


def solve(n, u, v, edge_list):
    # graph
    g = [[] for i in range(n)]
    for a, b in edge_list:
        g[a].append(b)
        g[b].append(a)

    # root at v
    parent = [0] * n
    depth = [0] * n
    parent[v] = -1
    queue = deque([v])
    while len(queue) > 0:
        p = queue.popleft()
        for q in g[p]:
            if parent[p] != q:
                parent[q] = p
                depth[q] = depth[p] + 1
                queue.append(q)

    # collect max_depth from leaf
    temp_list = [[i, -depth[i]] for i in range(n)]
    temp_list = list(sorted(temp_list, key=lambda x: x[1]))
    run_list = [temp_list[i][0] for i in range(n)]
    max_children_depth = depth.copy()
    for i in run_list[:-1]:
        max_children_depth[parent[i]] = max(max_children_depth[parent[i]], max_children_depth[i])
    # print(depth)
    # print(max_children_depth)
    du = depth[u]
    up = u
    res = 0
    if du > 2:
        for _ in range((du - 1) // 2):
            up = parent[up]
            res += 1
    res += max_children_depth[up] - depth[up]
    if du % 2 == 0:
        res += 1
    return res


def main():
    n, u, v = map(int, input().split())
    edge_list = [[0, 0] for _ in range(n - 1)]
    for i in range(n - 1):
        a, b = map(int, input().split())
        edge_list[i][0] = a - 1
        edge_list[i][1] = b - 1
    u -= 1
    v -= 1
    res = solve(n, u, v, edge_list)
    print(res)


def test():
    assert solve(5, 3, 0, [[0, 1], [1, 2], [2, 3], [2, 4]]) == 2
    assert solve(5, 3, 4, [[0, 1], [0, 2], [0, 3], [0, 4]]) == 1
    assert solve(2, 0, 1, [[0, 1]]) == 0


if __name__ == "__main__":
    test()
    main()
