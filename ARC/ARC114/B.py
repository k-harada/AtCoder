MOD = 998244353


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


def solve(n, f_list):
    uf = UnionFind(n + 1)
    for i in range(n):
        uf.union(i + 1, f_list[i])
    p_list = [uf.find(i) for i in range(1, n + 1)]
    res = len(set(p_list))
    return (pow(2, res, MOD) - 1) % MOD


def main():
    n = int(input())
    f_list = list(map(int, input().split()))
    res = solve(n, f_list)
    print(res)


def test():
    assert solve(2, [2, 1]) == 1
    assert solve(2, [1, 1]) == 1
    assert solve(3, [1, 2, 3]) == 7


if __name__ == "__main__":
    test()
    main()
