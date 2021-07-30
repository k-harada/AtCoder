def solve(n, ab_list, q, kv_list):
    # graph
    g = [[] for _ in range(n + 1)]
    for a, b in ab_list:
        g[a].append(b)
        g[b].append(a)

    # parent
    parent = [[0] * (n + 1) for _ in range(18)]
    depth = [0] * (n + 1)
    depth[0] = -1
    # dfs search
    visited = [0] * (n + 1)
    visited[0] = n + 1
    order = 0
    queue = [1]
    while len(queue):
        p = queue.pop()
        order += 1
        visited[p] = order
        for q in g[p]:
            if visited[q] == 0:
                parent[0][q] = p
                depth[q] = depth[p] + 1
                queue.append(q)

    # print(visited)
    # print(parent[0])
    # print(depth)

    # parent 2 ** i
    for i in range(17):
        for p in range(n + 1):
            parent[i + 1][p] = parent[i][parent[i][p]]
    # print(parent)

    def get_n_parent(node, k):
        p_ = node
        k_ = k
        n_ = 0
        while k_ > 0:
            if k_ & 1:
                p_ = parent[n_][p_]
            k_ = k_ >> 1
            n_ += 1
        return p_

    def get_common_parent(node_p, node_q):

        node_p_ = node_p
        node_q_ = node_q
        depth_diff = depth[node_q_] - depth[node_p_]
        if depth_diff > 0:
            node_q_ = get_n_parent(node_q_, depth_diff)
        elif depth_diff < 0:
            node_p_ = get_n_parent(node_p_, -depth_diff)

        # avoid 0, 1
        if node_p_ == node_q_:
            return node_q_
        elif parent[0][node_p_] == parent[0][node_q_]:
            return parent[0][node_p_]

        # bin
        left = 0
        right = depth[node_p_]
        while left < right - 1:
            middle = (left + right) // 2
            if get_n_parent(node_p_, middle) == get_n_parent(node_q_, middle):
                right = middle
            else:
                left = middle

        return get_n_parent(node_p_, right)

    res = []
    for kv in kv_list:
        k = kv[0]
        node_list = [(kv[i + 1], visited[kv[i + 1]]) for i in range(k)]
        node_list_s = list(sorted(node_list, key=lambda x: x[1]))
        p = node_list_s[0][0]
        depth_min = depth[p]
        s = 0
        for i in range(1, k):
            q = node_list_s[i][0]
            r = get_common_parent(p, q)
            s += depth[q] - depth[r]
            if depth_min > depth[r]:
                s += depth_min - depth[r]
                depth_min = depth[r]
            p = q
        res.append(s)
    # print(res)
    return res


def main():
    n = int(input())
    ab_list = [tuple(map(int, input().split())) for _ in range(n - 1)]
    q = int(input())
    kv_list = [tuple(map(int, input().split())) for _ in range(q)]
    res = solve(n, ab_list, q, kv_list)
    for r in res:
        print(r)


def test():
    assert solve(6, [(1, 2), (2, 3), (3, 4), (1, 5), (3, 6)], 5,
                 [(2, 1, 2), (3, 1, 3, 5), (4, 2, 3, 4, 5), (5, 1, 2, 3, 5, 6), (6, 1, 2, 3, 4, 5, 6)]
                 ) == [1, 3, 4, 4, 5]
    assert solve(6, [(1, 2), (2, 3), (3, 4), (1, 5), (3, 6)], 5,
                 [(2, 1, 2), (2, 3, 4), (2, 4, 6), (2, 1, 5), (2, 2, 5)]
                 ) == [1, 1, 2, 1, 2]
    assert solve(6, [(1, 2), (2, 3), (3, 4), (1, 5), (3, 6)], 5,
                 [(3, 1, 2, 3), (3, 1, 2, 5), (3, 1, 3, 6), (3, 3, 4, 5), (3, 4, 5, 6)]
                 ) == [2, 2, 3, 4, 5]


if __name__ == "__main__":
    test()
    main()
