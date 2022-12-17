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


def solve(n, m, a_list):
    xyr_list = []
    for i in range(n - 1):
        x = a_list[i]
        for j in range(i + 1, n):
            y = a_list[j]
            r = pow(x, y, m) + pow(y, x, m)
            xyr_list.append((r % m, i, j))
    xyr_list_s = list(sorted(xyr_list, key=lambda a: -a[0]))
    res = 0
    uf = UnionFind(n)
    for r, i, j in xyr_list_s:
        if uf.same_check(i, j):
            continue
        else:
            uf.union(i, j)
            res += r
    return res


def main():
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, m, a_list)
    print(res)


def test():
    assert solve(4, 10, [4, 2, 3, 2]) == 20
    assert solve(20, 100, [29, 31, 68, 20, 83, 66, 23, 84, 69, 96, 41, 61, 83, 37, 52, 71, 18, 55, 40, 8]) == 1733


if __name__ == "__main__":
    test()
    main()
