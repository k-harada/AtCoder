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


def solve(n, m, uv_list, k, x_list):
    uf = UnionFind(n + 1)
    x = x_list[0]
    j = 0
    for i, (u, v) in enumerate(uv_list):
        if i + 1 == x:
            j += 1
            if j == k:
                x = m + 1
            else:
                x = x_list[j]
        else:
            uf.union(u, v)
    cnt = [0] * (n + 1)
    for x in x_list:
        u, v = uv_list[x - 1]
        cnt[uf.find(u)] += 1
        cnt[uf.find(v)] += 1
    r = 0
    # print(cnt)
    for i in range(n + 1):
        if cnt[i] % 2 == 1:
            r += 1
    if r <= 2:
        return "Yes"
    else:
        return "No"


def main():
    n, m = map(int, input().split())
    uv_list = [tuple(map(int, input().split())) for _ in range(m)]
    k = int(input())
    x_list = list(map(int, input().split()))
    res = solve(n, m, uv_list, k, x_list)
    print(res)


def test():
    assert solve(6, 6, [(1, 3), (2, 3), (3, 4), (4, 5), (4, 6), (5, 6)], 4, [1, 2, 4, 5]) == "Yes"


if __name__ == "__main__":
    test()
    main()
