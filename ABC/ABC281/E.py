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


def op_add(x, y):
    return x + y


def solve(n, m, k, a_list):
    sgc = SegmentTree(n, op=op_add, e=lambda: 0)
    sgc.initialize([0] * n)
    sgv = SegmentTree(n, op=op_add, e=lambda: 0)
    sgv.initialize([0] * n)

    a_list_s = list(sorted(a_list))
    a_list_args = list(sorted([(a, i) for i, a in enumerate(a_list)]))
    a_list_index = [0] * n
    for i in range(n):
        _, j = a_list_args[i]
        a_list_index[j] = i

    # initialize
    res = []
    for i in range(m):
        j = a_list_index[i]
        sgc.set_val(j, 1)
        sgv.set_val(j, a_list[i])

    # にぶたんして値を求める
    left = 0
    right = n
    while left + 1 < right:
        mid = (left + right) // 2
        if sgc.query(0, mid) < k:
            left = mid
        else:
            right = mid
    res.append(sgv.query(0, right))

    for i in range(n - m):
        j = a_list_index[i]
        sgc.set_val(j, 0)
        sgv.set_val(j, 0)
        j = a_list_index[i + m]
        sgc.set_val(j, 1)
        sgv.set_val(j, a_list[i + m])
        # にぶたんして値を求める
        left = 0
        right = n
        while left + 1 < right:
            mid = (left + right) // 2
            if sgc.query(0, mid) < k:
                left = mid
            else:
                right = mid
        res.append(sgv.query(0, right))
    return " ".join([str(r) for r in res])


def main():
    n, m, k = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, m, k, a_list)
    print(res)


def test():
    assert solve(6, 4, 3, [3, 1, 4, 1, 5, 9]) == "5 6 10"
    assert solve(10, 6, 3, [12, 2, 17, 11, 19, 8, 4, 3, 6, 20]) == "21 14 15 13 13"


def test_large():
    print(solve(200000, 150000, 50000, list(range(200000))))


if __name__ == "__main__":
    test()
    # test_large()
    main()
