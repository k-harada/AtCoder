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


MOD = 998244353
MOD_INV_9 = pow(9, MOD - 2, MOD)


def op_con(x, y):
    if y[1] == 0:
        return x
    elif x[1] == 0:
        return y
    else:
        return (x[0] * y[1] + y[0]) % MOD, (x[1] * y[1]) % MOD


def e_zero():
    return 0, 0


def act_change(f, x):
    if f == 0:
        return x
    else:
        return ((x[1] - 1) * MOD_INV_9 * f) % MOD, x[1]


def com_change(f, g):
    if g == 0:
        return f
    else:
        return g


def idf_change():
    return 0


def solve(n, q, lrd_list):

    lsq = LazySegmentTree(n, op_con, e_zero, act=act_change, composition=com_change, idf=idf_change)
    lsq.initialize([(1, 10)] * n)

    res = []

    for i in range(q):
        l, r, d = lrd_list[i]
        # find where
        lsq.operate_range(l - 1, r, d)
        res.append(lsq.query(0, n)[0])

    return res


def solve_greedy(n, q, lrd_list):
    assert n <= 12 or q <= 10
    rep = [1] * n

    res = []

    for i in range(q):
        l, r, d = lrd_list[i]
        for j in range(l - 1, r):
            rep[j] = d
        res.append(int("".join([str(k) for k in rep])) % MOD)

    return res


def main():
    n, q = map(int, input().split())
    lrd_list = [tuple(map(int, input().split())) for _ in range(q)]
    res = solve(n, q, lrd_list)
    for r in res:
        print(r)


def test():
    assert solve(8, 5, [(3, 6, 2), (1, 4, 7), (3, 8, 3), (2, 2, 2), (4, 5, 1)]) == [11222211, 77772211, 77333333,
                                                                                    72333333, 72311333]
    assert solve(200000, 1, [(123, 456, 7)]) == [641437905]
    assert solve_greedy(8, 5, [(3, 6, 2), (1, 4, 7), (3, 8, 3), (2, 2, 2), (4, 5, 1)]) == [11222211, 77772211, 77333333,
                                                                                    72333333, 72311333]
    assert solve_greedy(200000, 1, [(123, 456, 7)]) == [641437905]
    assert solve_greedy(12, 1, [(4, 9, 3)]) == solve(12, 1, [(4, 9, 3)])


def test_random():
    import random
    for i in range(10):
        rand_list = []
        for _ in range(5):
            p = random.choice(list(range(12))) + 1
            q = random.choice(list(range(12))) + 1
            p, q = min(p, q), max(p, q)
            r = random.choice(list(range(9))) + 1
            rand_list.append((p, q, r))
        if solve(12, 5, rand_list) == solve_greedy(12, 5, rand_list):
            print("pass", i + 1)
        else:
            print(rand_list, solve(12, 5, rand_list), solve_greedy(12, 5, rand_list))


def test_493():
    n = 12
    lsq = LazySegmentTree(n, op_con, e_zero, act=act_change, composition=com_change, idf=idf_change)
    lsq.initialize([(1, 10)] * n)
    print(lsq.n)
    print(lsq.dat_f, lsq.dat_v)
    l, r, d = 4, 9, 3
    # find where
    lsq.operate_range(l - 1, r, d)
    print(lsq.dat_f, lsq.dat_v)
    print(lsq.query(0, 8)[0], lsq.query(8, 12)[0])
    print(lsq.dat_f, lsq.dat_v)


if __name__ == "__main__":
    # test_493()
    test()
    # test_random()
    main()
