import numpy as np


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


MOD = 998244353


def solve(n, k, a_list):
    a_array = np.array(a_list, dtype=int)
    # factorial
    factorial = [1] * (n + 1)
    for i in range(2, n + 1):
        factorial[i] = factorial[i - 1] * i % MOD

    res = 1

    # row
    uf_row = UnionFind(n)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if (a_array[i, :] + a_array[j, :]).max() <= k:
                uf_row.union(i + 1, j + 1)
    par_count = [0] * (n + 1)
    for i in range(1, n + 1):
        par_count[uf_row.find(i)] += 1
    for i in range(1, n + 1):
        res *= factorial[par_count[i]]
        res %= MOD

    # col
    uf_col = UnionFind(n)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if (a_array[:, i] + a_array[:, j]).max() <= k:
                uf_col.union(i + 1, j + 1)
    par_count = [0] * (n + 1)
    for i in range(1, n + 1):
        par_count[uf_col.find(i)] += 1
    for i in range(1, n + 1):
        res *= factorial[par_count[i]]
        res %= MOD

    return res


def main():
    n, k = map(int, input().split())
    a_list = [list(map(int, input().split())) for _ in range(n)]
    res = solve(n, k, a_list)
    print(res)


def test():
    assert solve(3, 13, [[2, 3, 7], [8, 4, 9], [6, 1, 5]]) == 12
    # assert solve(50, 1000, [[50 * i + j for j in range(50)] for i in range(50)]) == 12


if __name__ == "__main__":
    test()
    main()
