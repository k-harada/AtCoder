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


def solve(n, m, uvc_list):
    uf = UnionFind(n)
    g = [[] for _ in range(n + 1)]

    # make tree
    color_used = [0] * (n + 1)
    for u, v, c in uvc_list:
        if uf.same_check(u, v):
            continue
        uf.union(u, v)
        g[u].append((v, c))
        g[v].append((u, c))
        color_used[c] = 1

    color_not_used = 0
    for i in range(1, n + 1):
        if color_used[i] == 0:
            color_not_used = i
            break

    # root 1
    queue = deque([1])
    c_list = [color_not_used] * (n + 1)
    checked = [0] * (n + 1)
    checked[1] = 1
    while len(queue) > 0:
        p = queue.popleft()
        for q, c in g[p]:
            if checked[q]:
                continue
            if c_list[p] != c:
                c_list[q] = c
            checked[q] = 1
            queue.append(q)

    # print(c_list)
    return c_list[1:]


def main():
    n, m = map(int, input().split())
    uvc_list = [tuple(map(int, input().split())) for _ in range(m)]
    res = solve(n, m, uvc_list)
    for r in res:
        print(r)


def test():
    assert solve(3, 4, [(1, 2, 1), (2, 3, 2), (3, 1, 3), (1, 3, 1)]) == [3, 1, 2]


if __name__ == "__main__":
    test()
    main()
