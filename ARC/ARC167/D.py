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


def solve_sub(n, p_list):
    # グループ分け
    g = [-1] * n
    c = 0
    for i in range(n):
        if g[i] != -1:
            continue
        x = i
        while g[x] == -1:
            g[x] = c
            x = p_list[x] - 1
        c += 1
    print(g)
    group = [[] for _ in range(c)]
    for i in range(n):
        group[g[i]].append(i)
    print(group)
    rmq = SegmentTree(length=n, op=min, e=lambda: n + 1)
    rmq.initialize(p_list)
    res = [p for p in p_list]
    # set group[0] n + 1
    for i in group[0]:
        rmq.set_val(i, n + 1)
    for i in range(n):
        
    return ""


def solve(t, case_list):
    res = [solve_sub(n, p_list) for n, p_list in case_list]
    return res


def main():
    t = int(input())
    case_list = []
    for _ in range(t):
        n = int(input())
        p_list = list(map(int, input().split()))
        case_list.append((n, p_list))
    res = solve(t, case_list)
    for r in res:
        print(r)


def test():
    assert solve(5, [
        (4, [2, 1, 4, 3]),
        (5, [2, 1, 3, 4, 5]),
        (2, [1, 2]),
        (2, [2, 1]),
        (9, [4, 3, 6, 2, 7, 1, 9, 8, 5]),
    ]) == [
        "",
        "",
        "",
        "",
        ""
    ]
    assert solve(5, [
        (4, [2, 1, 4, 3]),
        (5, [2, 1, 3, 4, 5]),
        (2, [1, 2]),
        (2, [2, 1]),
        (9, [4, 3, 6, 2, 7, 1, 9, 8, 5]),
    ]) == [
        "2 3 4 1",
        "2 3 4 5 1",
        "2 1",
        "2 1",
        "4 3 5 2 7 1 8 9 6"
    ]


if __name__ == "__main__":
    test()
    main()
