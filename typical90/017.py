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


def solve(n, m, lr_list):

    def e_zero():
        return 0

    def op_add(x, y):
        return x + y

    seg = SegmentTree(n + 1, op_add, e_zero)
    seg.initialize([0] * (n + 1))

    lr_list_s = sorted(lr_list, key=lambda x: x[1])
    r_past = 0
    l_list = []
    r_list = []
    res = 0
    for l, r in lr_list_s:
        # update
        if r > r_past:
            for li in l_list:
                a = seg.query(li, li + 1)
                seg.set_val(li, a + 1)
            for ri in r_list:
                b = seg.query(ri, ri + 1)
                seg.set_val(ri, b - 1)
            l_list = []
            r_list = []
            r_past = r
        # query
        # print(seg.query(0, l))
        res += seg.query(0, l)
        # print(l, r, res)
        l_list.append(l)
        r_list.append(r)

    # remove l1_ < r_1 == l_2 < r_2
    l_count = [0] * (n + 1)
    r_count = [0] * (n + 1)
    for l, r in lr_list:
        l_count[l] += 1
        r_count[r] += 1
    for i in range(1, n + 1):
        res -= l_count[i] * r_count[i]
    # print(res)
    return res


def main():
    n, m = map(int, input().split())
    lr_list = [tuple(map(int, input().split())) for _ in range(m)]
    res = solve(n, m, lr_list)
    print(res)


def test():
    assert solve(6, 3, [(2, 5), (1, 4), (1, 3)]) == 2
    assert solve(250, 10, [
        (13, 218), (17, 99), (24, 180), (53, 115), (96, 97),
        (111, 158), (124, 164), (135, 227), (158, 177), (204, 224)
    ]) == 10
    assert solve(100, 10, [(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11)]) == 0


if __name__ == "__main__":
    test()
    main()
