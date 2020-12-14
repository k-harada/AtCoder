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


def solve(n, q, a_list, query_list):
    res_list = []

    def zero():
        return 0

    def op_xor(xx, yy):
        return xx ^ yy

    range_xor_query = SegmentTree(n, op_xor, zero)
    range_xor_query.initialize(a_list)

    for t, x, y in query_list:
        if t == 1:
            ax = range_xor_query.query(x - 1, x)
            range_xor_query.set_val(x - 1, ax ^ y)
        else:
            res_list.append(range_xor_query.query(x - 1, y))

    return res_list


def main():
    n, q = map(int, input().split())
    a_list = list(map(int, input().split()))
    query_list = [tuple(map(int, input().split())) for _ in range(q)]
    res = solve(n, q, a_list, query_list)
    for r in res:
        print(r)


def test():
    assert solve(3, 4, [1, 2, 3], [(2, 1, 3), (2, 2, 3), (1, 2, 3), (2, 2, 3)]) == [0, 1, 2]
    assert solve(10, 10, [0, 5, 3, 4, 7, 0, 0, 0, 1, 0], [
        (1, 10, 7), (2, 8, 9), (2, 3, 6), (2, 1, 6), (2, 1, 10), (1, 9, 4), (1, 6, 1), (1, 6, 3), (1, 1, 7), (2, 3, 5)
    ]) == [1, 0, 5, 3, 0]


if __name__ == "__main__":
    test()
    main()
