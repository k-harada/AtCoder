from bisect import bisect_left


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


def solve(n, m, a_list):
    a_sep = [[] for _ in range(m + 1)]

    # 元の値をとる
    a_min_tree = SegmentTree(n, op=min, e=lambda: m + 1)
    a_min_tree.initialize(a_list)

    # 後ろにいくつあるか
    back_v = [0] * (m + 1)
    back_v[0] = n + 1
    for i, a in enumerate(a_list):
        back_v[a] = max(back_v[a], i)
        a_sep[a].append(i)
    b_min_tree = SegmentTree(m + 1, op=min, e=lambda: n + 1)
    b_min_tree.initialize(back_v)
    # print(back_v)
    res = []
    left = 0
    for _ in range(m):
        r = b_min_tree.query(0, m + 1)
        a = a_min_tree.query(left, r + 1)
        res.append(a)
        # update
        for k in a_sep[a]:
            a_min_tree.set_val(k, m + 1)
        b_min_tree.set_val(a, n + 1)
        found_i = bisect_left(a_sep[a], left)
        left = a_sep[a][found_i]
    # print(res)
    return " ".join([str(r) for r in res])


def main():
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, m, a_list)
    print(res)


def test():
    assert solve(4, 3, [2, 3, 1, 3]) == "2 1 3"
    assert solve(4, 4, [2, 3, 1, 4]) == "2 3 1 4"
    assert solve(20, 10, [6, 3, 8, 5, 8, 10, 9, 3, 6, 1, 8, 3, 3, 7, 4, 7, 2, 7, 8, 5]) == "3 5 8 10 9 6 1 4 2 7"


if __name__ == "__main__":
    test()
    main()
