from collections import deque


MOD = 998244353


def solve(n, m, k, a_list, uv_list):
    g = [[] for _ in range(n + 1)]
    for u, v in uv_list:
        g[u].append(v)
        g[v].append(u)

    # root 1
    queue = deque([1])
    depth = [0] * (n + 1)
    parent = [0] * (n + 1)
    parent[1] = -1
    while len(queue):
        p = queue.popleft()
        for q in g[p]:
            if parent[q] == 0:
                parent[q] = p
                depth[q] = depth[p] + 1
                queue.append(q)
    # print(parent)
    # print(depth)
    count = [0] * (n + 1)
    for i in range(m - 1):
        a = a_list[i]
        b = a_list[i + 1]
        while depth[a] > depth[b]:
            count[a] += 1
            a = parent[a]
        while depth[a] < depth[b]:
            count[b] += 1
            b = parent[b]
        while a != b:
            count[a] += 1
            count[b] += 1
            a = parent[a]
            b = parent[b]

    # print(count)
    # print(max(count))
    dp = [[0] * 100001 for _ in range(n)]
    dp[0][0] = 1
    for i in range(n - 1):
        for j in range(100 * i + 1):
            if dp[i][j] > 0:
                dp[i + 1][j] += dp[i][j]
                dp[i + 1][j] %= MOD
                dp[i + 1][j + count[i + 2]] += dp[i][j]
                dp[i + 1][j + count[i + 2]] %= MOD
        # print(dp[i][99950:100050])
    d = sum(count) - k
    if d % 2 == 1:
        return 0
    else:
        return dp[-1][d // 2]


def main():
    n, m, k = map(int, input().split())
    a_list = list(map(int, input().split()))
    uv_list = [tuple(map(int, input().split())) for _ in range(n - 1)]
    res = solve(n, m, k, a_list, uv_list)
    print(res)


def test():
    assert solve(4, 5, 0, [2, 3, 2, 1, 4], [(1, 2), (2, 3), (3, 4)]) == 2
    assert solve(3, 10, 10000, [1, 2, 1, 2, 1, 2, 2, 1, 1, 2], [(1, 2), (1, 3)]) == 0
    assert solve(10, 2, -1, [1, 10], [
        (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10)
    ]) == 126
    assert solve(5, 8, -1, [1, 4, 1, 4, 2, 1, 3, 5], [(1, 2), (4, 1), (3, 1), (1, 5)]) == 2


def test_large():
    print(solve(1000, 100, 0, [1, 1000] * 500, [(i, i + 1) for i in range(1, 1000)]))


if __name__ == "__main__":
    test()
    # test_large()
    main()
