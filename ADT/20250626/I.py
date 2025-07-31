LARGE = 998244353


def scc(n, ab_list):  # 非再帰関数で実装

    g = [[] for _ in range(n + 1)]
    g_rev = [[] for _ in range(n + 1)]
    for a, b in ab_list:
        g[a].append(b)
        g_rev[b].append(a)

    def dfs(v):
        stack = [v]
        used[v] = True
        while len(stack) != 0:
            tmp = stack[-1]
            flag = True
            for i in g[tmp]:
                if not used[i]:
                    flag = False
                    used[i] = True
                    stack.append(i)
                    break
            if flag:  # どこにも行かなかった時
                stack.pop()
                # stack = stack[:-1] #一行上に最適化
                vs.append(tmp)

    def rdfs(v, k):
        stack = [v]
        used[v] = True
        cmp[v] = k
        while len(stack) != 0:
            tmp = stack[-1]
            stack.pop()
            # stack = stack[:-1] #一行上に最適化
            used[tmp] = True
            for i in g_rev[tmp]:
                if not used[i]:
                    cmp[i] = k
                    stack.append(i)

    used = [False] * (n + 1)  # 既に調べたかどうか
    vs = []  # 帰りがけの並び
    cmp = [-1] * (n + 1)
    for i in range(n + 1):
        if not used[i]:
            dfs(i)
    k = 0
    used = [False] * (n + 1)  # 既に調べたかどうか
    for i in vs[::-1]:
        if not used[i]:
            rdfs(i, k)
            k += 1
    return k, cmp  # 強連結成分分解をしたあとの要素数kとそれぞれの点がどこに位置するか


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


def solve(n, m, a_list):
    ab_list = []
    for i, a in enumerate(a_list):
        ab_list.append((i + 1, a))
    kk, cmp = scc(n, ab_list)
    # print(kk, cmp)

    pmap = [-1] * (kk - 1)
    for i, a in enumerate(a_list):
        pmap[cmp[i + 1]] = cmp[a]
    for i in range(kk - 1):
        if pmap[i] == i:
            pmap[i] = kk - 1
    # print(pmap)

    children = [[] for _ in range(kk)]
    for i, p in enumerate(pmap):
        children[p].append(i)
    # print(children)

    # tour
    queue = [kk - 1]
    tour = []
    while len(queue):
        p = queue.pop()
        tour.append(p)
        for c in children[p]:
            queue.append(c)
    # print(tour)
    table = [[1] * m for _ in range(kk)]
    for p in reversed(tour):
        if len(children[p]):
            for c in children[p]:
                x = 0
                for i in range(m):
                    x += table[c][i]
                    table[p][i] *= x
                    table[p][i] %= LARGE
        else:
            for i in range(m):
                table[p][i] = 1
    res = table[kk - 1][-1]
    # print(table)
    # print(res)
    return res


def main():
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, m, a_list)
    print(res)


def test():
    assert solve(3, 3, [2, 1, 1]) == 6
    assert solve(4, 9, [1, 1, 1, 1]) == 2025
    assert solve(10, 5, [9, 4, 5, 5, 4, 2, 1, 5, 7, 2]) == 10010


if __name__ == "__main__":
    test()
    main()
