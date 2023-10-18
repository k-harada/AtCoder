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


def add(x, y):
    return x + y


def solve(n, c_list, x_list):
    res_all = 0
    xi_list = [(i, x) for i, x in enumerate(x_list)]
    xi_list_s = list(sorted(xi_list, key=lambda x: (x[1], x[0]), reverse=True))
    sgt = SegmentTree(n, op=add)
    # print(xi_list_s)
    for i, x in xi_list_s:
        res_all += sgt.query(0, i)
        sgt.set_val(i, 1)
    # print(res_all)
    for i in range(n):
        sgt.set_val(i, 0)

    # 色ごとにする
    xic_list = [[] for _ in range(n + 1)]
    for i in range(n):
        xic_list[c_list[i]].append((i, x_list[i]))
    # print(xic_list)

    res_color = 0
    for c in range(n + 1):
        if len(xic_list[c]) == 0:
            continue
        xi_list_s = list(sorted(xic_list[c], key=lambda x: (x[1], x[0]), reverse=True))
        for i, x in xi_list_s:
            res_color += sgt.query(0, i)
            sgt.set_val(i, 1)
        for i, x in xi_list_s:
            sgt.set_val(i, 0)

    return res_all - res_color


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


if __name__ == "__main__":
    test()
    main()
