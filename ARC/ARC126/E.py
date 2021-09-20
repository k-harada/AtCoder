MOD = 998244353
INV2 = pow(2, MOD - 2, MOD)


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


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


def solve(n, q, a_list, xy_list):
    res = []
    v_list = [a for a in a_list]
    # fast read
    v_uni = list(sorted(list(set(v_list + [y for x, y in xy_list]))))
    v_map = {v: i for i, v in enumerate(v_uni)}
    m = len(v_uni)
    v_sgt = SegmentTree(len(v_uni), op=op_add, e=lambda: 0)
    c_sgt = SegmentTree(len(v_uni), op=op_add, e=lambda: 0)
    # initialize
    x_list = [0] * m
    c_list = [0] * m
    for a in a_list:
        x_list[v_map[a]] += a
        c_list[v_map[a]] += 1
    v_sgt.initialize(x_list)
    c_sgt.initialize(c_list)

    # initialize s2 (2 * s)
    s = 0
    a_list_s = list(sorted(a_list))
    s_left = 0
    for i, a in enumerate(a_list_s):
        s += (a * i) - s_left
        s_left += a
    # print(s)

    for x, y in xy_list:

        k1 = v_map[v_list[x - 1]]
        k2 = v_map[y]

        v_sgt.set_val(k1, v_sgt.query(k1, k1 + 1) - v_list[x - 1])
        c_sgt.set_val(k1, c_sgt.query(k1, k1 + 1) - 1)

        v_large = v_sgt.query(k1, m)
        c_large = c_sgt.query(k1, m)
        v_small = v_sgt.query(0, k1)
        c_small = c_sgt.query(0, k1)

        s -= v_large - c_large * v_list[x - 1]
        s -= c_small * v_list[x - 1] - v_small

        v_sgt.set_val(k2, v_sgt.query(k2, k2 + 1) + y)
        c_sgt.set_val(k2, c_sgt.query(k2, k2 + 1) + 1)

        v_large = v_sgt.query(k2, m)
        c_large = c_sgt.query(k2, m)
        v_small = v_sgt.query(0, k2)
        c_small = c_sgt.query(0, k2)

        s += v_large - c_large * y
        s += c_small * y - v_small

        v_list[x - 1] = y
        # print(v_list)
        # print(s)

        r = s * INV2
        res.append(r % MOD)
    # print(res)
    return res


def main():
    n, q = map(int, input().split())
    a_list = list(map(int, input().split()))
    xy_list = [tuple(map(int, input().split())) for _ in range(q)]
    res = solve(n, q, a_list, xy_list)
    for r in res:
        print(r)


def test():
    assert solve(3, 4, [7, 5, 5], [(1, 5), (2, 6), (1, 7), (3, 5)]) == [0, 1, 2, 2]
    assert solve(2, 4, [1, 2], [(2, 5), (1, 3), (1, 2), (2, 3)]) == [2, 1, 499122178, 499122177]


if __name__ == "__main__":
    test()
    main()
