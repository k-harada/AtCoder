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


def solve(n, polygon_list, q, xy_list):

    all_edge_list = []
    lst = LazySegmentTree(10 ** 5 + 1, op=lambda x, y: x + y, e=lambda: 0, act=lambda f, x: f + x, composition=lambda f, g: f + g, idf=lambda: 0)
    lst.initialize([0] * (10 ** 5 + 1))

    for polygon in polygon_list:
        m = len(polygon)
        edge_list = []
        for i in range(0, m, 2):
            x_base = polygon[i][0]
            y_min = min(polygon[i][1], polygon[i + 1][1])
            y_max = max(polygon[i][1], polygon[i + 1][1])
            edge_list.append((x_base, y_min, y_max))
        edge_list_s = sorted(edge_list, key=lambda v: v[0])
        for x_base, y_min, y_max in edge_list_s:
            if lst.query(y_min, y_min + 1) == 1:
                lst.operate_range(y_min, y_max, -1)
                all_edge_list.append((x_base, y_min, y_max, -1))
            else:
                lst.operate_range(y_min, y_max, 1)
                all_edge_list.append((x_base, y_min, y_max, 1))
    res = [0] * q
    for i in range(q):
        x, y = xy_list[i]
        all_edge_list.append((x, -1, y, i))

    all_edge_list_s = sorted(all_edge_list, key=lambda x: x[0] * 1000000 - x[1])
    for x_base, y_min, y_max, c in all_edge_list_s:
        if y_min == -1:
            res[c] = lst.query(y_max, y_max + 1)
        else:
            lst.operate_range(y_min, y_max, c)
    # print(res)
    return res


def main():
    n = int(input())
    polygon_list = []
    for _ in range(n):
        m = int(input())
        xy = list(map(int, input().split()))
        polygon_list.append([(xy[2 * i], xy[2 * i + 1]) for i in range(m)])
    q = int(input())
    xy_list = [tuple(map(int, input().split())) for _ in range(q)]
    res = solve(n, polygon_list, q, xy_list)
    for r in res:
        print(r)


def test():
    assert solve(3, [
        [(1, 2), (1, 4), (3, 4), (3, 2)], [(2, 5), (2, 3), (5, 3), (5, 5)], [(5, 6), (5, 5), (3, 5), (3, 6)]
    ], 3, [(1, 4), (2, 3), (4, 5)]) == [0, 2, 1]


if __name__ == "__main__":
    test()
    main()
