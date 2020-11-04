from heapq import heappop, heappush
import math


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

    uf = UnionFind(n + 1)

    h = []

    for i in range(n - 1):
        x_i, y_i = xy_list[i]
        for j in range(i + 1, n):
            x_j, y_j = xy_list[j]
            d_square = (x_i - x_j) ** 2 + (y_i - y_j) ** 2
            heappush(h, (d_square, i + 1, j + 1))

    for i in range(n):
        _, y_i = xy_list[i]
        d_square = (y_i + 100) ** 2
        heappush(h, (d_square, i + 1, 0))
        d_square = (100 - y_i) ** 2
        heappush(h, (d_square, i + 1, n + 1))

    while len(h):
        d_square, i, j = heappop(h)
        uf.union(i, j)
        # check if single
        if uf.find(0) == uf.find(n + 1):
            return math.sqrt(d_square) / 2

    return 0


def main():
    n = int(input())
    xy_list = [tuple(map(int, input().split())) for _ in range(n)]
    res = solve(n, xy_list)
    print(res)


if __name__ == "__main__":
    main()
