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


def solve(n, k, l, pq_list, rs_list):
    uf1 = UnionFind(n)
    for p, q in pq_list:
        uf1.union(p, q)
    uf2 = UnionFind(n)
    for r, s in rs_list:
        uf2.union(r, s)
    p_list = [0] * (n + 1)
    p_count = dict()
    for i in range(1, n + 1):
        p = uf1.find(i) * n + uf2.find(i)
        p_list[i] = p
        if p in p_count.keys():
            p_count[p] += 1
        else:
            p_count[p] = 1
    return " ".join([str(p_count[p_list[i]]) for i in range(1, n + 1)])


def main():
    n, k, l = map(int, input().split())
    pq_list = [tuple(map(int, input().split())) for _ in range(k)]
    rs_list = [tuple(map(int, input().split())) for _ in range(l)]
    res = solve(n, k, l, pq_list, rs_list)
    print(res)


def test():
    assert solve(4, 3, 1, [(1, 2), (2, 3), (3, 4)], [(2, 3)]) == "1 2 2 1"
    assert solve(4, 2, 2, [(1, 2), (2, 3)], [(1, 4), (2, 3)]) == "1 2 2 1"
    assert solve(7, 4, 4, [(1, 2), (2, 3), (2, 5), (6, 7)], [(3, 5), (4, 5), (3, 4), (6, 7)]) == "1 1 2 1 2 2 2"


if __name__ == "__main__":
    test()
    main()
