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


def solve(n, m, ab_list, c_list):
    uf = UnionFind(n)
    for a, b in ab_list:
        if c_list[a - 1] != c_list[b - 1]:
            uf.union(a, b)

    for a, b in ab_list:
        if c_list[a - 1] == c_list[b - 1]:
            if uf.same_check(a, b):
                return "Yes"
    return "No"


def main():
    n, m = map(int, input().split())
    ab_list = [tuple(map(int, input().split())) for _ in range(m)]
    c_list = list(map(int, input().split()))
    res = solve(n, m, ab_list, c_list)
    print(res)


def test():
    assert solve(4, 4, [(1, 2), (2, 3), (3, 4), (4, 2)], [0, 1, 0, 1]) == "Yes"
    assert solve(5, 6, [(1, 2), (2, 3), (3, 4), (4, 5), (1, 4), (2, 5)], [0, 1, 0, 1, 0]) == "No"


if __name__ == "__main__":
    test()
    main()
