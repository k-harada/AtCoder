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


def solve(n, k, d, a_list):
    if d * (k - 1) + 1 > n:
        return -1
    # Range Minimum Query
    sg = SegmentTree(a_list)
    res_list = []
    start = 0
    while k > 0:
        end = n - d * (k - 1)
        m = sg.query(start, end)
        # search min
        for i in range(start, n):
            if a_list[i] == m:
                start = i + d
                break
        k -= 1
        res_list.append(m)

    return " ".join([str(res) for res in res_list])


def main():
    n, k, d = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, k, d, a_list)
    print(res)


def test():
    assert solve(3, 2, 2, [3, 1, 4]) == "3 4"
    assert solve(3, 3, 2, [3, 1, 4]) == -1
    assert solve(3, 2, 1, [3, 1, 4]) == "1 4"
    assert solve(4, 2, 2, [3, 6, 5, 5]) == "3 5"


if __name__ == "__main__":
    test()
    main()
