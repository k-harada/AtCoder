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


def solve(n, lr_list):
    value_list = [0]
    for l, r in lr_list:
        if l > 0:
            value_list.append(l - 1)
        value_list.append(l)
        value_list.append(l + 1)
        value_list.append(r - 1)
        value_list.append(r)
        value_list.append(r + 1)
    value_list_sorted = list(sorted(list(set(value_list))))
    value_map = dict()
    for i, v in enumerate(value_list_sorted):
        value_map[v] = i
    m = len(value_list_sorted)
    pair_list = [[] for _ in range(m)]
    v_list = [0] * m
    right_count = [0] * m
    for l, r in lr_list:
        pair_list[value_map[l]].append(value_map[r])
        v_list[value_map[l] + 1] += 1
        v_list[value_map[r]] -= 1
        right_count[value_map[r]] += 1
    v_list_cum = [0] * m
    for i in range(m - 1):
        v_list_cum[i + 1] = v_list_cum[i] + v_list[i + 1]
    # print(v_list_cum)

    lst = LazySegmentTree(
        m, op=max, e=lambda: 0, act=lambda f, x: f + x, composition=lambda f, g: f + g, idf=lambda: 0
    )
    lst.initialize(v_list_cum)
    max_r = 0
    res_left = 0
    res_right = 1
    for i in range(m):
        # 今leftを踏んだやつ
        for j in pair_list[i]:
            lst.operate_range(i + 1, j, -1)
        # 今leftを踏み越えたやつ
        if i > 0:
            for j in pair_list[i - 1]:
                lst.operate_range(j + 1, m, 1)
        # 今rightを踏んだやつ
        lst.operate_range(i + 1, m, -right_count[i])
        r = lst.query(i + 1, m)

        if r > max_r:
            left = i
            right = m - 1
            while left + 1 < right:
                mid = (left + right) // 2
                if lst.query(i + 1, mid + 1) == r:
                    right = mid
                else:
                    left = mid
            res_left = value_list_sorted[i]
            res_right = value_list_sorted[right]
            max_r = r
            # print(res_left, res_right, max_r)

    return f"{res_left} {res_right}"


def main():
    n = int(input())
    lr_list = [tuple(map(int, input().split())) for _ in range(n)]
    res = solve(n, lr_list)
    print(res)


def test():
    assert solve(5, [(1, 7), (3, 9), (7, 18), (10, 14), (15, 20)]) == "4 11"
    assert solve(11, [
        (856977192, 996441446),
        (298251737, 935869360),
        (396653206, 658841528),
        (710569907, 929136831),
        (325371222, 425309117),
        (379628374, 697340458),
        (835681913, 939343451),
        (140179224, 887672320),
        (375607390, 611397526),
        (93530028, 581033295),
        (249611310, 775998537),
    ]) == "396653207 887672321"
    assert solve(5, [(1, 2), (3, 4), (5, 6), (7, 8), (0, 1)]) == "0 1"
    assert solve(5, [(1, 3), (1, 3), (1, 3), (1, 3), (1, 3)]) == "0 2"


if __name__ == "__main__":
    test()
    main()
