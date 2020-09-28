class SegmentTree(object):

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

    def update(self, k, a):
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
        res = self.e()

        while q - p > 1:
            if p & 1 == 0:
                res = self.op(res, self.dat[p])
            if q & 1 == 1:
                res = self.op(res, self.dat[q])
                q -= 1
            p = p // 2
            q = (q - 1) // 2
        if p == q:
            res = self.op(res, self.dat[p])
        else:
            res = self.op(self.op(res, self.dat[p]), self.dat[q])
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


def solve(n, k, a_list):
    seg_tree = SegmentTree(300001, max, e=lambda: 0)
    for i in range(n):
        a = a_list[i]
        r = seg_tree.query(max(0, a - k), min(a + k + 1, 300001))
        seg_tree.update(a, r + 1)
    return seg_tree.query(0, 300001)


def main():
    n, k = map(int, input().split())
    a_list = [int(input()) for _ in range(n)]
    res = solve(n, k, a_list)
    print(res)


def test():
    assert solve(10, 3, [1, 5, 4, 3, 8, 6, 9, 7, 2, 4]) == 7


if __name__ == "__main__":
    test()
    main()
