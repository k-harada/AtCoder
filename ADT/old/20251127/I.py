class SegmentTree(object):
    # 0-indexed
    # 2^m
    def __init__(self, length, op=min, e=lambda: 0):
        """
        :param length: length of initial values
        :param op: operator, op(x, y) -> z
        :param e: function that return identity element for op
        """
        self.op = op
        self.e = e
        self.n = 1
        while self.n < length:
            self.n *= 2  # pow2
        self.dat = [e()] * (2 * self.n - 1)

    def initialize(self, x_list):
        """
        initialize data
        :param x_list: initial values fot list
        :return:
        """
        assert len(x_list) <= self.n
        # update base
        # ith -> n - 1 + i
        for i, x in enumerate(x_list):
            self.dat[self.n - 1 + i] = x
        # upper values
        for i in range(self.n - 2, -1, -1):
            self.dat[i] = self.op(self.dat[2 * i + 1], self.dat[2 * i + 2])

    def set_val(self, k, a):
        """
        update k-th(0-indexed) value with a
        :param k: index to set(0-indexed)
        :param a: value to set
        :return: None
        """
        k += self.n - 1
        self.dat[k] = a
        while k > 0:
            k = (k - 1) // 2  # parent
            self.dat[k] = self.op(self.dat[k * 2 + 1], self.dat[k * 2 + 2])

    def query(self, p, q):
        """
        :param p: int
        :param q: int
        :return: "minimum" value in [p, q)
        """
        if q <= p:
            return self.e()
        p += self.n - 1
        q += self.n - 2
        vl = self.e()
        vr = self.e()

        while q - p > 1:
            if p & 1 == 0:
                vl = self.op(vl, self.dat[p])
            if q & 1 == 1:
                vr = self.op(self.dat[q], vr)
                q -= 1
            p = p // 2
            q = (q - 1) // 2
        if p == q:
            res = self.op(self.op(vl, self.dat[p]), vr)
        else:
            res = self.op(self.op(vl, self.dat[p]), self.op(self.dat[q], vr))
        return res

    def query_recursive(self, p, q):
        """
        recursive version, Ref. Ant Book p.155
        :param p: int
        :param q: int
        :return: "minimum" value in [p, q)
        """
        if q <= p:
            return self.e()
        return self._query_recursive(p, q, 0, 0, self.n)

    def _query_recursive(self, a, b, k, l, r):
        """
        :param a: int
        :param b: int
        :param k: int
        :param l: int
        :param r: int
        :return: "minimum" value in [a, b) and [l, r)
        """
        # no intersection -> e
        if r <= a or b <= l:
            return self.e()
        # [a, b) includes [l, r) -> return [l, r)
        if a <= l and r <= b:
            return self.dat[k]
        else:
            # ask children
            vl = self._query_recursive(a, b, k * 2 + 1, l, (l + r) // 2)
            vr = self._query_recursive(a, b, k * 2 + 2, (l + r) // 2, r)
        return self.op(vl, vr)


def add(a, b):
    return a + b


def solve(n, uv_list, q, query_list):
    # DFS tour
    G = [[] for _ in range(n + 1)]
    for i, (u, v) in enumerate(uv_list):
        G[u].append((v, i + 1))
        G[v].append((u, i + 1))
    queue = [-1, 1]
    visited = [False] * (n + 1)
    visited[1] = True
    dfs_tour = []
    start_ind = [0] * (n + 1)
    end_ind = [0] * (n + 1)
    edge_child = [0] * n
    while len(queue):
        p = queue.pop()
        if p < 0:
            end_ind[-p] = len(dfs_tour)
        else:
            start_ind[p] = len(dfs_tour)
            dfs_tour.append(p)
            queue.append(-p)
            for q, i in G[p]:
                if not visited[q]:
                    visited[q] = True
                    edge_child[i] = q
                    queue.append(q)
    # print(dfs_tour)
    # print(start_ind)
    # print(end_ind)
    # print(edge_child)

    node_index = [-1] * (n + 1)
    for i, v in enumerate(dfs_tour):
        node_index[v] = i

    st = SegmentTree(n, op=add, e=lambda: 0)
    st.initialize([1] * n)
    res = []
    for query in query_list:
        if query[0] == 1:
            x, w = query[1], query[2]
            i = node_index[x]
            w0 = st.query(i, i + 1)
            st.set_val(i, w + w0)
            # print([st.query(i, i + 1) for i in range(n)])
        else:
            y = edge_child[query[1]]
            s = st.query(start_ind[1], end_ind[1])
            s1 = st.query(start_ind[y], end_ind[y])
            # print(s, s1, start_ind[y], end_ind[y])
            s0 = s - s1
            # print(s0, s1)
            res.append(abs(s0 - s1))
    # print(res)
    return res


def main():
    n = int(input())
    uv_list = [tuple(map(int, input().split())) for _ in range(n - 1)]
    q = int(input())
    query_list = [tuple(map(int, input().split())) for _ in range(q)]
    res = solve(n, uv_list, q, query_list)
    for r in res:
        print(r)


def test():
    assert solve(6, [
        (1, 2), (1, 3), (2, 4), (4, 5), (4, 6)
    ], 5, [
        (2, 1), (1, 1, 3), (2, 1), (1, 4, 10), (2, 5)
    ]) == [2, 1, 17]


if __name__ == "__main__":
    test()
    main()
