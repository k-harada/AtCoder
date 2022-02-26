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


def e_zero():
    return 0


def op_add(x, y):
    return x + y


def solve(q, query_list):

    # Aの値にindexをはる
    a_list = []
    for query in query_list:
        a_list.append(query[1])
    a_list_s = list(sorted(list(set(a_list))))
    a_inv = dict()
    for i, a in enumerate(a_list_s):
        a_inv[a] = i

    rsq = SegmentTree(len(a_list_s), op_add, e_zero)
    rsq.initialize([0] * len(a_list_s))

    res = []

    # 実行
    c = 0
    c_list = [0] * len(a_list_s)
    for query in query_list:
        if query[0] == 1:
            c += 1
            v = query[1]
            u = a_inv[v]
            c_list[u] += 1
            rsq.set_val(u, c_list[u])

        elif query[0] == 2:
            x = query[1]
            k = query[2]
            u = a_inv[x]

            # どうやっても無理
            if rsq.query(0, u + 1) < k:
                res.append(-1)
            # xが答え
            elif c_list[u] >= k:
                res.append(x)
            else:
                # 二分探索
                left = 0
                right = u
                while left < right - 1:
                    center = (left + right) // 2
                    if rsq.query(center, u + 1) >= k:
                        left = center
                    else:
                        right = center
                res.append(a_list_s[left])
        else:
            x = query[1]
            k = query[2]
            u = a_inv[x]

            # 全部持ってきても無理
            if rsq.query(u, len(a_list_s)) < k:
                res.append(-1)
            # xが答え
            elif c_list[u] >= k:
                res.append(x)
            else:
                # 二分探索
                left = u
                right = len(a_list_s) - 1
                while left < right - 1:
                    center = (left + right) // 2
                    if rsq.query(u, center + 1) >= k:
                        right = center
                    else:
                        left = center
                res.append(a_list_s[right])
    # print(res)
    return res


def main():
    q = int(input())
    query_list = [tuple(map(int, input().split())) for _ in range(q)]
    res = solve(q, query_list)
    for r in res:
        print(r)


def test():
    assert solve(11, [
        (1, 20), (1, 10), (1, 30), (1, 20), (3, 15, 1), (3, 15, 2), (3, 15, 3), (3, 15, 4),
        (2, 100, 5), (1, 1), (2, 100, 5)
    ]) == [20, 20, 30, -1, -1, 1]


if __name__ == "__main__":
    test()
    main()
