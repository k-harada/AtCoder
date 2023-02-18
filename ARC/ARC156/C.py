from collections import deque


def solve(n, uv_list):
    g = [[] for _ in range(n + 1)]
    for u, v in uv_list:
        g[u].append(v)
        g[v].append(u)
    # 1で試す
    parents = [0] * (n + 1)
    dfs_tour = []
    queue = deque([1])
    while len(queue):
        p = queue.pop()
        dfs_tour.append(p)
        for q in g[p]:
            if q == parents[p]:
                continue
            else:
                parents[q] = p
                queue.append(q)

    count_child = [1] * (n + 1)
    for q in reversed(dfs_tour):
        p = parents[q]
        count_child[p] += count_child[q]
    # print(count_child)

    # nが偶数で単純な線の場合
    if max([len(g[i]) for i in range(1, n + 1)]) == 2 and n % 2 == 0:
        s = 1
        for i in range(1, n + 1):
            if len(g[i]) == 1:
                s = i
                break
        queue = deque([s])
        visited = [0] * (n + 1)
        tour = [s]
        while len(queue):
            p = queue.pop()
            visited[p] = 1
            for q in g[p]:
                if visited[q] == 1:
                    pass
                else:
                    queue.append(q)
                    tour.append(q)
        # print(tour)
        res = [0] * (n + 1)
        for i in range(n):
            res[tour[i]] = tour[-(i + 1)]
        return " ".join([str(p) for p in res[1:]])
    # バランスの良い親を探す
    the_parent = 1
    while True:
        break_flag = True
        for q in g[the_parent]:
            if count_child[q] > (n - 1) // 2:
                count_child[the_parent] = 0
                the_parent = q
                break_flag = False
        if break_flag:
            break
    # print(the_parent)

    # もう一回dfs
    parents = [0] * (n + 1)
    dfs_tour = []
    queue = deque([the_parent])
    while len(queue):
        p = queue.pop()
        dfs_tour.append(p)
        for q in g[p]:
            if q == parents[p]:
                continue
            else:
                parents[q] = p
                queue.append(q)
    count_child = [1] * (n + 1)
    for q in reversed(dfs_tour):
        p = parents[q]
        count_child[p] += count_child[q]
    even = False
    second = -1
    for q in g[the_parent]:
        assert count_child[q] <= n // 2
        if count_child[q] > (n - 1) // 2:
            even = True
            second = q
    if even == False:
        res = [0] * (n + 1)
        res[the_parent] = the_parent
        for i in range(n - 1):
            res[dfs_tour[1:][i]] = dfs_tour[1:][(i + (n - 1) // 2) % (n - 1)]
        # print(res)
        return " ".join([str(p) for p in res[1:]])
    else:
        parents = [0] * (n + 1)
        dfs_tour_1 = []
        queue = deque([the_parent])
        while len(queue):
            p = queue.pop()
            dfs_tour_1.append(p)
            for q in g[p]:
                if q == parents[p]:
                    continue
                elif q == second:
                    continue
                else:
                    parents[q] = p
                    queue.append(q)


        dfs_tour_2 = []
        queue = deque([second])
        while len(queue):
            p = queue.pop()
            dfs_tour_2.append(p)
            for q in g[p]:
                if q == parents[p]:
                    continue
                elif q == the_parent:
                    continue
                else:
                    parents[q] = p
                    queue.append(q)

        res = [0] * (n + 1)
        for p, q in zip(dfs_tour_1, dfs_tour_2):
            res[p] = q
            res[q] = p
        return " ".join([str(p) for p in res[1:]])


def main():
    n = int(input())
    uv_list = [tuple(map(int, input().split())) for _ in range(n - 1)]
    res = solve(n, uv_list)
    print(res)


def test():
    assert solve(3, [(1, 2), (2, 3)]) == "3 2 1"
    assert solve(4, [(2, 1), (2, 3), (2, 4)]) == "3 2 4 1"


if __name__ == "__main__":
    # test()
    main()
