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


def solve(n, m, q, abc_list, xy_list):
    uf = UnionFind(n + 1)
    for a, b, c in abc_list:
        uf.union(a, b)
    p_list = [uf.find(i) for i in range(n + 1)]
    p_list = [uf.find(i) for i in range(n + 1)]

    g = [[] for _ in range(n + 1)]
    for a, b, c in abc_list:
        g[a].append((b, c))
        g[b].append((a, -c))
    potential = [-10 ** 15] * (n + 1)
    visited = [0] * (n + 1)
    loop_st = [0] * (n + 1)
    for st in range(1, n + 1):
        if visited[st]:
            continue
        queue = deque([st])
        potential[st] = 0
        visited[st] = 1
        loop = 0
        while len(queue):
            p = queue.popleft()
            for q, c in g[p]:
                if visited[q] == 0:
                    potential[q] = potential[p] + c
                    visited[q] = 1
                    queue.append(q)
                else:
                    if potential[q] == potential[p] + c:
                        pass
                    else:
                        loop = 1
                        break
            if loop == 1:
                break
        if loop == 1:
            loop_st[p_list[st]] = 1

    res = []
    for x, y in xy_list:
        if uf.same_check(x, y):
            if loop_st[p_list[x]] == 1:
                res.append("inf")
            else:
                res.append(str(potential[y] - potential[x]))
        else:
            res.append("nan")

    return res


def main():
    n, m, q = map(int, input().split())
    abc_list = [tuple(map(int, input().split())) for _ in range(m)]
    xy_list = [tuple(map(int, input().split())) for _ in range(q)]
    res = solve(n, m, q, abc_list, xy_list)
    for r in res:
        print(r)


if __name__ == "__main__":
    main()
