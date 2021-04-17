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


def solve(n, m, q, txy_list):
    # value map
    y_list = []
    for t, x, y in txy_list:
        y_list.append(y)
    value_map = dict()
    value_map[0] = 0
    v = 1
    for y in sorted(set(y_list)):
        value_map[y] = v
        v += 1

    len_v = len(value_map.keys()) + 1

    def op_add(x_, y_):
        return x_ + y_

    a_count_tree = SegmentTree(len_v, op=op_add, e=lambda: 0)
    a_count_tree.initialize([0] * len_v)
    a_count_tree.set_val(0, n)
    a_value_tree = SegmentTree(len_v, op=op_add, e=lambda: 0)
    a_value_tree.initialize([0] * len_v)
    b_count_tree = SegmentTree(len_v, op=op_add, e=lambda: 0)
    b_count_tree.initialize([0] * len_v)
    b_count_tree.set_val(0, m)
    b_value_tree = SegmentTree(len_v, op=op_add, e=lambda: 0)
    b_value_tree.initialize([0] * len_v)

    res = 0
    a_list_now = [0] * n
    b_list_now = [0] * m
    res_list = []
    # print(value_map)
    for t, x, y in txy_list:
        if t == 1:
            p = value_map[a_list_now[x - 1]]
            q = value_map[y]

            if p != q:
                a_count_p = a_count_tree.query(p, p + 1)
                a_count_q = a_count_tree.query(q, q + 1)
                a_count_tree.set_val(p, a_count_p - 1)
                a_count_tree.set_val(q, a_count_q + 1)
                a_value_tree.set_val(p, (a_count_p - 1) * a_list_now[x - 1])
                a_value_tree.set_val(q, (a_count_q + 1) * y)

                res -= b_count_tree.query(0, p) * a_list_now[x - 1] + b_value_tree.query(p, len_v)
                res += b_count_tree.query(0, q) * y + b_value_tree.query(q, len_v)
            res_list.append(res)
            a_list_now[x - 1] = y
            # print(t, a_count_tree.dat, a_value_tree.dat)
        else:
            p = value_map[b_list_now[x - 1]]
            q = value_map[y]

            if p != q:
                b_count_p = b_count_tree.query(p, p + 1)
                b_count_q = b_count_tree.query(q, q + 1)
                b_count_tree.set_val(p, b_count_p - 1)
                b_count_tree.set_val(q, b_count_q + 1)
                b_value_tree.set_val(p, (b_count_p - 1) * b_list_now[x - 1])
                b_value_tree.set_val(q, (b_count_q + 1) * y)

                res -= a_count_tree.query(0, p) * b_list_now[x - 1] + a_value_tree.query(p, len_v)
                res += a_count_tree.query(0, q) * y + a_value_tree.query(q, len_v)
            res_list.append(res)
            b_list_now[x - 1] = y
            # print(t, b_count_tree.dat, b_value_tree.dat)
    # print(res_list)

    return res_list


def main():
    n, m, q = map(int, input().split())
    txy_list = [tuple(map(int, input().split())) for _ in range(q)]
    res_list = solve(n, m, q, txy_list)
    for res in res_list:
        print(res)


def test():
    assert solve(2, 2, 4, [(1, 1, 10), (2, 1, 20), (2, 2, 5), (1, 1, 30)]) == [20, 50, 55, 85]
    assert solve(3, 3, 5, [(1, 3, 10), (2, 1, 7), (1, 3, 5), (2, 2, 10), (2, 1, 1)]) == [30, 44, 31, 56, 42]
    assert solve(200000, 200000, 4, [
        (2, 112219, 100000000), (1, 73821, 100000000), (2, 26402, 100000000), (1, 73821, 100000000)
    ]) == [20000000000000, 39999900000000, 59999800000000, 59999800000000]


if __name__ == "__main__":
    test()
    main()
