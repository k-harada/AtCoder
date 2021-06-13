from collections import deque


class Dinic:
    def __init__(self, n):
        self.n = n
        self.g = [[] for i in range(n)]
        self.level = [None] * n
        self.it = None

    def add_edge(self, fr, to, cap):
        forward = [to, cap, None]
        forward[2] = backward = [fr, 0, forward]
        self.g[fr].append(forward)
        self.g[to].append(backward)

    def add_multi_edge(self, v1, v2, cap1, cap2):
        edge1 = [v2, cap1, None]
        edge1[2] = edge2 = [v1, cap2, edge1]
        self.g[v1].append(edge1)
        self.g[v2].append(edge2)

    def bfs(self, s, t):
        self.level = level = [None] * self.n
        deq = deque([s])
        level[s] = 0
        g = self.g
        while deq:
            v = deq.popleft()
            lv = level[v] + 1
            for w, cap, _ in g[v]:
                if cap and level[w] is None:
                    level[w] = lv
                    deq.append(w)
        return level[t] is not None

    def dfs(self, v, t, f):
        if v == t:
            return f
        level = self.level
        for e in self.it[v]:
            w, cap, rev = e
            if cap and level[v] < level[w]:
                d = self.dfs(w, t, min(f, cap))
                if d:
                    e[1] -= d
                    rev[1] += d
                    return d
        return 0

    def flow(self, s, t):
        flow = 0
        inf = 10 ** 9 + 7
        g = self.g
        while self.bfs(s, t):
            *self.it, = map(iter, self.g)
            f = inf
            while f:
                f = self.dfs(s, t, inf)
                flow += f
        return flow


def solve(h, w, n, abcd_list):
    flow = Dinic(h + w + 2 * n + 2)
    # 0: src
    # 1: dst
    # src -> row
    for i in range(h):
        flow.add_edge(0, i + 2, 1)
    # row -> piece
    for k in range(n):
        a, b, c, d = abcd_list[k]
        for i in range(a - 1, c):
            flow.add_edge(i + 2, h + w + 2 + k, 1)
    # piece -> piece
    for k in range(n):
        flow.add_edge(h + w + 2 + k, h + w + 2 + n + k, 1)
    # piece -> col
    for k in range(n):
        a, b, c, d = abcd_list[k]
        for j in range(b - 1, d):
            flow.add_edge(h + w + 2 + n + k, j + h + 2, 1)
    # col -> dst
    for j in range(w):
        flow.add_edge(j + h + 2, 1, 1)

    res = flow.flow(0, 1)
    return res


def main():
    h, w, n = map(int, input().split())
    abcd_list = [tuple(map(int, input().split())) for _ in range(n)]
    res = solve(h, w, n, abcd_list)
    print(res)


def test():
    assert solve(2, 3, 3, [(1, 1, 2, 2), (1, 2, 2, 3), (1, 1, 1, 3)]) == 2
    assert solve(5, 5, 3, [(1, 1, 5, 5), (1, 1, 4, 4), (2, 2, 3, 3)]) == 3


if __name__ == "__main__":
    test()
    main()