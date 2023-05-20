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


def add(x, y):
    return x + y


def solve(n, uvw_list, q, query_list):
    g = [[] for _ in range(n + 1)]
    for i, (u, v, w) in enumerate(uvw_list):
        g[u].append((v, w, i + 1))
        g[v].append((u, w, i + 1))

    # EulerTour
    queue = [-1, 1]
    tour = []
    parent_edge_id_list = [0] * (n + 1)
    length_list = []
    visited = [0] * (n + 1)
    parent = [0] * (n + 1)
    parent_length = [0] * (n + 1)
    depth = [0] * (n + 1)
    while len(queue):
        p = queue.pop()
        if p > 0:
            tour.append(p)
            visited[p] = 1
            length_list.append(parent_length[p])
            for q, w, i in g[p]:
                if visited[q] == 1:
                    continue
                queue.append(-q)
                queue.append(q)
                parent_length[q] = w
                parent[q] = p
                depth[q] = depth[p] + 1
                parent_edge_id_list[q] = i
        else:
            tour.append(parent[-p])
            length_list.append(-parent_length[-p])
    # print(tour)
    # print(length_list)
    # print(parent_edge_id_list)
    visited = [0] * (n + 1)
    index_list = [0] * (n + 1)
    edge_ind_list_add = [0] * (n + 1)
    edge_ind_list_sub = [0] * (n + 1)
    for i, x in enumerate(tour):
        if visited[x] == 0:
            visited[x] = 1
            index_list[x] = i
            if x != 1:
                edge_ind_list_add[parent_edge_id_list[x]] = i
        elif x != 0:
            edge_ind_list_sub[parent_edge_id_list[tour[i - 1]]] = i
    # print(tour)
    # print(length_list)
    # print(index_list)
    # print(edge_ind_list_add)
    # print(edge_ind_list_sub)

    res = []
    st = SegmentTree(length=2 * n, op=add, e=lambda: 0)
    st.initialize(length_list)
    dep = SegmentTree(length=2 * n, op=min, e=lambda: (n + 1) * n)
    dep.initialize([depth[x] * (n + 1) + x for x in tour])
    for query in query_list:
        if query[0] == 1:
            i = query[1]
            w = query[2]
            st.set_val(edge_ind_list_add[i], w)
            st.set_val(edge_ind_list_sub[i], -w)
            # print([st.query(i, i + 1) for i in range(2 * n)])
        else:
            u = query[1]
            v = query[2]
            ui = index_list[u]
            vi = index_list[v]
            x = dep.query(min(ui, vi), max(ui, vi) + 1) % (n + 1)
            # print(st.query(0, ui + 1), st.query(0, vi + 1), st.query(0, index_list[x] + 1))
            res.append(st.query(0, ui + 1) + st.query(0, vi + 1) - 2 * st.query(0, index_list[x] + 1))
    # print(res)
    return res


def main():
    n = int(input())
    uvw_list = [tuple(map(int, input().split())) for _ in range(n - 1)]
    q = int(input())
    query_list = [tuple(map(int, input().split())) for _ in range(q)]
    res = solve(n, uvw_list, q, query_list)
    for r in res:
        print(r)


def test():
    assert solve(
        5, [(1, 2, 3), (1, 3, 6), (1, 4, 9), (4, 5, 10)], 4, [(2, 2, 3), (2, 1, 5), (1, 3, 1), (2, 1, 5)]
    ) == [9, 19, 11]
    assert solve(7, [
        (1, 2, 1000000000), (2, 3, 1000000000), (3, 4, 1000000000), (4, 5, 1000000000),
        (5, 6, 1000000000), (6, 7, 1000000000)
    ], 3, [(2, 1, 6), (1, 1, 294967296), (2, 1, 6)]) == [5000000000, 4294967296]
    assert solve(1, [], 1, [(2, 1, 1)]) == [0]


if __name__ == "__main__":
    test()
    main()
