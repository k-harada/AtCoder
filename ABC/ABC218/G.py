from collections import deque


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


def solve(n, a_list, uv_list):
    # v_collection
    values = list(sorted(list(set(a_list))))
    v_dict = dict()
    for i, v in enumerate(values):
        v_dict[v] = i
    counter = [0] * len(values)
    root = [1] * (n + 1)

    # parent and depth
    g = [[] for _ in range(n + 1)]
    for u, v in uv_list:
        g[u].append(v)
        g[v].append(u)
    queue = deque([1])
    depth = [-1] * (n + 1)
    depth[1] = 0
    while len(queue):
        p = queue.popleft()
        for q in g[p]:
            if depth[q] == -1:
                root[p] = 0
                depth[q] = depth[p] + 1
                queue.append(q)

    # create dfs tour
    tour = []
    visited = [0] * (n + 1)
    visited[1] = 1
    queue = deque([1])
    while len(queue):
        p = queue.pop()
        for q in g[p]:
            if depth[q] == -1:
                depth[q] = depth[p] + 1
                queue.append(q)

    return 0


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    uv_list = [tuple(map(int, input().split())) for _ in range(n - 1)]
    res = solve(n, a_list, uv_list)
    print(res)


def test():
    assert solve() == 0
    assert solve() == 0
    assert solve() == 0


if __name__ == "__main__":
    test()
    main()
