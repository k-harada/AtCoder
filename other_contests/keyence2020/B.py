from heapq import heappop, heappush
from bisect import bisect_right


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


def solve(n, x_list, le_list):
    right_limits = dict()
    for i in range(n):
        right_limits[x_list[i] + le_list[i]] = 0
    right_limits_list = list(sorted(list(right_limits.keys())))
    s = SegmentTree([0] * len(right_limits_list), max, -1)

    h = []
    for i in range(n):
        heappush(h, (x_list[i] + le_list[i], i))

    for k in range(n):
        right, i = heappop(h)
        left = x_list[i] - le_list[i]
        ind_left = bisect_right(right_limits_list, left)
        ind_right = bisect_right(right_limits_list, right) - 1
        if ind_left == 0:
            r = s.query(ind_right, ind_right + 1)
            if r == 0:
                s.update(ind_right, 1)
        else:
            r = s.query(ind_right, ind_right + 1)
            l_max = s.query(0, ind_left)
            if r < l_max + 1:
                s.update(ind_right, l_max + 1)

    return s.query(0, n)


def main():
    n = int(input())
    x_list = [0] * n
    le_list = [0] * n
    for i in range(n):
        x, le = map(int, input().split())
        x_list[i] = x
        le_list[i] = le
    res = solve(n, x_list, le_list)
    print(res)


def test():
    assert solve(4, [2, 4, 9, 100], [4, 3, 3, 5]) == 3
    assert solve(2, [8, 1], [20, 10]) == 1
    assert solve(5, [10, 2, 4, 6, 8], [1, 1, 1, 1, 1]) == 5


if __name__ == "__main__":
    test()
    main()
