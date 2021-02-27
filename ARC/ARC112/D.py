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


def solve(h, w, s_list):
    ufh = UnionFind(h)
    ufh.union(0, h - 1)
    for j in range(w):
        if j == 0 or j == w - 1:
            i_min = 0
        else:
            i_min = -1
        for i in range(h):
            if s_list[i][j] == "#":
                if i_min == -1:
                    i_min = i
                else:
                    ufh.union(i_min, i)
    res_h = len(set([ufh.find(i) for i in range(h)]))

    ufw = UnionFind(w)
    ufw.union(0, w - 1)
    for i in range(h):
        if i == 0 or i == h - 1:
            j_min = 0
        else:
            j_min = -1
        for j in range(w):
            if s_list[i][j] == "#":
                if j_min == -1:
                    j_min = j
                else:
                    ufw.union(j_min, j)
    res_w = len(set([ufw.find(j) for j in range(w)]))
    return min(res_h, res_w) - 1


def main():
    h, w = map(int, input().split())
    s_list = [input() for _ in range(h)]
    res = solve(h, w, s_list)
    print(res)


def test():
    assert solve(3, 9, [".........", ".........", "........."]) == 1
    assert solve(10, 10, [
        "..........",
        "#...#.....",
        "..........",
        "..........",
        "..........",
        "....#.....",
        ".#......#.",
        "..........",
        "..........",
        ".........."
    ]) == 6


if __name__ == "__main__":
    test()
    main()
