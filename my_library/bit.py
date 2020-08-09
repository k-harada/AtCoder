class BIT:
    """
    https://tjkendev.github.io/procon-library/python/range_query/bit.html
    """
    def __init__(self, n):
        self.n = n
        self.data = [0] * (n + 1)
        self.el = [0] * (n + 1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & -i
        return s

    def add(self, i, x):
        assert i > 0
        self.el[i] += x
        while i <= self.n:
            self.data[i] += x
            i += i & -i

    def get(self, i, j=None):
        if j is None:
            return self.el[i]
        return self.sum(j) - self.sum(i)


if __name__ == "__main__":
    bit = BIT(10)
    bit.add(1, 3)
    print(bit.sum(0), bit.sum(1))
    bit.add(3, 2)
    print(bit.sum(5))
    bit.add(1, -3)
    print(bit.sum(5))
