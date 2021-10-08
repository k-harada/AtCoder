from collections import deque


def solve(n, uv_list):
    g = [[] for _ in range(n + 1)]
    for u, v in uv_list:
        g[u].append(v)
        g[v].append(u)

    # parent
    parent = [0] * (n + 1)
    parent[1] = -1
    depth = [-1] * (n + 1)
    depth[1] = 0
    leaf = [1] * (n + 1)
    leaf[0] = 0
    queue = deque([1])
    while len(queue):
        p = queue.popleft()
        for q in g[p]:
            if parent[q] == 0:
                parent[q] = p
                leaf[p] = 0
                depth[q] = depth[p] + 1
                queue.append(q)
    # print(parent)
    # print(leaf)

    # toward root
    dir_1_count = [1] * (n + 1)
    dir_1_length = [0] * (n + 1)

    depth_order = [(i, depth[i]) for i in range(1, n + 1)]
    depth_order_s = list(sorted(depth_order, key=lambda x: -x[1]))
    for p, _ in depth_order_s:
        q = parent[p]
        if q == -1:
            break
        dir_1_count[q] += dir_1_count[p]
        dir_1_length[q] += dir_1_count[p] + dir_1_length[p]

    # print(dir_1_count)
    # print(dir_1_length)

    # toward leaf
    dir_2_length = [0] * (n + 1)
    dir_2_length[1] = dir_1_length[1]
    visited = [0] * (n + 1)
    visited[1] = 1
    queue = deque([1])
    while len(queue):
        p = queue.popleft()
        for q in g[p]:
            if q == parent[p]:
                continue
            else:
                dir_2_length[q] = (dir_2_length[p] - dir_1_length[q] - dir_1_count[q]) + (n - dir_1_count[q]) + dir_1_length[q]
                queue.append(q)
    # print(dir_2_length)
    return dir_2_length[1:]


def main():
    n = int(input())
    uv_list = [tuple(map(int, input().split())) for _ in range(n - 1)]
    res = solve(n, uv_list)
    for r in res:
        print(r)


def test():
    assert solve(3, [(1, 2), (2, 3)]) == [3, 2, 3]
    assert solve(2, [(1, 2)]) == [1, 1]
    assert solve(6, [(1, 6), (1, 5), (1, 3), (1, 4), (1, 2)]) == [5, 9, 9, 9, 9, 9]


if __name__ == "__main__":
    test()
    main()
