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


def solve(n, ab_list, q, query_list):
    point_dict = dict()
    point_unique_list = []
    point_list = [0]
    count_list = [0]
    for a, b in ab_list:
        if a not in point_dict.keys():
            point_dict[a] = 0
        point_dict[a] += b
        point_list.append(a)
        count_list.append(b)
        point_unique_list.append(a)

    for query in query_list:
        if query[0] == 1:
            p = query[2]
            point_unique_list.append(p)
            if p not in point_dict.keys():
                point_dict[p] = 0

    point_unique_list = list(sorted(list(set(point_unique_list))))
    m = len(point_unique_list)
    point_rev_map = dict()
    for i, p in enumerate(point_unique_list):
        point_rev_map[p] = i

    count_tree = SegmentTree(m, op=add, e=lambda: 0)
    count_tree.initialize([point_dict[p] for p in point_unique_list])
    score_tree = SegmentTree(m, op=add, e=lambda: 0)
    score_tree.initialize([p * point_dict[p] for p in point_unique_list])

    res = []

    for query in query_list:
        if query[0] == 1:
            i = query[1]
            p = query[2]
            q = point_list[i]
            c = count_list[i]
            point_dict[p] += c
            point_dict[q] -= c
            jp = point_rev_map[p]
            jq = point_rev_map[q]
            count_tree.set_val(jp, point_dict[p])
            count_tree.set_val(jq, point_dict[q])
            score_tree.set_val(jp, p * point_dict[p])
            score_tree.set_val(jq, q * point_dict[q])

            point_list[i] = p
        elif query[0] == 2:
            i = query[1]
            c_new = query[2]
            c_old = count_list[i]
            p = point_list[i]
            point_dict[p] += c_new - c_old
            jp = point_rev_map[p]
            count_tree.set_val(jp, point_dict[p])
            score_tree.set_val(jp, p * point_dict[p])

            count_list[i] = c_new
        else:
            x = query[1]
            # binary search
            if count_tree.query(0, m) < x:
                res.append(-1)
            else:
                left = 0
                right = m
                while left + 1 < right:
                    middle = (left + right) // 2
                    if count_tree.query(middle, m) < x:
                        right = middle
                    else:
                        left = middle
                c = count_tree.query(right, m)
                s = score_tree.query(right, m)
                s += (x - c) * point_unique_list[left]
                res.append(s)
        # print([count_tree.query(i, i + 1) for i in range(m)])
        # print([score_tree.query(i, i + 1) for i in range(m)])
        # check
        # check_cnt_1 = 0
        # check_sum_1 = 0
        # for p in point_unique_list:
        #     check_cnt_1 += point_dict[p]
        #     check_sum_1 += p * point_dict[p]
        # assert check_cnt_1 == count_tree.query(0, m)
        # assert check_sum_1 == score_tree.query(0, m)
        # check_cnt_2 = sum(count_list)
        # check_sum_2 = sum([p * c for p, c in zip(count_list, point_list)])
        # assert check_cnt_2 == check_cnt_1
        # assert check_sum_2 == check_sum_1
    # print(res)
    return res


def main():
    n = int(input())
    ab_list = [tuple(map(int, input().split())) for _ in range(n)]
    q = int(input())
    query_list = [tuple(map(int, input().split())) for _ in range(q)]
    res = solve(n, ab_list, q, query_list)
    for r in res:
        print(r)


def test():
    assert solve(
        3, [(1, 1), (2, 2), (3, 3)], 7, [(3, 4), (1, 1, 10), (3, 4), (2, 1, 0), (2, 3, 0), (3, 4), (3, 2)]
    ) == [11, 19, -1, 4]


if __name__ == "__main__":
    test()
    main()


