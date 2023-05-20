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
        self.par[x] = y

    # check
    def same_check(self, x, y):
        return self.find(x) == self.find(y)


def solve(n, p_list, q, query_list):
    uf = UnionFind(n)
    p_list_ = [0, 0] + p_list
    res = []
    for query in query_list:
        if query[0] == 1:
            u, v = query[1], query[2]
            w = uf.find(u)
            while w > v:
                uf.union(w, v)
                w = p_list_[w]
        else:
            res.append(uf.find(query[1]))
    # print(res)
    return res


def main():
    n = int(input())
    p_list = list(map(int, input().split()))
    q = int(input())
    query_list = [tuple(map(int, input().split())) for _ in range(q)]
    res = solve(n, p_list, q, query_list)
    for r in res:
        print(r)


def test():
    assert solve(5, [1, 2, 3, 3], 5, [(2, 4), (1, 4, 2), (2, 4), (1, 5, 1), (2, 4)]) == [4, 2, 1]


if __name__ == "__main__":
    test()
    main()
