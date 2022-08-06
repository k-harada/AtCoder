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


def e_zero():
    return 0


def solve_sub(y_list):
    m = len(y_list)
    if m <= 1:
        return 0
    # compress
    table = dict()
    v = 0
    for y in sorted(list(set(y_list))):
        table[y] = v
        v += 1

    res = 0

    rev_cnt = SegmentTree(v, op_add, e_zero)
    rev_cnt.initialize([0] * v)
    for y in y_list:
        z = table[y]
        cnt = rev_cnt.query(z, z + 1)
        rev_cnt.set_val(z, cnt + 1)
        res += rev_cnt.query(z + 1, v)

    return res


def solve(n, c_list, x_list):
    x_list_list = [[] for _ in range(n + 1)]
    for c, x in zip(c_list, x_list):
        x_list_list[c].append(x)
    res = solve_sub(x_list)
    # print(res)
    for c in range(n + 1):
        if len(x_list_list[c]) > 1:
            res -= solve_sub(x_list_list[c])
            # print(c, res)
    return res


def main():
    n = int(input())
    c_list = list(map(int, input().split()))
    x_list = list(map(int, input().split()))
    res = solve(n, c_list, x_list)
    print(res)


def test():
    assert solve(5, [1, 5, 2, 2, 1], [3, 2, 1, 2, 1]) == 6
    assert solve(3, [1, 1, 1], [3, 2, 1]) == 0
    assert solve(3, [3, 1, 2], [1, 1, 2]) == 0


def test_large():
    import numpy as np
    print(solve(300000, list(np.random.choice(3000, size=300000)), list(np.random.choice(300000, size=300000))))


if __name__ == "__main__":
    test()
    # test_large()
    main()
