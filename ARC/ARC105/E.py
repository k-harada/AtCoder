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


def solve(t, case_list):
    res_list = []
    for i in range(t):
        # union-find
        n, m, edge_list = case_list[i]
        uf = UnionFind(n)
        for j in range(m):
            x, y = edge_list[j]
            uf.union(x, y)
        # query parent
        parent_size = [0] * (n + 1)
        for p in range(n):
            parent = uf.find(p + 1)
            parent_size[parent] += 1
        # count size
        s1 = parent_size[uf.find(1)]
        sn = parent_size[uf.find(n)]

        if n % 2 == 1:
            edges_left = n * (n - 1) // 2 - m
            if edges_left % 2 == 1:
                res_list.append("First")
            else:
                res_list.append("Second")
        else:
            if (s1 + sn) % 2 == 1:
                res_list.append("First")
            else:
                edges_left = n * (n - 1) // 2 - m - s1 * sn
                if edges_left % 2 == 1:
                    res_list.append("First")
                else:
                    res_list.append("Second")

    return res_list


def main():
    t = int(input())
    case_list = []
    for _ in range(t):
        n, m = map(int, input().split())
        edge_list = [list(map(int, input().split())) for _ in range(m)]
        case_list.append([n, m, edge_list])
    res = solve(t, case_list)
    for r in res:
        print(r)


if __name__ == "__main__":
    main()
