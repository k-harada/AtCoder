from heapq import heappop, heappush


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


def solve(h, w, m, xy_list):
    # x1_min, y1_min
    x1_min = w + 1
    y1_min = h + 1
    for x, y in xy_list:
        if x == 1:
            x1_min = min(x1_min, y)
        if y == 1:
            y1_min = min(y1_min, x)

    # 1 <= x < y1_min and 1 <= y < x1_min
    heap = []
    for x, y in xy_list:
        if x < y1_min and y < x1_min:
            heappush(heap, (x, y))

    # seg_tree
    sg = SegmentTree(x1_min, op=add, e=lambda: 0)
    last_x = -1
    res = h * w
    while len(heap):
        x, y = heappop(heap)
        if last_x != x:
            res -= sg.query(y, x1_min)
        if sg.query(y, y + 1) == 0:
            res -= 1
            sg.set_val(y, 1)
        last_x = x
    # print(res)

    # y >= x1_min
    heap = []
    for x, y in xy_list:
        heappush(heap, (x, y))
    last_x = -1
    while len(heap):
        x, y = heappop(heap)
        if x >= y1_min:
            break
        if last_x != x:
            if y < x1_min:
                res -= w - x1_min + 1
            else:
                res -= w - y + 1
        last_x = x
    # print(res)

    # x >= y1_min
    heap = []
    for x, y in xy_list:
        heappush(heap, (y, x))
    last_y = -1
    while len(heap):
        y, x = heappop(heap)
        if y >= x1_min:
            break
        if last_y != y:
            if x < y1_min:
                res -= h - y1_min + 1
            else:
                res -= h - x + 1
        last_y = y
    # print(res)

    # zone 4
    res -= (h - y1_min + 1) * (w - x1_min + 1)
    # print(res)
    return res


def main():
    h, w, m = map(int, input().split())
    xy_list = [tuple(map(int, input().split())) for _ in range(m)]
    res = solve(h, w, m, xy_list)
    print(res)


def test():
    assert solve(4, 3, 2, [(2, 2), (3, 3)]) == 10
    assert solve(5, 4, 4, [(3, 2), (3, 4), (4, 2), (5, 2)]) == 14
    assert solve(200000, 200000, 0, []) == 40000000000


if __name__ == "__main__":
    test()
    main()
