from bisect import bisect_left


LARGE = 998244353


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


def solve(n, x_list, d_list):
    reach_right = [0] * n
    reach_right[-1] = n - 1
    # from right
    seg = SegmentTree(list(range(n)), max, -1)
    for i in range(n - 2, -1, -1):
        j = bisect_left(x_list, x_list[i] + d_list[i])
        k = seg.query(i, j)
        seg.update(i, k)
        reach_right[i] = k
    # dp
    dp = [[0] * 2 for _ in range(n)]
    dp[n - 1][0] = 1
    dp[n - 1][1] = 1
    for i in range(n - 2, -1, -1):
        dp[i][0] = (dp[i + 1][0] + dp[i + 1][1]) % LARGE
        j = reach_right[i] + 1
        if j <= n - 1:
            dp[i][1] = (dp[j][0] + dp[j][1]) % LARGE
        else:
            dp[i][1] = 1

    return (dp[0][0] + dp[0][1]) % LARGE


def main():
    n = int(input())
    xd_list = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: x[0])
    x_list = [xd[0] for xd in xd_list]
    d_list = [xd[1] for xd in xd_list]
    res = solve(n, x_list, d_list)
    print(res)


def test():
    assert solve(2, [1, 3], [5, 3]) == 3
    assert solve(3, [-1, 3, 6], [10, 3, 5]) == 5
    assert solve(4, [-10, -4, 4, 7], [3, 3, 3, 10]) == 16


# pypy
if __name__ == "__main__":
    test()
    main()
