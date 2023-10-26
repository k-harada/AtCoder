MOD = 998244353


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


def solve(n, a_list):
    mod_inv = [1]
    for i in range(1, n + 1):
        mod_inv.append(pow(i, MOD - 2, MOD))
    res = [a_list[0]]
    r = a_list[0]
    m = max(a_list) + 1
    c_tree = SegmentTree(m, op=add, e=lambda: 0)
    s_tree = SegmentTree(m, op=add, e=lambda: 0)
    c_tree.set_val(a_list[0], 1)
    s_tree.set_val(a_list[0], a_list[0])

    for i in range(1, n):
        r *= i * i
        r %= MOD
        r *= mod_inv[i + 1]
        r %= MOD
        r *= mod_inv[i + 1]
        r %= MOD

        a = a_list[i]
        c = c_tree.query(a, m)
        s = s_tree.query(a, m)
        # print(c, s)
        r += (2 * (s + (i - c) * a) * mod_inv[i + 1] * mod_inv[i + 1]) % MOD
        r %= MOD
        r += (a * mod_inv[i + 1] * mod_inv[i + 1]) % MOD
        r %= MOD
        res.append(r)

        c_a = c_tree.query(a, a + 1)
        s_a = s_tree.query(a, a + 1)
        c_tree.set_val(a, c_a + 1)
        s_tree.set_val(a, s_a + a)

    # print(res)
    return res


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    for r in res:
        print(r)


def test():
    assert solve(3, [5, 7, 5]) == [5, 499122183, 443664163]
    assert solve(7, [22, 75, 26, 45, 72, 81, 47]) == [
        22, 249561150, 110916092, 873463862, 279508479, 360477194, 529680742
    ]


if __name__ == "__main__":
    test()
    main()
