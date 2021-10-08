from collections import deque


def solve(n, ab_list):
    g = [[] for _ in range(n + 1)]
    for u, v in ab_list:
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
    res = 0

    dir_1_count = [1] * (n + 1)
    dir_1_length = [0] * (n + 1)

    depth_order = [(i, depth[i]) for i in range(1, n + 1)]
    depth_order_s = list(sorted(depth_order, key=lambda x: -x[1]))
    for p, _ in depth_order_s:
        q = parent[p]
        if q == -1:
            break
        res += dir_1_count[p] * (dir_1_length[q] + dir_1_count[q]) + dir_1_length[p] * dir_1_count[q]
        dir_1_count[q] += dir_1_count[p]
        dir_1_length[q] += dir_1_count[p] + dir_1_length[p]

        # print(dir_1_count)
        # print(dir_1_length)
        # print(res)

    return res


def main():
    n = int(input())
    ab_list = [tuple(map(int, input().split())) for _ in range(n - 1)]
    res = solve(n, ab_list)
    print(res)


def test():
    assert solve(2, [(1, 2)]) == 1
    assert solve(4, [(1, 2), (1, 3), (1, 4)]) == 9
    assert solve(12, [(1, 2), (3, 1), (4, 2), (2, 5), (3, 6), (3, 7), (8, 4), (4, 9), (10, 5), (11, 7), (7, 12)]) == 211


if __name__ == "__main__":
    test()
    main()
