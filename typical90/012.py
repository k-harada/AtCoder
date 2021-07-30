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


def solve(h, w, q, query_list):
    res = []
    uf = UnionFind(h * w)
    red_map = [[0] * w for _ in range(h)]
    for query in query_list:
        if query[0] == 1:
            _, r, c = query
            r -= 1
            c -= 1
            p = r * w + c
            # paste
            red_map[r][c] = 1
            # unite
            if r > 0:
                if red_map[r - 1][c] == 1:
                    uf.union(p, p - w)
            if r < h - 1:
                if red_map[r + 1][c] == 1:
                    uf.union(p, p + w)
            if c > 0:
                if red_map[r][c - 1] == 1:
                    uf.union(p, p - 1)
            if c < w - 1:
                if red_map[r][c + 1] == 1:
                    uf.union(p, p + 1)
        else:
            _, ra, ca, rb, cb = query
            ra -= 1
            ca -= 1
            rb -= 1
            cb -= 1
            p = ra * w + ca
            q = rb * w + cb
            if uf.same_check(p, q) and red_map[ra][ca] == 1 and red_map[rb][cb] == 1:
                res.append("Yes")
            else:
                res.append("No")
    # print(res)
    return res


def main():
    h, w = map(int, input().split())
    q = int(input())
    query_list = [tuple(map(int, input().split())) for _ in range(q)]
    res = solve(h, w, q, query_list)
    for r in res:
        print(r)


def test():
    assert solve(3, 3, 10, [
        (1, 2, 2), (1, 1, 1), (2, 1, 1, 2, 2), (1, 3, 2), (2, 1, 1, 2, 2),
        (2, 2, 2, 3, 2), (1, 2, 3), (1, 2, 1), (2, 1, 1, 2, 2), (2, 1, 1, 3, 3)
    ]) == ["No", "No", "Yes", "Yes", "No"]
    assert solve(1, 1, 3, [(2, 1, 1, 1, 1), (1, 1, 1), (2, 1, 1, 1, 1)]) == ["No", "Yes"]


if __name__ == "__main__":
    test()
    main()
