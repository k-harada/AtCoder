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


def solve(h, w, q, rc_list):
    status = [1] * (h * w)
    status_min = SegmentTree(h * w, min, lambda: h * w)
    status_min.initialize(list(range(h * w)))
    status_max = SegmentTree(h * w, max, lambda: -1)
    status_max.initialize(list(range(h * w)))

    status_min_t = SegmentTree(h * w, min, lambda: h * w)
    status_min_t.initialize(list(range(h * w)))
    status_max_t = SegmentTree(h * w, max, lambda: -1)
    status_max_t.initialize(list(range(h * w)))
    for r, c in rc_list:
        # not transposed
        x = w * (r - 1) + c - 1
        left = w * (r - 1)
        right = w * r
        # transposed
        x_t = h * (c - 1) + r - 1
        left_t = h * (c - 1)
        right_t = h * c
        if status_max.query(x, x + 1) != -1:
            status_max.set_val(x, -1)
            status_min.set_val(x, h * w)
            status_max_t.set_val(x_t, -1)
            status_min_t.set_val(x_t, h * w)
            status[x] = 0
        else:
            left_w = status_max.query(left, x)
            if left_w >= 0:
                left_w_t = (left_w % w) * h + (left_w // w)
                status_max.set_val(left_w, -1)
                status_min.set_val(left_w, h * w)
                status_max_t.set_val(left_w_t, -1)
                status_min_t.set_val(left_w_t, h * w)
                status[left_w] = 0
                # print(1, left_w // w, left_w % w)

            right_w = status_min.query(x, right)
            if right_w < h * w:
                right_w_t = (right_w % w) * h + (right_w // w)
                status_max.set_val(right_w, -1)
                status_min.set_val(right_w, h * w)
                status_max_t.set_val(right_w_t, -1)
                status_min_t.set_val(right_w_t, h * w)
                status[right_w] = 0
                # print(2, right_w // w, right_w % w)

            left_w_t = status_max_t.query(left_t, x_t)
            if left_w_t >= 0:
                left_w = (left_w_t % h) * w + (left_w_t // h)
                status_max.set_val(left_w, -1)
                status_min.set_val(left_w, h * w)
                status_max_t.set_val(left_w_t, -1)
                status_min_t.set_val(left_w_t, h * w)
                status[left_w] = 0
                # print(3, left_w_t % h, left_w_t // h)
            right_w_t = status_min_t.query(x_t, right_t)
            if right_w_t < h * w:
                right_w = (right_w_t % h) * w + (right_w_t // h)
                status_max.set_val(right_w, -1)
                status_min.set_val(right_w, h * w)
                status_max_t.set_val(right_w_t, -1)
                status_min_t.set_val(right_w_t, h * w)
                status[right_w] = 0
                # print(4, right_w_t % h, right_w_t // h)

        # print("--")
        # for i in range(h):
        #     print(status[i * w: (i + 1) * w])
        # print("--")
    res = sum(status)
    return res


def main():
    h, w, q = map(int, input().split())
    rc_list = [tuple(map(int, input().split())) for _ in range(q)]
    res = solve(h, w, q, rc_list)
    print(res)


def test():
    assert solve(2, 4, 3, [(1, 2), (1, 2), (1, 3)]) == 2
    assert solve(5, 5, 5, [(3, 3), (3, 3), (3, 2), (2, 2), (1, 2)]) == 10
    assert solve(4, 3, 10, [
        (2, 2), (4, 1), (1, 1), (4, 2), (2, 1),
        (3, 1), (1, 3), (1, 2), (4, 3), (4, 2),
    ]) == 2


if __name__ == "__main__":
    test()
    main()
