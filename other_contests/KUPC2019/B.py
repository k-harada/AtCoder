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


def solve_b(n, m, w_total, w_list, v_list, ab_list):
    # union find
    uf = UnionFind(n)
    for k in range(m):
        uf.union(ab_list[k][0], ab_list[k][1])

    w_list_new = [0] * (n + 1)
    v_list_new = [0] * (n + 1)
    for i in range(n):
        j = uf.find(i + 1)
        w_list_new[j] += w_list[i]
        v_list_new[j] += v_list[i]

    w_list_new = [w for w in w_list_new if w > 0]
    v_list_new = [v for v in v_list_new if v > 0]

    ln = len(w_list_new)
    assert len(v_list_new) == ln

    dp = [[0] * (w_total + 1) for _ in range(2)]

    for i in range(ln):
        s = i % 2
        t = 1 - s
        w_add = w_list_new[i]
        v_add = v_list_new[i]
        for w in range(w_total - w_add + 1):
            dp[t][w + w_add] = max(dp[s][w] + v_add, dp[s][w + w_add])

    return max(max(dp[0]), max(dp[1]))


def main():
    n, m, w_total = map(int, input().split())
    w_list = [0] * n
    v_list = [0] * n
    for i in range(n):
        w, v = map(int, input().split())
        w_list[i] = w
        v_list[i] = v
    ab_list = []
    for i in range(m):
        a, b = map(int, input().split())
        ab_list.append([a, b])
    res = solve_b(n, m, w_total, w_list, v_list, ab_list)
    print(res)


def test():
    assert solve_b(3, 1, 10, [3, 5, 3], [2, 4, 3], [[1, 2]]) == 6
    assert solve_b(4, 0, 10, [1, 2, 3, 4], [1, 2, 3, 4], []) == 10
    assert solve_b(3, 3, 6, [2, 3, 3], [5, 8, 4], [[1, 2], [2, 3], [3, 1]]) == 0
    assert solve_b(1, 0, 10000, [10000], [10000000], []) == 10000000


if __name__ == "__main__":
    test()
    main()
