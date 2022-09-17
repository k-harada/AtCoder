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


def solve(n, xy_list):
    uf = UnionFind(n)
    for i in range(n - 1):
        x_i, y_i = xy_list[i]
        for j in range(i + 1, n):
            x_j, y_j = xy_list[j]
            if (x_i - 1 == x_j) and (y_i - 1 == y_j):
                uf.union(i + 1, j + 1)
            elif (x_i - 1 == x_j) and (y_i == y_j):
                uf.union(i + 1, j + 1)
            elif (x_i == x_j) and (y_i - 1 == y_j):
                uf.union(i + 1, j + 1)
            elif (x_i == x_j) and (y_i + 1 == y_j):
                uf.union(i + 1, j + 1)
            elif (x_i + 1 == x_j) and (y_i == y_j):
                uf.union(i + 1, j + 1)
            elif (x_i + 1 == x_j) and (y_i + 1 == y_j):
                uf.union(i + 1, j + 1)

    parents = []
    for i in range(1, n + 1):
        parents.append(uf.find(i))

    res = len(set(parents))
    return res


def main():
    n = int(input())
    xy_list = [tuple(map(int, input().split())) for _ in range(n)]
    res = solve(n, xy_list)
    print(res)


def test():
    assert solve(6, [(-1, -1), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0)]) == 3
    assert solve(4, [(5, 0), (4, 1), (-3, -4), (-2, -5)]) == 4
    assert solve(5, [(2, 1), (2, -1), (1, 0), (3, 1), (1, -1)]) == 1


def test_large():
    print(solve(1000, [(i, i) for i in range(1000)]))


if __name__ == "__main__":
    test()
    # test_large()
    main()
