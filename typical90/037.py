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


def solve(w, n, lrv_list):
    sgt = SegmentTree(w + 1, op=max, e=lambda: -10 ** 9 - 7)
    sgt.initialize([0] + [- 10 ** 9 - 7] * w)
    for l, r, v in lrv_list:
        for x in range(w, l - 1, -1):
            new_v = v + sgt.query(max(0, x - r), x - l + 1)
            old_v = sgt.query(x, x + 1)
            if new_v > 0 and new_v > old_v:
                sgt.set_val(x, new_v)
        # print([sgt.query(i, i + 1) for i in range(101)])
    res = sgt.query(w, w + 1)
    if res < 0:
        res = -1
    return res


def main():
    w, n = map(int, input().split())
    lrv_list = [tuple(map(int, input().split())) for _ in range(n)]
    res = solve(w, n, lrv_list)
    print(res)


def test():
    assert solve(100, 4, [(30, 40, 120), (30, 40, 30), (30, 40, 1500), (30, 40, 40)]) == 1660
    assert solve(100, 4, [(13, 15, 31415), (12, 13, 92653), (29, 33, 58979), (95, 98, 32384)]) == -1
    assert solve(5000, 5, [
        (1000, 1000, 1000000000), (1000, 1000, 1000000000), (1000, 1000, 1000000000),
        (1000, 1000, 1000000000), (1000, 1000, 1000000000)
    ]) == 5000000000


if __name__ == "__main__":
    test()
    main()
