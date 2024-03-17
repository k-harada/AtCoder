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


def solve(n, k, p_list):
    size = n
    factorial = [1] * (size + 1)
    factorial_inv = [1] * (size + 1)
    for i in range(1, size + 1):
        factorial[i] = (factorial[i - 1] * i) % MOD

    factorial_inv[-1] = pow(factorial[-1], MOD - 2, MOD)

    for i in range(size, 0, -1):
        factorial_inv[i - 1] = (factorial_inv[i] * i) % MOD

    res = [-1] * n
    # 辞書順でP以下を全部数える
    p_count = [0] * (k + 1)
    sgt = SegmentTree(length=n, op=lambda x, y: (x + y) % MOD, e=lambda: 0)
    sgt.initialize([1] * n)
    for i, p in enumerate(p_list):
        c = sgt.query(0, p - 1)
        p_count[i] = c * factorial[n - i - 1] * factorial_inv[n - k]
        p_count[i] %= MOD
        sgt.set_val(p - 1, 0)
    p_count[-1] = 1
    # print(p_count)
    p_count_sum = [0] * (k + 1)
    p_count_sum[-1] = 1
    for i in range(k - 1, -1, -1):
        p_count_sum[i] = (p_count_sum[i + 1] + p_count[i]) % MOD
    # print(p_count_sum)
    sgt = SegmentTree(length=n, op=lambda x, y: (x + y) % MOD, e=lambda: 0)
    sgt.initialize([1] * n)
    lst = LazySegmentTree(
        length=n, op=max, e=lambda: 0,
        act=lambda f, x: (f + x) % MOD, composition=lambda f, g: (f + g) % MOD, idf=lambda: 0
    )
    lst.initialize([0] * n)
    for i, p in enumerate(p_list):
        c = sgt.query(0, p - 1)
        # pより小さいところ
        x1 = (factorial[n - i - 1] * factorial_inv[n - k]) % MOD
        x2 = ((c - 1) * (k - i - 1) * factorial[n - i - 2] * factorial_inv[n - k]) % MOD
        # print(x1, x2)
        lst.operate_range(0, p - 1, (x1 + x2) % MOD)
        # pより大きいところ
        x1 = 0
        x2 = (c * (k - i - 1) * factorial[n - i - 2] * factorial_inv[n - k]) % MOD
        # print(x1, x2)
        lst.operate_range(p - 1, n, (x1 + x2) % MOD)
        # pちょうどの場合はこの時点で処理終了
        # print("finish", p)
        # print(lst.query(p - 1, p), p_count_sum[i + 1])
        res[p - 1] = (lst.query(p - 1, p) + p_count_sum[i + 1]) % MOD
        # print(p, res[p - 1])
        sgt.set_val(p - 1, 0)
    for i in range(n):
        if res[i] < 0:
            res[i] = lst.query(i, i + 1) % MOD
    # print(res)
    return res


def main():
    n, k = map(int, input().split())
    p_list = list(map(int, input().split()))
    res = solve(n, k, p_list)
    for r in res:
        print(r)


def test():
    assert solve(4, 2, [3, 2]) == [5, 5, 4, 2]
    assert solve(18, 13, [5, 13, 11, 2, 18, 1, 10, 15, 17, 4, 12, 7, 3]) == [
        925879409,
        905921009,
        665544804,
        665544719,
        783035803,
        349952762,
        349952758,
        349952757,
        349952757,
        349921178,
        212092637,
        710350150,
        378895603,
        129113201,
        129111892,
        129098081,
        129096772,
        110181652,
    ]


if __name__ == "__main__":
    test()
    main()
