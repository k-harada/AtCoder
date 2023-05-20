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
    uf = UnionFind(n + 1)
    count_edge = [0] * (n + 1)
    for u, v in uv_list:
        uf.union(u, v)
        count_edge[u] += 1
        count_edge[v] += 1

    parents = [uf.find(i) for i in range(n + 1)]
    count_parents_nodes = [0] * (n + 1)
    count_parents_edges = [0] * (n + 1)
    for i in range(1, n + 1):
        count_parents_nodes[parents[i]] += 1
        count_parents_edges[parents[i]] += count_edge[i]

    for i in range(n + 1):
        if count_parents_edges[i] != count_parents_nodes[i] * 2:
            return "No"
    return "Yes"


def main():
    n, m = map(int, input().split())
    uv_list = [tuple(map(int, input().split())) for _ in range(m)]
    res = solve(n, m, uv_list)
    print(res)


def test():
    assert solve(3, 3, [(2, 3), (1, 1), (2, 3)]) == "Yes"
    assert solve(5, 5, [(1, 2), (2, 3), (3, 4), (3, 5), (1, 5)]) == "Yes"


if __name__ == "__main__":
    test()
    main()
