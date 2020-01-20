from collections import deque


def solve(n, edge_list, m, cond_list):

    g = [[] for _ in range(n)]

    for a, b in edge_list:
        g[a - 1].append(b - 1)
        g[b - 1].append(a - 1)

    cond_mat = [[0] * m for _ in range(n - 1)]

    for i in range(m):
        u, v = cond_list[i]
        parent_list = [-1] * n
        p = u - 1
        parent_list[p] = p
        queue = deque([p])
        while len(queue) > 0:
            p = queue.popleft()
            for q in g[p]:
                if parent_list[q] == -1:
                    parent_list[q] = p
                    queue.append(q)
        q = v - 1
        p = parent_list[q]
        while q != u - 1:
            if (p + 1, q + 1) in edge_list:
                k = edge_list.index((p + 1, q + 1))
            else:
                k = edge_list.index((q + 1, p + 1))
            cond_mat[k][i] = 1
            p, q = parent_list[p], parent_list[q]

    # cond_vec
    cond_vec = [0] * (n - 1)
    for k in range(n - 1):
        for i in range(m):
            cond_vec[k] += cond_mat[k][i] * (2 ** i)
    # print(cond_vec)
    # bit DP
    dp = [[0] * (2 ** m) for _ in range(n)]
    dp[0][0] = 1
    for k in range(n - 1):
        for i in range(2 ** m):
            dp[k + 1][i] += dp[k][i]
            dp[k + 1][i | cond_vec[k]] += dp[k][i]
    # print(dp)
    return dp[-1][-1]


def main():
    n = int(input())
    edge_list = []
    for _ in range(n - 1):
        a, b = map(int, input().split())
        edge_list.append((a, b))
    m = int(input())
    cond_list = []
    for _ in range(m):
        u, v = map(int, input().split())
        cond_list.append((u, v))
    res = solve(n, edge_list, m, cond_list)
    print(res)


def test():
    assert solve(3, [(1, 2), (2, 3)], 1, [(1, 3)]) == 3
    assert solve(2, [(1, 2)], 1, [(1, 2)]) == 1
    assert solve(5, [(1, 2), (3, 2), (3, 4), (5, 3)], 3, [(1, 3), (2, 4), (2, 5)]) == 9


if __name__ == "__main__":
    test()
    main()
