from heapq import heappop, heappush


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


def solve(n, xy_list):

    # sort y by x
    xy_list_s = sorted(xy_list, key=lambda x: x[0])
    y_list_s = [xy[1] for xy in xy_list_s]

    # union_find
    uf = UnionFind(n)

    # heap
    h = []
    for y in y_list_s:
        yp_list = [y]
        while len(h):
            p = heappop(h)
            if p < y:
                yp_list.append(p)
                uf.union(p, y)
            else:
                heappush(h, p)
                break
        heappush(h, min(yp_list))

    # unite
    parent_n = [0] * n
    parent_cnt = [0] * (n + 1)
    for i in range(n):
        p = uf.find(xy_list[i][1])
        parent_n[i] = p
        parent_cnt[p] += 1

    return [parent_cnt[parent_n[i]] for i in range(n)]


def main():
    n = int(input())
    xy_list = [[0] * 2 for _ in range(n)]
    for i in range(n):
        x, y = map(int, input().split())
        xy_list[i][0] = x
        xy_list[i][1] = y
    res = solve(n, xy_list)
    for r in res:
        print(r)


def test():
    assert solve(4, [[1, 4], [2, 3], [3, 1], [4, 2]]) == [1, 1, 2, 2]
    assert solve(7, [[6, 4], [4, 3], [3, 5], [7, 1], [2, 7], [5, 2], [1, 6]]) == [3, 3, 1, 1, 2, 3, 2]


if __name__ == "__main__":
    test()
    main()
