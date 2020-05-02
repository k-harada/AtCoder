from bisect import bisect_left


def solve(n, a_list, uv_list):
    res = [0] * n
    tree = [[] for _ in range(n)]
    for u, v in uv_list:
        tree[u - 1].append(v - 1)
        tree[v - 1].append(u - 1)

    # euler tour
    visited = [0] * n
    parent = [-1] * n
    tour = [0]
    p = 0
    while True:
        visited[p] = 1
        r = parent[p]
        while len(tree[p]):
            q = tree[p].pop()
            if visited[q] == 0:
                parent[q] = p
                r = q
                break
        if r == -1:
            break
        p = r
        tour.append(p)
    # assert len(tour) == 2 * n - 1
    # print(tour)

    # tree DP
    dp = [10 ** 9 + i for i in range(n + 1)]
    dp[0] = 0
    re_visited = [0] * n
    callbacks = []
    for p in tour:
        if re_visited[p] == 0:
            re_visited[p] = 1
            ind = bisect_left(dp, a_list[p])
            callbacks.append((ind, dp[ind]))
            dp[ind] = a_list[p]
            res[p] = bisect_left(dp, 10 ** 9) - 1
        else:
            ind, v = callbacks.pop()
            dp[ind] = v
        # print(dp)
    # print(res)
    return res


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    uv_list = [list(map(int, input().split())) for _ in range(n - 1)]
    res = solve(n, a_list, uv_list)
    for r in res:
        print(r)


def test():
    assert solve(10, [1, 2, 5, 3, 4, 6, 7, 3, 2, 4],
                 [[1, 2], [2, 3], [3, 4], [4, 5], [3, 6], [6, 7], [1, 8], [8, 9], [9, 10]]
                 ) == [1, 2, 3, 3, 4, 4, 5, 2, 2, 3]
    assert solve(10, [5, 2, 5, 3, 4, 6, 7, 3, 2, 4],
                 [[1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]]
                 ) == [1, 1, 1, 1, 1, 2, 2, 1, 1, 1]
    assert solve(10, [5, 2, 5, 3, 4, 6, 7, 3, 2, 4],
                 [[1, 2], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [2, 8], [2, 9], [2, 10]]
                 ) == [1, 1, 2, 2, 2, 2, 2, 2, 1, 2]
    assert solve(10, [3, 5, 5, 3, 4, 6, 7, 3, 2, 4],
                 [[1, 2], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [2, 8], [2, 9], [2, 10]]
                 ) == [1, 2, 2, 2, 2, 3, 3, 2, 2, 2]
    assert solve(10, [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
                 [[1, 2], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [2, 8], [2, 9], [2, 10]]
                 ) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]


if __name__ == "__main__":
    test()
    main()
