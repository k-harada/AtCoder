# source : http://at274.hatenablog.com/entry/2018/02/02/173000


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
    for u, v in uv_list:
        uf.union(u, v)
    parents = []
    for i in range(1, n + 1):
        parents.append(uf.find(i))
    res = len(set(parents))
    return res


def main():
    n, m = map(int, input().split())
    uv_list = tuple(map(int, input().split()))
    res = solve(n, m, uv_list)
    print(res)


def test():
    assert solve(5, 3, [(1, 2), (1, 3), (4, 5)]) == 2
    assert solve(5, 0, []) == 5
    assert solve(4, 6, [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]) == 1


if __name__ == "__main__":
    test()
    main()
