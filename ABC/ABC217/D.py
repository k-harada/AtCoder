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


def op_max(a, b):
    return max(a, b)


def op_min(a, b):
    return min(a, b)


def solve(l, q, cx_list):
    x_list = [0, l]
    for c, x in cx_list:
        x_list.append(x)
    x_list_s = list(sorted(list(set(x_list))))
    m = len(x_list_s)
    x_dict_s_inv = dict()
    for i, x in enumerate(x_list_s):
        x_dict_s_inv[x] = i

    # print(x_list_s)

    max_tree = SegmentTree(m, op=op_max, e=lambda: 0)
    max_tree.initialize([0] * m)
    min_tree = SegmentTree(m, op=op_min, e=lambda: l)
    min_tree.initialize([l] * m)

    res_list = []

    for c, x in cx_list:
        if c == 1:
            max_tree.set_val(x_dict_s_inv[x], x)
            min_tree.set_val(x_dict_s_inv[x], x)
            # print(min_tree.query(0, m), max_tree.query(0, m))
        else:
            p = x_dict_s_inv[x]
            left = max_tree.query(0, p)
            right = min_tree.query(p + 1, m)
            res_list.append(right - left)
    # print(res_list)
    return res_list


def main():
    l, q = map(int, input().split())
    cx_list = [tuple(map(int, input().split())) for _ in range(q)]
    res = solve(l, q, cx_list)
    for r in res:
        print(r)


def test():
    assert solve(5, 3, [(2, 2), (1, 3), (2, 2)]) == [5, 3]
    assert solve(5, 3, [(1, 2), (1, 4), (2, 3)]) == [2]


if __name__ == "__main__":
    test()
    main()
