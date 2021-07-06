import sys
sys.setrecursionlimit(10000000)


def solve(n, m, ab_list):
    g = [[] for _ in range(n + 1)]
    g_rev = [[] for _ in range(n + 1)]
    for a, b in ab_list:
        g[a].append(b)
        g_rev[b].append(a)

    label = [0] * (n + 1)
    visited = [0] * (n + 1)
    order = []

    def dfs(s):
        visited[s] = 1
        for t in g[s]:
            if not visited[t]:
                dfs(t)
        order.append(s)

    def rev_dfs(s, c):
        label[s] = c
        for t in g_rev[s]:
            if not label[t]:
                rev_dfs(t, c)

    for i in range(1, n + 1):
        if visited[i] == 0:
            dfs(i)

    for p in reversed(order):
        if label[p] == 0:
            rev_dfs(p, p)

    res = 0
    count = [0] * (n + 1)
    for i in range(1, n + 1):
        count[label[i]] += 1
    for i in range(1, n + 1):
        res += count[i] * (count[i] - 1) // 2
    # print(label)
    # print(count)
    return res


def main():
    n, m = map(int, input().split())
    ab_list = [tuple(map(int, input().split())) for _ in range(m)]
    res = solve(n, m, ab_list)
    print(res)


def test():
    assert solve(4, 7, [(1, 2), (2, 1), (2, 3), (4, 3), (4, 1), (1, 4), (2, 3)]) == 3
    assert solve(100, 1, [(1, 2)]) == 0


if __name__ == "__main__":
    test()
    main()
