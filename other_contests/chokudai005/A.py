class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n + 1)]
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


class Panel:

    n = 100
    k = 9

    # pre-compute neighbor list
    neighbor_list = []
    for i in range(n):
        for j in range(n):
            idx = i * n + j
            neighbor = []
            if i != 0:
                neighbor.append(idx - n)
            if j != 0:
                neighbor.append(idx - 1)
            if i != n - 1:
                neighbor.append(idx + n)
            if j != n - 1:
                neighbor.append(idx + 1)
            neighbor_list.append(neighbor)

    def __init__(self, s_list):
        # initialize union-find
        self.s_list_1d = [0] * (self.n * self.n)
        for i in range(self.n):
            for j in range(self.n):
                self.s_list_1d[i * self.n + j] = s_list[i][j]
        self.uf = UnionFind(self.n * self.n)
        for u in range(self.n * self.n):
            for v in self.neighbor_list[u]:
                if self.s_list_1d[u] == self.s_list_1d[v]:
                    self.uf.union(u, v)

    def color_one(self, i, j, c):
        p = self.uf.find(i * self.n + j)
        # change color
        switched = []
        for u in range(self.n * self.n):
            if self.uf.find(u) == p:
                self.s_list_1d[u] = c
                switched.append(u)
        for u in switched:
            for v in self.neighbor_list[u]:
                if self.s_list_1d[u] == self.s_list_1d[v]:
                    self.uf.union(u, v)

    def find_dense(self):
        parent_list = [self.uf.find(u) for u in range(self.n * self.n)]
        counter_dict = dict()
        max_len = 0
        max_u = 0
        max_c = 0
        for pu in set(parent_list):
            counter_dict[pu] = dict()
        for u in range(self.n * self.n):
            pu = parent_list[u]
            cu = self.s_list_1d[u]
            for v in self.neighbor_list[u]:
                cv = self.s_list_1d[v]
                if cu != cv:
                    pv = parent_list[v]
                    counter_dict[pu][pv] = cv
        for pu in set(parent_list):
            c_count = [0] * 10
            for pv in counter_dict[pu].keys():
                c_count[counter_dict[pu][pv]] += 1
            max_pu = max(c_count)
            if max_pu > max_len:
                max_len = max_pu
                max_u = pu
                for c in range(10):
                    if c_count[c] == max_pu:
                        max_c = c
        return max_u, max_c, max_len

    def find_max_c(self, i, j):
        parent_list = [self.uf.find(u) for u in range(self.n * self.n)]
        counter_dict = dict()
        p_center = parent_list[i * self.n + j]
        c_center = self.s_list_1d[p_center]
        for u in range(self.n * self.n):
            pu = parent_list[u]
            if pu != p_center:
                continue
            for v in self.neighbor_list[u]:
                cv = self.s_list_1d[v]
                if cv != c_center:
                    counter_dict[v] = cv

        c_count = [0] * 10
        for v in counter_dict.keys():
            c_count[counter_dict[v]] += 1
        max_pu = max(c_count)
        max_c = 0
        for c in range(10):
            if c_count[c] == max_pu:
                max_c = c
        return max_c, max_pu

    def color_ij(self, i, j):
        return self.s_list_1d[i * self.n + j]


def solve(case_id, n, k, s_list):

    res_list = []

    panel = Panel(s_list)

    while True:
        c, le = panel.find_max_c(49, 49)
        if le == 0:
            break
        panel.color_one(49, 49, c)
        res_list.append([50, 50, c])

    return res_list


def main():
    case_id, n, k = map(int, input().split())
    s_list = []
    for _ in range(n):
        s_list.append(list(map(int, list(input()))))
    res_list = solve(case_id, n, k, s_list)
    print(len(res_list))
    for res in res_list:
        print(" ".join([str(r) for r in res]))


if __name__ == "__main__":
    main()
