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


def solve(h, w, s):
    id_map = defaultdict(int)
    id_list = []
    flag_list = [0] * (h * w)
    for i in range(h):
        for j in range(w):
            r = i * w + j
            if s[i][j] == "#":
                id_map[r] = len(id_list)
                id_list.append(r)
                flag_list[r] = 1

    m = len(id_list)
    uf = UnionFind(m)
    for r in id_list:
        i = r // w
        j = r % w
        p = id_map[r]
        if i > 0 and j > 0:
            i_, j_ = i - 1, j - 1
            r_ = i_ * w + j_
            if flag_list[r_] == 1:
                q = id_map[r_]
                uf.union(p, q)
        if i > 0:
            i_, j_ = i - 1, j
            r_ = i_ * w + j_
            if flag_list[r_] == 1:
                q = id_map[r_]
                uf.union(p, q)
        if i > 0 and j < w - 1:
            i_, j_ = i - 1, j + 1
            r_ = i_ * w + j_
            if flag_list[r_] == 1:
                q = id_map[r_]
                uf.union(p, q)
        if j > 0:
            i_, j_ = i, j - 1
            r_ = i_ * w + j_
            if flag_list[r_] == 1:
                q = id_map[r_]
                uf.union(p, q)

    parent_list = [uf.find(i) for i in range(m)]
    # print(set(parent_list))
    return len(set(parent_list))


def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    res = solve(h, w, s)
    print(res)


def test():
    assert solve(5, 6, [
        ".##...",
        "...#..",
        "....##",
        "#.#...",
        "..#...",
    ]) == 3
    assert solve(3, 3, [
        "#.#",
        ".#.",
        "#.#",
    ]) == 1
    assert solve(4, 2, ["..", "..", "..", ".."]) == 0
    assert solve(5, 47, [
        ".#..#..#####..#...#..#####..#...#...###...#####",
        ".#.#...#.......#.#...#......##..#..#...#..#....",
        ".##....#####....#....#####..#.#.#..#......#####",
        ".#.#...#........#....#......#..##..#...#..#....",
        ".#..#..#####....#....#####..#...#...###...#####"
    ]) == 7


if __name__ == "__main__":
    test()
    main()
