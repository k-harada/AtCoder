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


if __name__ == "__main__":
    sg = SegTree([1, 2, 3, 5], [10, 2, 1, 9])
    print(sg.dat_a)
    print(sg.dat_b)
    sg.add(2, 8, 100)
    print([sg.return_value(i) for i in range(8)])
