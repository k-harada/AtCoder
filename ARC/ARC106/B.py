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


def solve(n, m, a_list, b_list, cd_list):

    uf = UnionFind(n)

    for c, d in cd_list:
        uf.union(c, d)

    parent_list = [uf.find(i + 1) for i in range(n)]
    con_group = [[] for _ in range(n + 1)]
    for i in range(n):
        con_group[parent_list[i]].append(i)

    for i in range(n + 1):
        if len(con_group[i]) > 0:
            if sum([a_list[j] for j in con_group[i]]) != sum([b_list[j] for j in con_group[i]]):
                return 'No'
    return 'Yes'


def main():
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    cd_list = [tuple(map(int, input().split())) for _ in range(m)]
    res = solve(n, m, a_list, b_list, cd_list)
    print(res)


def test():
    assert solve(3, 2, [1, 2, 3], [2, 2, 2], [(1, 2), (2, 3)]) == 'Yes'
    assert solve(1, 0, [5], [5], []) == 'Yes'
    assert solve(2, 1, [1, 1], [2, 1], [(1, 2)]) == 'No'


if __name__ == "__main__":
    test()
    main()
