from collections import deque
import numpy as np


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


def solve(n, m, ab_list):
    res = 1

    g = [[] for _ in range(n + 1)]

    # union find
    uf = UnionFind(n)
    for a, b in ab_list:
        uf.union(a, b)
        g[a].append(b)
        g[b].append(a)

    par_list = [0] * (n + 1)
    for i in range(1, n + 1):
        par_list[i] = uf.find(i)

    calculated = [0] * (n + 1)
    for i in range(1, n + 1):
        if calculated[i]:
            continue
        cnt = 0
        for j in range(1, n + 1):
            if par_list[j] == par_list[i]:
                calculated[j] = 1
                cnt += 1
        # edge_list
        edge_list = [(p, q) for p, q in ab_list if par_list[p] == par_list[i]]
        color_list = - np.ones((2 ** (cnt - 1), n + 1), dtype=np.int8)
        ans_list = np.array([1] * (2 ** (cnt - 1)))
        visited = [0] * (n + 1)

        # initial
        visited[i] = 1
        d = 0
        color_list[:, i] = 0
        # for k in range(2 ** (cnt - 1)):
        #     color_list[k][i] = 0
        # edges
        queue = deque([i])
        while len(queue):
            p = queue.popleft()
            for q in g[p]:
                if visited[q]:
                    ans_list[color_list[:, p] == color_list[:, q]] = 0
                else:
                    color_list[:, q] = (color_list[:, p] + (np.arange(2 ** (cnt - 1)) >> d) % 2 + 1) % 3
                    d += 1
                    queue.append(q)
                    visited[q] = 1

        res *= 3 * ans_list.sum()

    return res


def main():
    n, m = map(int, input().split())
    ab_list = [tuple(map(int, input().split())) for _ in range(m)]
    res = solve(n, m, ab_list)
    print(res)


def test():
    assert solve(3, 3, [(1, 2), (2, 3), (3, 1)]) == 6
    assert solve(3, 0, []) == 27
    assert solve(4, 6, [(1, 2), (2, 3), (3, 4), (2, 4), (1, 3), (1, 4)]) == 0
    assert solve(20, 0, []) == 3486784401


if __name__ == "__main__":
    test()
    main()
