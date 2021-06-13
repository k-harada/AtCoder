# Dinic's algorithm
# https://tjkendev.github.io/procon-library/python/max_flow/dinic.html
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
