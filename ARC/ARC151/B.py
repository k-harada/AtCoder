MOD = 998244353


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


def solve(n, m, p_list):
    res = 0
    used = [0] * n
    uf = UnionFind(n)
    fixed = 0
    free = n
    for i in range(n):
        # 自分自身
        if i == p_list[i] - 1:
            fixed += 1
            free -= 1
            continue
        # 既に同じになること強いられている
        if uf.find(i) == uf.find(p_list[i] - 1):
            continue
        # iとp_list[i] - 1の分
        r = m * (m - 1) // 2
        r %= MOD
        # 残りの自由度
        r *= pow(m, fixed + free - 2, MOD)
        r %= MOD
        res += r
        # print(i, r, fixed, free)
        res %= MOD
        # 自由度の更新
        if used[i] == 0:
            if used[p_list[i] - 1] == 0:
                fixed += 1
                free -= 2
            else:
                free -= 1
        else:
            if used[p_list[i] - 1] == 0:
                free -= 1
            else:
                fixed -= 1
        uf.union(i, p_list[i] - 1)
        used[i] = 1
        used[p_list[i] - 1] = 1
    # print(res)
    return res


def main():
    n, m = map(int, input().split())
    p_list = list(map(int, input().split()))
    res = solve(n, m, p_list)
    print(res)


def test():
    assert solve(4, 2, [4, 1, 3, 2]) == 6
    assert solve(1, 1, [1]) == 0
    assert solve(20, 100000, [11, 15, 3, 20, 17, 6, 1, 9, 5, 19, 10, 16, 7, 8, 12, 2, 18, 14, 4, 13]) == 55365742


if __name__ == "__main__":
    test()
    main()
