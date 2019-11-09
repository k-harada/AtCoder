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


def solve(n, m, lrc_list):
    s = SegmentTree([10 ** 15 + 1] * n, min, 10 ** 15 + 1)
    s.update(0, 0)
    lrc_list_s = sorted(lrc_list, key=lambda x: x[0])
    for i in range(m):
        l, r, c = lrc_list_s[i]
        p = s.query(l - 1, r)
        if p + c < s.query(r - 1, r):
            s.update(r - 1, p + c)
    if s.query(n - 1, n) == 10 ** 15 + 1:
        return -1
    else:
        return s.query(n - 1, n)


def main():
    n, m = map(int, input().split())
    lrc_list = []
    for _ in range(m):
        l, r, c = map(int, input().split())
        lrc_list.append([l, r, c])
    res = solve(n, m, lrc_list)
    print(res)


def test():
    assert solve(4, 3, [[1, 3, 2], [2, 4, 3], [1, 4, 6]]) == 5
    assert solve(4, 2, [[1, 2, 1], [3, 4, 2]]) == -1


if __name__ == "__main__":
    # test()
    main()
