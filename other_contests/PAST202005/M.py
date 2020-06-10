from collections import deque


def solve(n, m, uv_list, s, k, t_list):

    # original graph
    g = [[] for _ in range(n)]
    for u, v in uv_list:
        g[u - 1].append(v - 1)
        g[v - 1].append(u - 1)

    # degenerated graph
    g_d = [[0] * (k + 1) for _ in range(k + 1)]

    # start from s
    queue = deque([s - 1])
    dist = [10 ** 6] * n
    dist[s - 1] = 0
    while len(queue) > 0:
        p = queue.popleft()
        for q in g[p]:
            if dist[q] > dist[p] + 1:
                dist[q] = dist[p] + 1
                queue.append(q)
    for j in range(k):
        g_d[0][j + 1] = dist[t_list[j] - 1]
        g_d[j + 1][0] = dist[t_list[j] - 1]

    for i in range(k):
        # start from t_k
        queue = deque([t_list[i] - 1])
        dist = [10 ** 6] * n
        dist[t_list[i] - 1] = 0
        while len(queue) > 0:
            p = queue.popleft()
            for q in g[p]:
                if dist[q] > dist[p] + 1:
                    dist[q] = dist[p] + 1
                    queue.append(q)
        for j in range(k):
            g_d[i + 1][j + 1] = dist[t_list[j] - 1]

    # visit all
    table = [[10 ** 7] * 2 ** k for _ in range(k + 1)]
    table[0][0] = 0
    queue = deque([(0, 0)])
    while len(queue) > 0:
        p, stage = queue.popleft()
        cost_old = table[p][stage]
        for q in range(1, k + 1):
            cost_new = cost_old + g_d[p][q]
            stage_new = stage | 2 ** (q - 1)
            if table[q][stage_new] > cost_new:
                table[q][stage_new] = cost_new
                queue.append((q, stage_new))

    res = min([tab[-1] for tab in table])
    return res


def main():
    n, m = map(int, input().split())
    uv_list = [list(map(int, input().split())) for _ in range(m)]
    s = int(input())
    k = int(input())
    t_list = list(map(int, input().split()))
    res = solve(n, m, uv_list, s, k, t_list)
    print(res)


def test():
    assert solve(3, 2, [[1, 2], [2, 3]], 2, 2, [1, 3]) == 3
    assert solve(5, 5, [[1, 2], [1, 3], [1, 4], [1, 5], [2, 3]], 1, 3, [2, 3, 5]) == 4


if __name__ == "__main__":
    test()
    main()
