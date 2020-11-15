from collections import defaultdict


class UnionFindMod:
    def __init__(self, n, c_list):
        self.par = [i for i in range(n + 1)]
        self.rank = [1] * (n + 1)
        self.contents = [defaultdict(int) for _ in range(n + 1)]
        for i in range(n):
            self.contents[i + 1][c_list[i]] = 1

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
            self.rank[y] += self.rank[x]
            for k in self.contents[x].keys():
                self.contents[y][k] += self.contents[x][k]
        else:
            self.par[y] = x
            self.rank[x] += self.rank[y]
            for k in self.contents[y].keys():
                self.contents[x][k] += self.contents[y][k]

    # check
    def same_check(self, x, y):
        return self.find(x) == self.find(y)


def solve(n, q, c_list, query_list):
    ufm = UnionFindMod(n, c_list)
    res_list = []
    for q1, q2, q3 in query_list:
        if q1 == 1:
            if not ufm.same_check(q2, q3):
                ufm.union(q2, q3)
        else:
            p = ufm.find(q2)
            res_list.append(ufm.contents[p][q3])

    return res_list


def main():
    n, q = map(int, input().split())
    c_list = list(map(int, input().split()))
    query_list = [tuple(map(int, input().split())) for _ in range(q)]
    res_list = solve(n, q, c_list, query_list)
    for r in res_list:
        print(r)


def test():
    assert solve(5, 5, [1, 2, 3, 2, 1], [(1, 1, 2), (1, 2, 5), (2, 1, 1), (1, 3, 4), (2, 3, 4)]) == [2, 0]
    assert solve(5, 4, [2, 2, 2, 2, 2], [(1, 1, 2), (1, 1, 3), (1, 2, 3), (2, 2, 2)]) == [3]
    assert solve(12, 9, [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3], [
        (1, 1, 2), (1, 3, 4), (1, 5, 6), (1, 7, 8), (2, 2, 1), (1, 9, 10), (2, 5, 6), (1, 4, 8), (2, 6, 1)
    ]) == [1, 0, 0]
    # print(0)
    # print(solve(200000, 200000, [1] * 200000, [(1, i + 1, i + 2) for i in range(199999)] + [(2, 1, 1)]))


if __name__ == "__main__":
    # test()
    main()
