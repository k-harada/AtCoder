from collections import deque


def solve(n, edge_list, q, query_list):
    res_list = [0] * (n + 1)

    # root 1
    graph_list = [[] for _ in range(n + 1)]
    for a, b in edge_list:
        graph_list[a].append(b)
        graph_list[b].append(a)

    parent_list = [0] * (n + 1)
    visited = [0] * (n + 1)
    visited[1] = 1
    queue = deque([1])
    while len(queue) > 0:
        a = queue.popleft()
        for b in graph_list[a]:
            if visited[b]:
                continue
            visited[b] = 1
            parent_list[b] = a
            queue.append(b)
    # print(parent_list)

    root = 0
    child_from = [0] * (n + 1)
    for t, e, x in query_list:
        if t == 1:
            a, b = edge_list[e - 1]
        else:
            b, a = edge_list[e - 1]
        if parent_list[a] == b:
            child_from[a] += x
        else:
            child_from[b] -= x
            root += x
    # print(root, child_from)
    res_list[1] = root
    queue = deque([1])
    visited = [0] * (n + 1)
    visited[1] = 1
    while len(queue) > 0:
        a = queue.popleft()
        for b in graph_list[a]:
            if visited[b]:
                continue
            visited[b] = 1
            res_list[b] = res_list[a] + child_from[b]
            queue.append(b)
    # print(res_list)
    return res_list[1:]


def main():
    n = int(input())
    edge_list = [tuple(map(int, input().split())) for _ in range(n - 1)]
    q = int(input())
    query_list = [tuple(map(int, input().split())) for _ in range(q)]
    res_list = solve(n, edge_list, q, query_list)
    for res in res_list:
        print(res)


def test():
    assert solve(5, [(1, 2), (2, 3), (2, 4), (4, 5)], 4, [(1, 1, 1), (1, 4, 10), (2, 1, 100), (2, 2, 1000)]) == [11, 110, 1110, 110, 100]
    assert solve(7, [(2, 1), (2, 3), (4, 2), (4, 5), (6, 1), (3, 7)], 7, [(2, 2, 1), (1, 3, 2), (2, 2, 4), (1, 6, 8), (1, 3, 16), (2, 4, 32), (2, 1, 64)]) == [72, 8, 13, 26, 58, 72, 5]


if __name__ == "__main__":
    test()
    main()
