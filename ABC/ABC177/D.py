class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank = [0] * (n+1)

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
    uf = UnionFind(n)
    for a, b in ab_list:
        uf.union(a, b)

    par_count = [0] * (n + 1)
    for i in range(1, n + 1):
        par_count[uf.find(i)] += 1

    return max(par_count)


def main():
    n, m = map(int, input().split())
    ab_list = [tuple(map(int, input().split())) for _ in range(m)]
    res = solve(n, m, ab_list)
    print(res)


def test():
    assert solve(5, 3, [(1, 2), (3, 4), (5, 1)]) == 3
    assert solve(4, 10, [(1, 2), (2, 1), (1, 2), (2, 1), (1, 2), (1, 3), (1, 4), (2, 3), (3, 4)]) == 4
    assert solve(10, 4, [(3, 1), (4, 1), (5, 9), (2, 6)]) == 3


if __name__ == "__main__":
    test()
    main()
