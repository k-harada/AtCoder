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


def solve(n, p_list):
    g = [[] for _ in range(n)]
    sgt = SegmentTree(n, op=max, e=lambda: 0)
    m = 0
    cum_max = []
    for p in p_list:
        m = max(m, p)
        cum_max.append(m)
    cum_max_rev = []
    m = 0
    for p in reversed(p_list):
        m = max(m, p)
        cum_max_rev.append(m)
    cum_max_rev = list(reversed(cum_max_rev))
    sgt.initialize(p_list)
    for i in range(n):
        # left
        if cum_max[i] == p_list[i]:
            pass
        elif p_list[i - 1] > p_list[i]:
            g[i].append(i - 1)
        else:
            right = i - 1
            left = 0
            while left + 1 < right:
                mid = (right + left) // 2
                v = sgt.query(mid, i)
                if v < p_list[i]:
                    right = mid
                else:
                    left = mid
            g[i].append(left)

        # right
        if cum_max_rev[i] == p_list[i]:
            pass
        elif p_list[i + 1] > p_list[i]:
            g[i].append(i + 1)
        else:
            left = i + 1
            right = n - 1
            while left + 1 < right:
                mid = (right + left) // 2
                v = sgt.query(i + 1, mid + 1)
                if v < p_list[i]:
                    left = mid
                else:
                    right = mid
            g[i].append(right)
    # print(g)
    res_list = [0] * n
    p_list_rev = [0] * n
    for i, p in enumerate(p_list):
        p_list_rev[p - 1] = i
    for i in range(n):
        p = p_list_rev[i]
        for q in g[p]:
            res_list[q] = max(res_list[q], res_list[p] + abs(p - q))
    # print(res_list)
    return res_list[p_list_rev[n - 1]]


def main():
    n = int(input())
    p_list = list(map(int, input().split()))
    res = solve(n, p_list)
    print(res)


def test():
    assert solve(5, [5, 3, 4, 1, 2]) == 5
    assert solve(3, [1, 3, 2]) == 1
    assert solve(5, [5, 3, 1, 2, 4]) == 10


if __name__ == "__main__":
    test()
    main()
