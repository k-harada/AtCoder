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


def solve(n, m, abcd_list):
    uf = UnionFind(2 * n)
    for i in range(n):
        uf.union(2 * i, 2 * i + 1)
    for a, b, c, d in abcd_list:
        if b == "R":
            i = 2 * int(a) - 2
        else:
            i = 2 * int(a) - 1
        if d == "R":
            j = 2 * int(c) - 2
        else:
            j = 2 * int(c) - 1
        # print(i, j)
        uf.union(i, j)

    parents = [uf.find(i) for i in range(2 * n)]
    # print(parents)
    n_components = len(set(parents))
    x = n_components - (n - m)
    y = n_components - x
    # print(n_components, x, y)
    return f"{x} {y}"


def main():
    n, m = map(int, input().split())
    abcd_list = [list(input().split()) for _ in range(m)]
    res = solve(n, m, abcd_list)
    print(res)


def test():
    assert solve(5, 3, [["3", "R", "5", "B"], ["5", "R", "3", "B"], ["4", "R", "2", "B"]]) == "1 2"
    assert solve(7, 0, []) == "0 7"


if __name__ == "__main__":
    test()
    main()
