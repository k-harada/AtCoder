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
    if m != n - 1:
        return "No"
    degree = [0] * (n + 1)
    for u, v in uv_list:
        degree[u] += 1
        degree[v] += 1
    if max(degree) > 2:
        return "No"
    # connected or not
    uf = UnionFind(n + 1)
    for u, v in uv_list:
        uf.union(u, v)
    for i in range(2, n + 1):
        if not uf.same_check(1, i):
            return "No"
    return "Yes"


def main():
    n, m = map(int, input().split())
    uv_list = [tuple(map(int, input().split())) for _ in range(m)]
    res = solve(n, m, uv_list)
    print(res)
    # for r in res:
    #     print(r)


def test():
    assert solve(4, 3, [(1, 3), (4, 2), (3, 2)]) == "Yes"
    assert solve(2, 0, []) == "No"
    assert solve(5, 5, [(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)]) == "No"


if __name__ == "__main__":
    test()
    main()
