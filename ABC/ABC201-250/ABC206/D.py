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


def solve(n, a_list):

    uf = UnionFind(max(a_list))
    res = 0
    for i in range(n):
        if i >= n - 1 - i:
            break
        if not uf.same_check(a_list[i], a_list[n - 1 - i]):
            uf.union(a_list[i], a_list[n - 1 - i])
            res += 1

    return res


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(8, [1, 5, 3, 2, 5, 2, 3, 1]) == 2
    assert solve(7, [1, 2, 3, 4, 1, 2, 3]) == 1
    assert solve(1, [200000]) == 0


if __name__ == "__main__":
    test()
    main()
