from collections import deque


def solve(n, abc_list, d_list):
    g = [[] for _ in range(n + 1)]
    cost = {i: dict() for i in range(1, n + 1)}
    for a, b, c in abc_list:
        g[a].append(b)
        g[b].append(a)
        cost[a][b] = c
        cost[b][a] = c

    # root 1
    queue = deque([1])
    depth = [0] * (n + 1)
    parent = [0] * (n + 1)
    parent[1] = -1
    while len(queue):
        p = queue.popleft()
        for q in g[p]:
            if parent[q] == 0:
                parent[q] = p
                depth[q] = depth[p] + 1
                queue.append(q)

    # from leaf
    order = list(sorted([(i, depth[i]) for i in range(1, n + 1)], key=lambda x: (-x[1], x[0])))
    p_list = [order[i][0] for i in range(n)]

    cost_up = [[0, 0, 0, 0]] + [[d_list[i], i + 1, 0, 0] for i in range(n)]
    # print(cost_up)

    for p in p_list[:-1]:
        q = parent[p]
        if cost_up[p][0] + cost[p][q] >= cost_up[q][0]:
            cost_up[q][2] = cost_up[q][0]
            cost_up[q][3] = cost_up[q][1]
            cost_up[q][0] = cost_up[p][0] + cost[p][q]
            cost_up[q][1] = p
        elif cost_up[p][0] + cost[p][q] >= cost_up[q][2]:
            cost_up[q][2] = cost_up[p][0] + cost[p][q]
            cost_up[q][3] = p
    # print(cost_up)
    # down
    for q in reversed(p_list[:-1]):
        p = parent[q]
        if cost_up[p][1] != q:
            if cost_up[p][0] + cost[p][q] >= cost_up[q][0]:
                cost_up[q][2] = cost_up[q][0]
                cost_up[q][3] = cost_up[q][1]
                cost_up[q][0] = cost_up[p][0] + cost[p][q]
                cost_up[q][1] = p
            elif cost_up[p][0] + cost[p][q] >= cost_up[q][2]:
                cost_up[q][2] = cost_up[p][0] + cost[p][q]
                cost_up[q][3] = p
        else:
            if cost_up[p][2] + cost[p][q] >= cost_up[q][0]:
                cost_up[q][2] = cost_up[q][0]
                cost_up[q][3] = cost_up[q][1]
                cost_up[q][0] = cost_up[p][2] + cost[p][q]
                cost_up[q][1] = p
            elif cost_up[p][2] + cost[p][q] >= cost_up[q][2]:
                cost_up[q][2] = cost_up[p][2] + cost[p][q]
                cost_up[q][3] = p
    # print(cost_up)
    res = []
    for p in range(1, n + 1):
        if cost_up[p][1] != p:
            res.append(cost_up[p][0])
        else:
            res.append(cost_up[p][2])
    # print(res)
    return res


def main():
    n = int(input())
    abc_list = [tuple(map(int, input().split())) for _ in range(n - 1)]
    d_list = list(map(int, input().split()))
    res = solve(n, abc_list, d_list)
    for r in res:
        print(r)


def test():
    assert solve(3, [(1, 2, 2), (2, 3, 3)], [1, 2, 3]) == [8, 6, 6]
    assert solve(
        6, [(1, 2, 3), (1, 3, 1), (1, 4, 4), (1, 5, 1), (1, 6, 5)], [9, 2, 6, 5, 3, 100]
    ) == [105, 108, 106, 109, 106, 14]
    assert solve(6, [
        (1, 2, 1000000000), (2, 3, 1000000000), (3, 4, 1000000000), (4, 5, 1000000000), (5, 6, 1000000000)
    ], [1, 2, 3, 4, 5, 6]) == [5000000006, 4000000006, 3000000006, 3000000001, 4000000001, 5000000001]


if __name__ == "__main__":
    test()
    main()
