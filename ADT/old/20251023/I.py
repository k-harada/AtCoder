from collections import deque


def solve(n, m, uv_list):
    res = []
    g = [[] for _ in range(n + 1)]
    for u, v in uv_list:
        g[u].append(v)
        g[v].append(u)

    # DFS
    visited = [0] * (n + 1)
    parents = [0] * (n + 1)
    queue = deque([1])
    while len(queue):
        p = queue.pop()
        if visited[p]:
            continue
        visited[p] = 1
        if p > 1:
            res.append(f"{parents[p]} {p}")
        for q in g[p]:
            if visited[q] == 0:
                queue.append(q)
                parents[q] = p
    # print(res)
    # BFS
    visited = [0] * (n + 1)
    parents = [0] * (n + 1)
    queue = deque([1])
    while len(queue):
        p = queue.popleft()
        if visited[p]:
            continue
        visited[p] = 1
        if p > 1:
            res.append(f"{parents[p]} {p}")
        for q in g[p]:
            if visited[q] == 0:
                queue.append(q)
                if parents[q] == 0:
                    parents[q] = p
    # print(res)
    return res


def main():
    n, m = map(int, input().split())
    uv_list = [tuple(map(int, input().split())) for _ in range(m)]
    res = solve(n, m, uv_list)
    for r in res:
        print(r)


def test():
    assert solve(6, 8, [
        (5, 1),
        (4, 3),
        (1, 4),
        (3, 5),
        (1, 2),
        (2, 6),
        (1, 6),
        (4, 2)
    ]) == ['1 6', '6 2', '2 4', '4 3', '3 5', '1 5', '1 4', '1 2', '1 6', '5 3']
    assert solve(4, 3, [
        (3, 1),
        (1, 2),
        (1, 4)
    ]) == ['1 4', '1 2', '1 3', '1 3', '1 2', '1 4']


if __name__ == "__main__":
    test()
    main()
