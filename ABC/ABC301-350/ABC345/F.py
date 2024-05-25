from collections import deque


def solve(n, m, k, uv_list):
    if k == 0:
        return ["Yes", "0", ""]
    if k % 2 == 1:
        return ["No"]
    g = [[] for _ in range(n + 1)]
    for i, (u, v) in enumerate(uv_list):
        g[u].append((v, i + 1))
        g[v].append((u, i + 1))
    parents = [-1] * (n + 1)
    edge_num = [-1] * (n + 1)
    bfs_list = []
    for i in range(1, n + 1):
        if parents[i] >= 0:
            continue
        parents[i] = 0
        bfs_list.append(i)
        queue = deque([i])
        while len(queue):
            p = queue.popleft()
            for q, r in g[p]:
                if parents[q] == -1:
                    parents[q] = p
                    edge_num[q] = r
                    bfs_list.append(q)
                    queue.append(q)
    # print(bfs_list)
    status = [0] * (n + 1)
    # print(parents)
    res = 0
    res_list = []
    for q in reversed(bfs_list):
        p = parents[q]
        if p <= 0:
            continue
        if status[q] == 0:
            res_list.append(edge_num[q])
            status[q] = 1
            status[p] = 1 - status[p]
            res += 2 * status[p]
        if res == k:
            break
    if res != k:
        return ["No"]
    else:
        # print(["Yes", str(len(res_list)), " ".join([str(r) for r in res_list])])
        return ["Yes", str(len(res_list)), " ".join([str(r) for r in res_list])]


def main():
    n, m, k = map(int, input().split())
    uv_list = [tuple(map(int, input().split())) for _ in range(m)]
    res = solve(n, m, k, uv_list)
    for r in res:
        print(r)


def test():
    assert solve(5, 5, 4, [(1, 2), (1, 3), (2, 4), (3, 5), (1, 5)]) == ["Yes", "2", "3 5"]
    assert solve(5, 5, 5, [(1, 2), (1, 3), (2, 4), (3, 5), (1, 5)]) == ["No"]
    assert solve(10, 10, 6, [
        (2, 5), (2, 6), (3, 5), (3, 8), (4, 6),
        (4, 8), (5, 9), (6, 7), (6, 10), (7, 9)
    ]) == ["Yes", "4", "4 9 8 5"]


if __name__ == "__main__":
    test()
    main()
