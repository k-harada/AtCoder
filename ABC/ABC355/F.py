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


def solve(n, q, abc_list, uvw_list):
    uf_list = [UnionFind(n) for _ in range(11)]
    cnt_list = [n] * 11
    for a, b, c in abc_list:
        for x in range(c, 11):
            if uf_list[x].same_check(a, b):
                continue
            else:
                uf_list[x].union(a, b)
                cnt_list[x] -= 1
    res = []
    for u, v, w in uvw_list:
        for x in range(w, 11):
            if uf_list[x].same_check(u, v):
                continue
            else:
                uf_list[x].union(u, v)
                cnt_list[x] -= 1
        tt = n
        r = 0
        # print(cnt_list)
        for i in range(11):
            if cnt_list[i] < tt:
                r += i * (tt - cnt_list[i])
                tt = cnt_list[i]
        res.append(r)
    # print(res)
    return res


def main():
    n, q = map(int, input().split())
    abc_list = [tuple(map(int, input().split())) for _ in range(n - 1)]
    uvw_list = [tuple(map(int, input().split())) for _ in range(q)]
    res = solve(n, q, abc_list, uvw_list)
    for r in res:
        print(r)


def test():
    assert solve(4, 4, [
        (1, 2, 6),
        (2, 3, 5),
        (2, 4, 4)
    ], [
        (1, 3, 3),
        (1, 2, 3),
        (1, 4, 10),
        (3, 4, 1)
    ]) == [12, 10, 10, 7]
    assert solve(8, 6, [
        (1, 8, 8),
        (1, 6, 10),
        (1, 5, 8),
        (2, 6, 6),
        (6, 7, 6),
        (1, 3, 9),
        (2, 4, 7),
    ], [
        (1, 3, 4),
        (1, 6, 7),
        (3, 4, 6),
        (1, 5, 1),
        (7, 8, 4),
        (3, 5, 3),
    ]) == [49, 46, 45, 38, 34, 33]


if __name__ == "__main__":
    test()
    main()
