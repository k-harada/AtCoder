from collections import deque


def solve(n, uv_list):
    g = [[] for _ in range(n + 1)]
    for u, v in uv_list:
        g[u].append(v)
        g[v].append(u)

    # 親子を定義する
    # ついでにEuler Tourしてleafを順に追加する
    leaves = []
    parent = [0] * (n + 1)
    visited = [0] * (n + 1)
    visited[1] = 1
    queue = deque([1])
    visit_order = []
    while len(queue):
        p = queue.pop()
        visit_order.append(p)
        c = 0
        for q in g[p]:
            if visited[q] == 0:
                parent[q] = p
                visited[q] = 1
                queue.append(q)
                c += 1
        if c == 0:
            leaves.append(p)

    l_list = [n + 1] * (n + 1)
    r_list = [0] * (n + 1)

    for i, a in enumerate(leaves):
        l_list[a] = i + 1
        r_list[a] = i + 1

    for q in reversed(visit_order):
        p = parent[q]
        l_list[p] = min(l_list[p], l_list[q])
        r_list[p] = max(r_list[p], r_list[q])

    res = []
    for i in range(1, n + 1):
        res.append(str(l_list[i]) + " " + str(r_list[i]))
    return res


def main():
    n = int(input())
    uv_list = [tuple(map(int, input().split())) for _ in range(n - 1)]
    res = solve(n, uv_list)
    for r in res:
        print(r)


def test():
    assert solve(3, [(2, 1), (3, 1)]) == ["1 2", "2 2", "1 1"]
    assert solve(5, [(3, 4), (5, 4), (1, 2), (1, 4)]) == ["1 3", "3 3", "2 2", "1 2", "1 1"]
    assert solve(5, [(4, 5), (3, 2), (5, 2), (3, 1)]) == ["1 1", "1 1", "1 1", "1 1", "1 1"]


if __name__ == "__main__":
    # test()
    main()
