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


def solve(n, m, p_list, xy_list):
    uf = UnionFind(n + 1)
    for x, y in xy_list:
        uf.union(x, y)
    res = 0
    for a in range(1, n + 1):
        if uf.find(a) == uf.find(p_list[a - 1]):
            res += 1
    return res


def main():
    n, m = map(int, input().split())
    p_list = list(map(int, input().split()))
    xy_list = [tuple(map(int, input().split())) for _ in range(m)]
    res = solve(n, m, p_list, xy_list)
    print(res)


def test():
    assert solve(5, 2, [5, 3, 1, 4, 2], [(1, 3), (5, 4)]) == 2
    assert solve(3, 2, [3, 2, 1], [(1, 2), (2, 3)]) == 3
    assert solve(5, 1, [1, 2, 3, 4, 5], [(1, 5)]) == 5


if __name__ == "__main__":
    test()
    main()
