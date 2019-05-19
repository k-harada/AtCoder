# unionfind


class UnionFind(object):

    def __init__(self, n):
        self.n = n
        self.parent = list(range(self.n))
        self.rank = [0]*n

    def find_parent(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find_parent(self.parent[x])
            return self.parent[x]

    def unite(self, x, y):
        x = self.find_parent(x)
        y = self.find_parent(y)
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1


N, M = map(int, input().split())
uf = UnionFind(N+1)

for _ in range(M):
    xx, yy, zz = map(int, input().split())
    uf.unite(xx, yy)

res = [0] * (N + 1)
res_c = 0
for i in range(1, N + 1):
    j = uf.find_parent(i)
    if res[j] == 0:
        res_c += 1
    res[j] += 1

print(N - (sum(res) - res_c))
