from collections import deque


def solve(n, k, uv_list):
    if k < n:
        return ["No"]
    g = [[] for _ in range(n + 1)]
    for u, v in uv_list:
        g[u].append(v)
        g[v].append(u)
    parents = [-1] * (n + 1)
    length_list = [0] * (n + 1)
    parents[1] = 0
    length_list[1] = 1
    queue = deque([1])
    bfs_order = []
    while len(queue):
        p = queue.popleft()
        bfs_order.append(p)
        for q in sorted(g[p]):
            if parents[q] == -1:
                parents[q] = p
                queue.append(q)
    # print(parents)
    # print(bfs_order)
    count_list = [1] * (n + 1)
    count_list[0] = 0
    for q in reversed(bfs_order):
        p = parents[q]
        if p > 0:
            count_list[p] += count_list[q]
    # print(count_list)
    if sum(count_list) < k:
        return ["No"]
    else:
        r = sum(count_list) - k
    reverse_flag = [0] * (n + 1)
    ic_list = [(i, count_list[i]) for i in range(1, n + 1)]
    ic_list_s = list(sorted(ic_list, key=lambda x: -x[1]))
    for i, c in ic_list_s:
        if r >= count_list[i] and i != 1:
            r -= count_list[i]
            count_list[i] = 0
            reverse_flag[i] = 1
    # print(reverse_flag)
    # print(r)
    no = 1
    res = [0] * (n + 1)
    for p in reversed(bfs_order):
        if reverse_flag[p]:
            res[p] = no
            no += 1
    for p in bfs_order:
        if reverse_flag[p] == 0:
            res[p] = no
            no += 1
    # print(res)
    return ["Yes", " ".join([str(r) for r in res[1:]])]


def main():
    n, k = map(int, input().split())
    uv_list = [tuple(map(int, input().split())) for _ in range(n - 1)]
    res = solve(n, k, uv_list)
    for r in res:
        print(r)


def test():
    assert solve(5, 8, [(1, 2), (2, 3), (2, 4), (4, 5)]) == ["Yes", "3 2 1 4 5"]
    assert solve(7, 21, [(2, 1), (7, 2), (5, 1), (3, 7), (2, 6), (3, 4)]) == ["No"]
    assert solve(8, 20, [(3, 1), (3, 8), (7, 1), (7, 5), (3, 2), (6, 5), (4, 7)]) == ["Yes", "2 1 3 6 7 8 4 5"]


if __name__ == "__main__":
    test()
    main()
