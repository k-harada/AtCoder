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


def solve(n, m, abc_list):
    abc_list_s = list(sorted(abc_list, key=lambda x: x[2]))
    res = 0
    uf = UnionFind(n)
    for a, b, c in abc_list_s:
        if uf.same_check(a, b):
            if c > 0:
                res += c
        else:
            uf.union(a, b)
    return res


def main():
    n, m = map(int, input().split())
    abc_list = [tuple(map(int, input().split())) for _ in range(m)]
    res = solve(n, m, abc_list)
    print(res)


def test():
    assert solve(4, 5, [(1, 2, 1), (1, 3, 1), (1, 4, 1), (3, 2, 2), (4, 2, 2)]) == 4
    assert solve(3, 3, [(1, 2, 1), (2, 3, 0), (3, 1, -1)]) == 1
    assert solve(2, 3, [(1, 2, -1), (1, 2, 2), (1, 1, 3)]) == 5


if __name__ == "__main__":
    test()
    main()
