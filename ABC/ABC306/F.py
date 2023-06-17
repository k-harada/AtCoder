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


def solve(n, m, a):
    a_values = []
    for i in range(n):
        for j in range(m):
            a_values.append(a[i][j])
    a_values = list(sorted(a_values))
    a_index_dict = dict()
    for i, a_ in enumerate(a_values):
        a_index_dict[a_] = i + 1

    res = 0
    base = m * (m + 1) // 2
    bit = BIT(n * m + 1)
    for i in range(n - 1, -1, -1):
        for a_ in a[i]:
            j = a_index_dict[a_]
            res += bit.get(0, j)
        res += base * (n - 1 - i)
        for a_ in a[i]:
            j = a_index_dict[a_]
            bit.add(j, 1)
        # print(bit.sum(n * m + 1))
        # print(res)
    return res


def main():
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    res = solve(n, m, a)
    print(res)


def test():
    assert solve(3, 2, [[1, 3], [2, 8], [4, 6]]) == 12
    assert solve(1, 1, [[306]]) == 0
    assert solve(4, 4, [
        [155374934, 164163676, 576823355, 954291757],
        [797829355, 404011431, 353195922, 138996221],
        [191890310, 782177068, 818008580, 384836991],
        [160449218, 545531545, 840594328, 501899080]
    ]) == 102


if __name__ == "__main__":
    test()
    main()
