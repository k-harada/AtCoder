class SegmentTree(object):

    def __init__(self, init_array, seg_func=min, seg_func_null=10 ** 9 + 7):

        self.seg_func = seg_func
        self.seg_func_null = seg_func_null
        self.n = 1
        while self.n < len(init_array):
            self.n *= 2
        self.dat = [0] * (2 * self.n - 1)
        for i in range(len(init_array)):
            self.dat[self.n - 1 + i] = init_array[i]
        for i in range(self.n - 2, -1, -1):
            self.dat[i] = self.seg_func(self.dat[2 * i + 1], self.dat[2 * i + 2])

    def update(self, k, a):
        k += self.n - 1
        self.dat[k] = a
        while k > 0:
            k = (k - 1) // 2
            self.dat[k] = self.seg_func(self.dat[k * 2 + 1], self.dat[k * 2 + 2])

    def query(self, p, q):
        # [p, q)
        if q <= p:
            return self.seg_func_null

        p += self.n - 1
        q += self.n - 2
        res = self.seg_func_null

        while q - p > 1:
            if p & 1 == 0:
                res = self.seg_func(res, self.dat[p])
            if q & 1 == 1:
                res = self.seg_func(res, self.dat[q])
                q -= 1
            p = p // 2
            q = (q-1) // 2
        if p == q:
            res = self.seg_func(res, self.dat[p])
        else:
            res = self.seg_func(self.seg_func(res, self.dat[p]), self.dat[q])

        return res

    def get_item(self, i):
        return self.dat[self.n - 1 + i]


def solve(n, q, query_list):

    normal_tree = SegmentTree(list(range(n + 1)))
    strange_tree = SegmentTree([10 ** 9 + 7] * (n + 1))

    a_list = list(range(n + 1))
    for t, x, y in query_list:
        if t == 1:
            a_list[x], a_list[x + 1] = a_list[x + 1], a_list[x]
            # dirty
            normal_tree.update(x, 10 ** 9 + 7)
            normal_tree.update(x + 1, 10 ** 9 + 7)
            strange_tree.update(x, x)
            strange_tree.update(x + 1, x + 1)
        else:
            if normal_tree.get_item(x) == 10 ** 9 + 7:
                left = x
            else:
                left = strange_tree.query(x, y + 1)
            while left < 10 ** 9 + 7:
                right = normal_tree.query(left, y)
                if x < left and right <= y:
                    # clean case
                    for i in range(left, right):
                        # normalize
                        a_list[i] = i
                        normal_tree.update(i, i)
                        strange_tree.update(i, 10 ** 9 + 7)
                else:
                    # still dirty
                    right = min(right, y + 1)
                    for i, k in enumerate(sorted(a_list[left:right])):
                        a_list[left + i] = k

                left = strange_tree.query(right, y + 1)

    return " ".join([str(a) for a in a_list[1:]])


def main():
    n, q = map(int, input().split())
    query_list = [list(map(int, input().split())) for _ in range(q)]
    res = solve(n, q, query_list)
    print(res)


def test():
    assert solve(5, 3, [[1, 1, 0], [1, 2, 0], [2, 2, 4]]) == "2 1 3 4 5"


if __name__ == "__main__":
    test()
    main()
