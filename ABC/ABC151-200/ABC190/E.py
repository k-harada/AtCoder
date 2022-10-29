from collections import deque


LARGE = 10 ** 9 + 7


def solve(n, m, ab_list, k, c_list):
    g = [[] for _ in range(n + 1)]
    for a, b in ab_list:
        g[a].append(b)
        g[b].append(a)
    d_list = [[LARGE] * k for _ in range(k)]
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

    # TSP
    dp0 = [[LARGE] * k for _ in range(2 ** k)]
    dp1 = [[LARGE] * k for _ in range(2 ** k)]
    for i in range(k):
        dp0[2 ** i][i] = 1

    for t in range(k - 1):
        if t % 2 == 0:
            for i in range(2 ** k):
                for p in range(k):
                    for q in range(k):
                        dp1[i | (2 ** q)][q] = min(dp1[i | (2 ** q)][q], dp0[i][p] + d_list[p][q])
        else:
            for i in range(2 ** k):
                for p in range(k):
                    for q in range(k):
                        dp0[i | (2 ** q)][q] = min(dp0[i | (2 ** q)][q], dp1[i][p] + d_list[p][q])
    if k % 2 == 0:
        res = min(dp1[2 ** k - 1])
    else:
        res = min(dp0[2 ** k - 1])
    if res >= LARGE:
        res = -1
    return res


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
