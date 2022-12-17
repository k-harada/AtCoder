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


def solve(n, m, uv_list):
    g = [[] for _ in range(n + 1)]
    uf = UnionFind(n)
    for u, v in uv_list:
        g[u].append(v)
        g[v].append(u)
        uf.union(u, v)

    # 適当に２部グラフにする
    seg_01 = [-1] * (n + 1)
    failure = False
    for i in range(n + 1):
        if seg_01[i] != -1:
            continue
        seg_01[i] = 0
        queue = deque([i])
        while len(queue):
            p = queue.popleft()
            for q in g[p]:
                if seg_01[q] == -1:
                    seg_01[q] = 1 - seg_01[p]
                    queue.append(q)
                elif seg_01[q] == seg_01[p]:
                    failure = True
    # print(seg_01)
    if failure:
        return 0

    cnt_0 = [0] * (n + 1)
    cnt_1 = [0] * (n + 1)
    for i in range(1, n + 1):
        p = uf.find(i)
        if seg_01[i] == 0:
            cnt_0[p] += 1
        else:
            cnt_1[p] += 1

    res = 0
    for i in range(1, n + 1):
        p = uf.find(i)
        if seg_01[i] == 0:
            res += n - (cnt_0[p] + len(g[i]))
        else:
            res += n - (cnt_1[p] + len(g[i]))
    # print(res)
    return res // 2


def main():
    n, m = map(int, input().split())
    uv_list = [tuple(map(int, input().split())) for _ in range(m)]
    res = solve(n, m, uv_list)
    print(res)


def test():
    assert solve(5, 4, [(4, 2), (3, 1), (5, 2), (3, 2)]) == 2
    assert solve(4, 3, [(3, 1), (3, 2), (1, 2)]) == 0


if __name__ == "__main__":
    test()
    main()
