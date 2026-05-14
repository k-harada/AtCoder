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


def solve(n, m, a_list, b_list, c_list, d_list):
    # n + m 個に横の大きい順に番号をつけてindexを振る
    # 並んだら箱の方が必ずチョコより大きくなるように
    status_list = []
    for i in range(n):
        status_list.append((-b_list[i], 1, i))
    for j in range(m):
        status_list.append((-d_list[j], 0, j))
    status_list_s = list(sorted(status_list))
    status_list_mod = []
    for i, q in enumerate(status_list_s):
        _, flag, ij = q
        if flag == 1:
            status_list_mod.append((-a_list[ij], 0, n + m - 1 - i))
        else:
            status_list_mod.append((-c_list[ij], -1, n + m - 1 - i))
    status_list_mod_s = list(sorted(status_list_mod))
    rmq = SegmentTree(n + m, op=min, e=lambda: n + m)
    rmq.initialize([n + m] * (n + m))
    res = "Yes"
    for s in status_list_mod_s:
        # print(s)
        _, flag, k = s
        if flag == -1:
            rmq.set_val(k, k)
        else:
            r = rmq.query(k, n + m)
            if r == n + m:
                res = "No"
                return res
            else:
                rmq.set_val(r, n + m)
    return res


def main():
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    c_list = list(map(int, input().split()))
    d_list = list(map(int, input().split()))
    res = solve(n, m, a_list, b_list, c_list, d_list)
    print(res)


def test():
    assert solve(2, 3, [2, 4], [3, 2], [8, 1, 5], [2, 10, 5]) == "Yes"
    assert solve(2, 2, [1, 1], [2, 2], [100, 1], [100, 1]) == "No"
    assert solve(1, 1, [10], [100], [100], [10]) == "No"
    assert solve(1, 1, [10], [100], [10], [100]) == "Yes"


if __name__ == "__main__":
    test()
    main()
