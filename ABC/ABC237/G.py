class LazySegmentTree:
    # 0-indexed
    # 2^m
    # ref. https://yukicoder.me/submissions/470340
    def __init__(self, length, op=min, e=lambda: 0, act=lambda f, x: f if f != 0 else x, composition=lambda f, g: g, idf=lambda: 0):
        """
        :param length: length of initial values
        :param op: operator, op(x, y) -> z
        :param e: function that return identity element for op
        """
        self.op = op
        self.e = e
        self.act = act
        self.composition = composition
        self.n = 1
        self.idf = idf
        while self.n < length:
            self.n *= 2  # pow2
        self.dat_v = [self.e()] * (2 * self.n - 1)
        self.dat_f = [self.idf()] * (2 * self.n - 1)

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
            self.dat_v[self.n - 1 + i] = x
        # upper values
        for i in range(self.n - 2, -1, -1):
            self.dat_v[i] = self.op(self.dat_v[2 * i + 1], self.dat_v[2 * i + 2])

    def _eval_at(self, i):
        return self.act(self.dat_f[i], self.dat_v[i])

    def _propagate_at(self, i):
        self.dat_v[i] = self._eval_at(i)
        self.dat_f[i * 2 + 1] = self.composition(self.dat_f[i * 2 + 1], self.dat_f[i])
        self.dat_f[i * 2 + 2] = self.composition(self.dat_f[i * 2 + 2], self.dat_f[i])
        self.dat_f[i] = self.idf()

    def _propagate_above(self, i):
        history = []
        while i > 0:
            i = (i - 1) // 2
            history.append(i)
        for j in reversed(history):
            self._propagate_at(j)

    def _re_calculate_above(self, i):
        while i > 0:
            i = (i - 1) // 2
            self.dat_v[i] = self.op(self._eval_at(2 * i + 1), self._eval_at(2 * i + 2))

    def operate_range(self, p, q, f):
        """
        apply operator f for [p, q)
        :param p: int
        :param q: int
        :param f: operator
        :return: None
        """
        if p >= q:
            return None
        p0 = p + self.n - 1
        q0 = q + self.n - 2
        # propagate from top
        self._propagate_above(p0)
        self._propagate_above(q0)
        # compose f
        while q0 - p0 > 1:
            if p0 & 1 == 0:
                self.dat_f[p0] = self.composition(self.dat_f[p0], f)
            if q0 & 1 == 1:
                self.dat_f[q0] = self.composition(self.dat_f[q0], f)
                q0 -= 1
            p0 = p0 // 2
            q0 = (q0 - 1) // 2
        if p0 == q0:
            self.dat_f[p0] = self.composition(self.dat_f[p0], f)
        elif p0 & 1 == 1:
            self.dat_f[p0 // 2] = self.composition(self.dat_f[p0 // 2], f)
        else:
            self.dat_f[p0] = self.composition(self.dat_f[p0], f)
            self.dat_f[q0] = self.composition(self.dat_f[q0], f)
        # re-calculate above
        self._re_calculate_above(p + self.n - 1)
        self._re_calculate_above(q + self.n - 2)

    def set_val(self, k, v):
        """
        update k-th(0-indexed) value with v
        :param k: index to set(0-indexed)
        :param v: value to set
        :return: None
        """
        k += self.n - 1
        self.dat_v[k] = v
        self.dat_f[k] = self.idf()
        self._re_calculate_above(k)

    def query(self, p, q):
        """
        :param p: int
        :param q: int
        :return: "minimum" value in [p, q)
        """
        if q <= p:
            return self.e()
        p0 = p + self.n - 1
        q0 = q + self.n - 2
        self._propagate_above(p0)
        self._propagate_above(q0)
        vl = self.e()
        vr = self.e()
        while q0 - p0 > 1:
            if p0 & 1 == 0:
                vl = self.op(vl, self._eval_at(p0))
            if q0 & 1 == 1:
                vr = self.op(self._eval_at(q0), vr)
                q0 -= 1
            p0 = p0 // 2
            q0 = (q0 - 1) // 2
        if p0 == q0:
            res = self.op(self.op(vl, self._eval_at(p0)), vr)
        else:
            res = self.op(self.op(vl, self._eval_at(p0)), self.op(self._eval_at(q0), vr))
        return res


def op_add(x, y):
    return x + y


def e_zero():
    return 0


def act_change(f, x):
    if f == 0:
        return x
    else:
        return f


def com_change(f, g):
    if g == 0:
        return f
    else:
        return g


def idf_change():
    return 0


def solve(n, q, x, p_list, query_list):
    v = []
    ind_x = 0
    for i, p in enumerate(p_list):
        if p < x:
            v.append(-1)
        elif p == x:
            v.append(2)
            ind_x = i
        else:
            v.append(1)

    lsq = LazySegmentTree(n, op_add, e_zero, act=act_change, composition=com_change, idf=idf_change)
    lsq.initialize(v)

    # print([lsq.query(i, i + 1) for i in range(n)])

    for c, l, r in query_list:
        vs = lsq.query(l - 1, r)
        # print(vs)
        if c == 1:
            if l - 1 <= ind_x <= r - 1:
                count_n = (r - l + 1 - 1 - vs + 2) // 2
                count_p = r - l + 1 - 1 - count_n
                ind_x = l - 1 + count_n
                lsq.operate_range(l - 1, l - 1 + count_n, -1)
                lsq.operate_range(r - count_p, r, 1)
                lsq.operate_range(ind_x, ind_x + 1, 2)
            else:
                count_n = (r - l + 1 - vs) // 2
                count_p = r - l + 1 - count_n
                lsq.operate_range(l - 1, l - 1 + count_n, -1)
                lsq.operate_range(r - count_p, r, 1)
        else:
            if l - 1 <= ind_x <= r - 1:
                count_n = (r - l + 1 - 1 - vs + 2) // 2
                count_p = r - l + 1 - 1 - count_n
                ind_x = l - 1 + count_p
                lsq.operate_range(l - 1, l - 1 + count_p, 1)
                lsq.operate_range(r - count_n, r, -1)
                lsq.operate_range(ind_x, ind_x + 1, 2)
            else:
                count_n = (r - l + 1 - vs) // 2
                count_p = r - l + 1 - count_n
                lsq.operate_range(l - 1, l - 1 + count_p, 1)
                lsq.operate_range(r - count_n, r, -1)
        # print([lsq.query(i, i + 1) for i in range(n)])

    return ind_x + 1


def main():
    n, q, x = map(int, input().split())
    p_list = list(map(int, input().split()))
    query_list = [tuple(map(int, input().split())) for _ in range(q)]
    res = solve(n, q, x, p_list, query_list)
    print(res)


def test():
    assert solve(5, 2, 1, [1, 4, 5, 2, 3], [(1, 3, 5), (2, 1, 3)]) == 3
    assert solve(7, 3, 3, [7, 5, 3, 1, 2, 4, 6], [(1, 1, 7), (2, 3, 6), (2, 5, 7)]) == 7


def test_large():
    r = solve(200000, 200000, 200000, list(range(1, 200001)), [(1, 1, 200000)] * 200000)
    print(r)


if __name__ == "__main__":
    test()
    # test_large()
    main()
