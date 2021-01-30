from collections import deque


LARGE = 10 ** 9 + 7


def solve(n, m, ab_list, k, c_list):
    g = [[] for _ in range(n + 1)]
    for a, b in ab_list:
        g[a].append(b)
        g[b].append(a)
    d_list = [[LARGE] * (k + 1) for _ in range(k + 1)]
    # BFS
    for i in range(k):
        st = c_list[i]
        dist = [LARGE] * (n + 1)
        dist[st] = 0
        queue = deque([st])
        while len(queue):
            p = queue.popleft()
            for q in g[p]:
                if dist[q] > dist[p] + 1:
                    dist[q] = dist[p] + 1
                    queue.append(q)
        for j in range(k):
            d_list[i][j] = dist[c_list[j]]
    # print(d_list)
    for i in range(k):
        d_list[k][i] = 1
    dp = [[LARGE] * (k + 1) for _ in range(2 ** k)]

    # TSP
    def dfs(s, v, dp):
        if dp[s][v] != LARGE:  # 訪問済みならメモを返す
            return dp[s][v]
        if s == 2 ** k - 1:  # 全ての頂点を訪れて頂点0に戻ってきた
            return 0  # もう動く必要はない
        res = 10 ** 9 + 7
        for u in range(k):
            if s >> u & 1 == 0 and d_list[v][u] < LARGE:  # 未訪問かどうか
                res = min(res, dfs(s | 1 << u, u, dp) + d_list[v][u])
        dp[s][v] = res
        return res
    res_min = dfs(0, k, dp)
    # print(res_min)
    if res_min >= LARGE:
        return -1
    else:
        return res_min


def main():
    n, m = map(int, input().split())
    ab_list = [tuple(map(int, input().split())) for _ in range(m)]
    k = int(input())
    c_list = list(map(int, input().split()))
    res = solve(n, m, ab_list, k, c_list)
    print(res)


def test():
    assert solve(4, 3, [(1, 4), (2, 4), (3, 4)], 3, [1, 2, 3]) == 5
    assert solve(4, 3, [(1, 4), (2, 4), (1, 2)], 3, [1, 2, 3]) == -1


if __name__ == "__main__":
    test()
    main()
