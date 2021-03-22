from heapq import heappop, heappush
from bisect import bisect_left, bisect_right


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


def solve(n, m, xy_list, a_list):
    h = []
    a_list_s = list(sorted(a_list))
    for x, y in xy_list:
        p = bisect_left(a_list_s, x)
        q = bisect_right(a_list_s, y) - 1
        if p > q:
            continue
        heappush(h, (q, p))
        # [p, q] is ok
    res = 0

    sgt = SegmentTree(m, min, lambda: 1)
    sgt.initialize([0] * m)
    while len(h):
        q, p = heappop(h)
        # print("start", p, q)
        # print(sgt.dat)
        # find minimum index empty
        # print(sgt.query(p, p + 1))
        if sgt.query(p, q + 1) == 1:
            # print("skipped", p, q)
            continue
        left = p
        right = q + 1
        while left + 1 < right:
            middle = (left + right) // 2
            if sgt.query(left, middle) == 1:
                left = middle
            else:
                right = middle
        sgt.set_val(left, 1)
        res += 1
        # print("set", p, q, left)
    return res


def main():
    n, m = map(int, input().split())
    xy_list = [tuple(map(int, input().split())) for _ in range(n)]
    a_list = [int(input()) for _ in range(m)]
    res = solve(n, m, xy_list, a_list)
    print(res)


def test():
    assert solve(3, 3, [(1, 2), (2, 3), (3, 4)], [1, 2, 3]) == 3
    assert solve(3, 3, [(1, 2), (2, 3), (3, 4)], [2, 4, 5]) == 2
    assert solve(3, 4, [(1, 4), (2, 3), (5, 5)], [2, 4, 5, 6]) == 3


if __name__ == "__main__":
    test()
    main()
