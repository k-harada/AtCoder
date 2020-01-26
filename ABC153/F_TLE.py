from bisect import bisect_right


class SegTree:

    def __init__(self, a_list, x_list):
        assert max(a_list) <= 10 ** 7
        assert min(a_list) >= 0
        self.n = 1
        m = max(a_list)
        while self.n <= m:
            self.n *= 2
        self.dat_a = [0] * (self.n * 2 - 1)
        self.dat_b = [0] * (self.n * 2 - 1)
        for a, x in zip(a_list, x_list):
            self._add(a, a + 1, x, 0, 0, self.n)

    def _add(self, a, b, x, k, left, right):
        # add k for [a, b)
        if a <= left and right <= b:
            self.dat_a[k] += x
        elif left < b and a < right:
            self.dat_b[k] += (min(b, right) - max(a, left)) * x
            self._add(a, b, x, k * 2 + 1, left, (left + right) // 2)
            self._add(a, b, x, k * 2 + 2, (left + right) // 2, right)

    def _query_sum(self, a, b, k, left, right):
        if b <= left or right <= a:
            return 0
        elif a <= left and right <= b:
            return self.dat_a[k] + (right - left) * self.dat_b[k]
        else:
            res = (min(b, right) - max(a, left)) * self.dat_a[k]
            res += self._query_sum(a, b, k * 2 + 1, left, (left + right) // 2)
            res += self._query_sum(a, b, k * 2 + 2, (left + right) // 2, right)
            return res

    def add(self, a, b, x):
        return self._add(a, b, x, 0, 0, self.n)

    def query_sum(self, a, b):
        return self._query_sum(a, b, 0, 0, self.n)

    def _return_value(self, a, k, left, right):
        if left == a and right == a + 1:
            return self.dat_a[k]
        elif a < (left + right) // 2:
            return self.dat_a[k] + self._return_value(a, k * 2 + 1, left, (left + right) // 2)
        else:
            return self.dat_a[k] + self._return_value(a, k * 2 + 2, (left + right) // 2, right)

    def return_value(self, a):
        return self._return_value(a, 0, 0, self.n)


def solve(n, d, a, xh_list):
    res = 0
    xh_list_s = sorted(xh_list, key=lambda x: x[0])
    x_list_s = [xh[0] for xh in xh_list_s]
    h_list_s = [xh[1] for xh in xh_list_s]

    sg = SegTree(list(range(n)), h_list_s)

    for i in range(n):
        v = sg.return_value(i)
        if v > 0:
            t = (v - 1) // a + 1
            res += t
            j = bisect_right(x_list_s, x_list_s[i] + 2 * d)
            sg.add(i, j, - t * a)
    return res


def main():
    n, d, a = map(int, input().split())
    xh_list = []
    for _ in range(n):
        x, h = map(int, input().split())
        xh_list.append((x, h))
    res = solve(n, d, a, xh_list)
    print(res)


def test():
    assert solve(3, 3, 2, [(1, 2), (5, 4), (9, 2)]) == 2
    assert solve(9, 4, 1, [(1, 5), (2, 4), (3, 3), (4, 2), (5, 1), (6, 2), (7, 3), (8, 4), (9, 5)]) == 5
    assert solve(3, 0, 1, [(300000000, 1000000000), (100000000, 1000000000), (200000000, 1000000000)]) == 3000000000


if __name__ == "__main__":
    test()
    main()
