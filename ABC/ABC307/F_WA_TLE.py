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


def solve(n, m, uvw_list, k, a_list, d, x_list):
    rmq = SegmentTree(d, op=max, e=lambda: 0)
    rmq.initialize(x_list)

    def find_min(i, x):
        if rmq.query(i, d) < x:
            return -1
        left = i
        right = d
        while left + 1 < right:
            mid = (left + right) // 2
            if rmq.query(i, mid) >= x:
                right = mid
            else:
                left = mid
        return left

    g = [[] for _ in range(n + 1)]
    for u, v, w in uvw_list:
        g[u].append((v, w))
        g[v].append((u, w))
    res = [-1] * (n + 1)
    h = []
    for a in a_list:
        heappush(h, (0, a, 0))
    while len(h):
        d_, p, wd = heappop(h)
        if res[p] >= 0:
            continue
        res[p] = d_
        for q, w in g[p]:
            if wd >= w:
                if res[q] == -1:
                    heappush(h, (d_, q, wd - w))
            else:
                dd_ = find_min(d_, w)
                # print(d_, w, p, q, dd_)
                if dd_ == -1:
                    continue
                elif res[q] == -1:
                    heappush(h, (dd_ + 1, q, x_list[dd_] - w))
    # print(res)
    return res[1:]


def main():
    n, m = map(int, input().split())
    uvw_list = [tuple(map(int, input().split())) for _ in range(m)]
    k = int(input())
    a_list = list(map(int, input().split()))
    d = int(input())
    x_list = list(map(int, input().split()))
    res = solve(n, m, uvw_list, k, a_list, d, x_list)
    for r in res:
        print(r)


def test():
    assert solve(4, 4, [(1, 2, 2), (2, 3, 1), (2, 4, 3), (3, 4, 2)], 1, [1], 2, [3, 3]) == [0, 1, 1, 2]
    assert solve(
        7, 7, [(1, 2, 2), (2, 3, 3), (3, 4, 1), (4, 5, 1), (5, 6, 3), (3, 7, 1), (4, 7, 1)],
        2, [1, 6], 2, [2, 3]
    ) == [0, 1, 2, -1, 2, 0, -1]
    assert solve(5, 1, [(1, 2, 5)], 2, [1, 3], 3, [3, 7, 5]) == [0, 2, 0, -1, -1]


if __name__ == "__main__":
    # test()
    main()
