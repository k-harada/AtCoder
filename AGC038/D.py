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


def solve_d(n, m, q, a_list, b_list, c_list):

    res = 'Yes'
    uf = UnionFind(n - 1)
    for i in range(q):
        if c_list[i] == 0:
            uf.union(a_list[i], b_list[i])

    for i in range(q):
        if c_list[i] == 1:
            if uf.same_check(a_list[i], b_list[i]):
                res = 'No'

    par_list = [0] * n
    for i in range(n):
        par_list[i] = uf.find(i)

    k = len(set(par_list))
    # print(k, par_list)
    if max(c_list) == 0:
        min_m = n - 1
    else:
        min_m = n
    if m < min_m:
        res = 'No'
    elif m > n + k * (k - 3) // 2:
        res = 'No'

    return res


def main():
    n, m, q = map(int, input().split())
    a_list = [0] * q
    b_list = [0] * q
    c_list = [0] * q

    for i in range(q):
        a, b, c = map(int, input().split())
        a_list[i] = a
        b_list[i] = b
        c_list[i] = c

    res = solve_d(n, m, q, a_list, b_list, c_list)
    print(res)


if __name__ == "__main__":
    main()
