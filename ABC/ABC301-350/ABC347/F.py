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


def solve(n, m, a):
    a_cum_sum = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(n):
            a_cum_sum[i + 1][j + 1] = a_cum_sum[i + 1][j] + a_cum_sum[i][j + 1] - a_cum_sum[i][j] + a[i][j]
    # print(a_cum_sum)
    # 左上に2個置く
    # あるラインより左 -> それより右上
    b = [[0] * (n - m + 1) for _ in range(n - m + 1)]
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            b[i][j] = a_cum_sum[i + m][j + m] - a_cum_sum[i + m][j] - a_cum_sum[i][j + m] + a_cum_sum[i][j]
    b_cum_max_lu = [[0] * (n - m + 1) for _ in range(n - m + 1)]
    b_cum_max_ru = [[0] * (n - m + 1) for _ in range(n - m + 1)]
    b_cum_max_ld = [[0] * (n - m + 1) for _ in range(n - m + 1)]
    b_cum_max_rd = [[0] * (n - m + 1) for _ in range(n - m + 1)]
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            b_cum_max_lu[i][j] = max(b_cum_max_lu[i][j], b[i][j])
            if i > 0:
                b_cum_max_lu[i][j] = max(b_cum_max_lu[i][j], b_cum_max_lu[i - 1][j])
            if j > 0:
                b_cum_max_lu[i][j] = max(b_cum_max_lu[i][j], b_cum_max_lu[i][j - 1])
    for i in range(n - m + 1):
        for j in range(n - m, -1, -1):
            b_cum_max_ru[i][j] = max(b_cum_max_ru[i][j], b[i][j])
            if i > 0:
                b_cum_max_ru[i][j] = max(b_cum_max_ru[i][j], b_cum_max_ru[i - 1][j])
            if j < n - m:
                b_cum_max_ru[i][j] = max(b_cum_max_ru[i][j], b_cum_max_ru[i][j + 1])
    for i in range(n - m, -1, -1):
        for j in range(n - m + 1):
            b_cum_max_ld[i][j] = max(b_cum_max_ld[i][j], b[i][j])
            if i < n - m:
                b_cum_max_ld[i][j] = max(b_cum_max_ld[i][j], b_cum_max_ld[i + 1][j])
            if j > 0:
                b_cum_max_ld[i][j] = max(b_cum_max_ld[i][j], b_cum_max_ld[i][j - 1])
    for i in range(n - m, -1, -1):
        for j in range(n - m, -1, -1):
            b_cum_max_rd[i][j] = max(b_cum_max_rd[i][j], b[i][j])
            if i < n - m:
                b_cum_max_rd[i][j] = max(b_cum_max_rd[i][j], b_cum_max_rd[i + 1][j])
            if j < n - m:
                b_cum_max_rd[i][j] = max(b_cum_max_rd[i][j], b_cum_max_rd[i][j + 1])
    res_1 = 0
    for j in range(n - m + 1 - m):
        for i in range(n - m + 1 - m):
            r = b_cum_max_lu[n - m][j] + b_cum_max_ru[i][j + m] + b_cum_max_rd[i + m][j + m]
            res_1 = max(res_1, r)
    res_2 = 0
    for j in range(n - m + 1 - m):
        for i in range(n - m + 1 - m):
            r = b_cum_max_ru[n - m][j + m] + b_cum_max_lu[i][j] + b_cum_max_ld[i + m][j]
            res_2 = max(res_2, r)
    res_3 = 0
    for i in range(n - m + 1 - m):
        for j in range(n - m + 1 - m):
            r = b_cum_max_lu[i][n - m] + b_cum_max_ld[i + m][j] + b_cum_max_rd[i + m][j + m]
            res_3 = max(res_3, r)
    res_4 = 0
    for i in range(n - m + 1 - m):
        for j in range(n - m + 1 - m):
            r = b_cum_max_ld[i + m][n - m] + b_cum_max_lu[i][j] + b_cum_max_ru[i][j + m]
            res_4 = max(res_4, r)

    max_5_arr = [0] * (n - m + 1)
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            max_5_arr[i] = max(max_5_arr[i], b[i][j])
    sgt_5 = SegmentTree(n - m + 1, op=max, e=lambda: 0)
    sgt_5.initialize(max_5_arr)
    res_5 = 0
    for i in range(n - m + 1):
        for j in range(i + 2 * m, n - m + 1):
            res_5 = max(res_5, sgt_5.query(0, i + 1) + sgt_5.query(i + m, j - m + 1) + sgt_5.query(j, n - m + 1))

    max_6_arr = [0] * (n - m + 1)
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            max_6_arr[j] = max(max_5_arr[j], b[i][j])
    sgt_6 = SegmentTree(n - m + 1, op=max, e=lambda: 0)
    sgt_6.initialize(max_6_arr)
    res_6 = 0
    for i in range(n - m + 1):
        for j in range(i + 2 * m, n - m + 1):
            res_6 = max(res_6, sgt_6.query(0, i + 1) + sgt_6.query(i + m, j - m + 1) + sgt_6.query(j, n - m + 1))

    # print(res_1, res_2, res_3, res_4, res_5, res_6)
    res = max([res_1, res_2, res_3, res_4, res_5, res_6])
    return res


def main():
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    res = solve(n, m, a)
    print(res)


def test():
    assert solve(7, 3, [
        [3, 1, 4, 1, 5, 9, 2],
        [6, 5, 3, 5, 8, 9, 7],
        [9, 3, 2, 3, 8, 4, 6],
        [2, 6, 4, 3, 3, 8, 3],
        [2, 7, 9, 5, 0, 2, 8],
        [8, 4, 1, 9, 7, 1, 6],
        [9, 3, 9, 9, 3, 7, 5],
    ]) == 154
    assert solve(7, 1, [
        [3, 1, 4, 1, 5, 9, 2],
        [6, 5, 3, 5, 8, 9, 7],
        [9, 3, 2, 3, 8, 4, 6],
        [2, 6, 4, 3, 3, 8, 3],
        [2, 7, 9, 5, 0, 2, 8],
        [8, 4, 1, 9, 7, 1, 6],
        [9, 3, 9, 9, 3, 7, 5],
    ]) == 27


if __name__ == "__main__":
    test()
    main()
