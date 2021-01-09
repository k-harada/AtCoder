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


def solve(n, ab_list):
    m = 0
    for a, b in ab_list:
        m = max([m, a, b])
    uf = UnionFind(m)
    for a, b in ab_list:
        uf.union(a, b)

    # find components
    components_count = [0] * (m + 1)
    parent_list = [0] * (m + 1)
    card_count = [0] * (m + 1)
    for i in range(m + 1):
        p = uf.find(i)
        parent_list[i] = p
        components_count[p] += 1
    for a, b in ab_list:
        p = parent_list[a]
        card_count[p] += 1
    res = 0
    for i in range(m + 1):
        res += min(card_count[i], components_count[i])
    return res


def main():
    n = int(input())
    ab_list = [tuple(map(int, input().split())) for _ in range(n)]
    res = solve(n, ab_list)
    print(res)


def test():
    assert solve(4, [(1, 2), (1, 3), (4, 2), (2, 3)]) == 4
    assert solve(2, [(111, 111), (111, 111)]) == 1
    assert solve(12, [(5, 2), (5, 6), (1, 2), (9, 7), (2, 7), (5, 5), (4, 2), (6, 7), (2, 2), (7, 8), (9, 7), (1, 8)]) == 8


if __name__ == "__main__":
    test()
    main()
