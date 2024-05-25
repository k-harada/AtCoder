from collections import defaultdict


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


def solve(n, m, uv_list, k, xy_list, q, pq_list):
    uf = UnionFind(n)
    for u, v in uv_list:
        uf.union(u, v)
    p_list = [uf.find(i) for i in range(n + 1)]
    counter = defaultdict(int)
    for x, y in xy_list:
        counter[f"{p_list[x]} {p_list[y]}"] = 1
        counter[f"{p_list[y]} {p_list[x]}"] = 1
    res = []
    for p_, q_ in pq_list:
        if counter[f"{p_list[p_]} {p_list[q_]}"] == 1:
            res.append("No")
        else:
            res.append("Yes")
    return res


def main():
    n, m = map(int, input().split())
    uv_list = [tuple(map(int, input().split())) for _ in range(m)]
    k = int(input())
    xy_list = [tuple(map(int, input().split())) for _ in range(k)]
    q = int(input())
    pq_list = [tuple(map(int, input().split())) for _ in range(q)]
    res = solve(n, m, uv_list, k, xy_list, q, pq_list)
    for r in res:
        print(r)


def test():
    assert solve(6, 6, [
        (1, 2), (2, 3), (2, 3), (3, 1), (5, 4), (5, 5)
    ], 3, [
        (1, 5), (2, 6), (4, 3)
    ], 4, [
        (2, 5), (2, 6), (5, 6), (5, 4)
    ]) == ["No", "No", "Yes", "Yes"]


if __name__ == "__main__":
    test()
    main()
