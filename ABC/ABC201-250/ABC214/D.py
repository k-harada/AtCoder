from heapq import heappop, heappush
from collections import deque


class UnionFind:

    def __init__(self, n):
        self.par = [i for i in range(n + 1)]
        self.rank = [0] * (n + 1)

    # search
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    # unite
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    # check
    def same_check(self, x, y):
        return self.find(x) == self.find(y)


def solve(n, uvw_list):
    h = []
    for u, v, w in uvw_list:
        heappush(h, (w, u, v))

    g = [[] for _ in range(n + 1)]
    for u, v, w in uvw_list:
        g[u].append(v)
        g[v].append(u)

    # tree from 1
    queue = deque()
    parent = [-1] * (n + 1)
    depth = [0] * (n + 1)
    parent[1] = 0
    queue.append(1)
    while len(queue):
        p = queue.popleft()
        for q in g[p]:
            if parent[q] == -1:
                parent[q] = p
                queue.append(q)
                depth[q] = depth[p] + 1

    uf = UnionFind(n)
    uf.rank = [-d for d in depth]

    weight = [1] * (n + 1)

    res = 0
    while len(h):
        w, u, v = heappop(h)
        pu = uf.find(u)
        pv = uf.find(v)
        res += w * weight[pu] * weight[pv]
        new_weight = weight[pu] + weight[pv]
        uf.union(u, v)
        weight[uf.find(u)] = new_weight

    return res


def main():
    n = int(input())
    uvw_list = [tuple(map(int, input().split())) for _ in range(n - 1)]
    res = solve(n, uvw_list)
    print(res)


def test():
    assert solve(3, [(1, 2, 10), (2, 3, 20)]) == 50
    assert solve(5, [(1, 2, 1), (2, 3, 2), (4, 2, 5), (3, 5, 14)]) == 76


if __name__ == "__main__":
    test()
    main()
