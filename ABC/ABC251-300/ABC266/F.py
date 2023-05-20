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


def solve(n, uv_list, q, xy_list):
    # find loop
    g = [[] for _ in range(n + 1)]
    for u, v in uv_list:
        g[u].append(v)
        g[v].append(u)

    visited = [0] * (n + 1)
    parent = [0] * (n + 1)
    queue = deque([1])
    loop_start = 0
    loop_end = 0
    c = 0
    while len(queue):
        c += 1
        p = queue.pop()
        visited[p] = 1
        for q in g[p]:
            if q == parent[p]:
                continue
            if visited[q] == 1:
                loop_start = q
                loop_end = p
                break
            parent[q] = p
            queue.append(q)
        if loop_start != 0:
            break

    loop_member = [0] * (n + 1)
    p = loop_end
    loop_member[p] = 1
    while True:
        p = parent[p]
        loop_member[p] = 1
        if p == loop_start:
            break
    # print(loop_member)
    uf = UnionFind(n + 1)
    for u, v in uv_list:
        if loop_member[u] + loop_member[v] <= 1:
            uf.union(u, v)
    res = []
    for x, y in xy_list:
        if uf.same_check(x, y):
            res.append("Yes")
        else:
            res.append("No")

    return res


def main():
    n = int(input())
    uv_list = [tuple(map(int, input().split())) for _ in range(n)]
    q = int(input())
    xy_list = [tuple(map(int, input().split())) for _ in range(q)]
    res = solve(n, uv_list, q, xy_list)
    for r in res:
        print(r)


if __name__ == "__main__":
    main()
