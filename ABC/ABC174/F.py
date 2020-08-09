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


def solve(n, q, c_list, lr_list):
    lri_list = [[lr_list[i][0], lr_list[i][1], i] for i in range(q)]
    # sort by r
    lri_list_s = sorted(lri_list, key=lambda x: x[1])
    # color_index
    color_index = [0] * (n + 1)
    # bit
    bit = BIT(n)

    res = [0] * q

    r_temp = 0
    for l, r, i in lri_list_s:
        while r > r_temp:
            r_temp += 1
            c = c_list[r_temp - 1]
            c_ind = color_index[c]
            if c_ind > 0:
                bit.add(c_ind, -1)
            color_index[c] = r_temp
            bit.add(r_temp, 1)
        # print(r, [bit.get(i) for i in range(n + 1)])
        res[i] = bit.get(l - 1, r)
    # print(res)
    return res


def main():
    n, q = map(int, input().split())
    c_list = list(map(int, input().split()))
    lr_list = [list(map(int, input().split())) for _ in range(q)]
    res = solve(n, q, c_list, lr_list)
    for r in res:
        print(r)


def test():
    assert solve(4, 3, [1, 2, 1, 3], [[1, 3], [2, 4], [3, 3]]) == [2, 3, 1]
    assert solve(10, 10, [2, 5, 6, 5, 2, 1, 7, 9, 7, 2], [
        [5, 5], [2, 4], [6, 7], [2, 2], [7, 8], [7, 9], [1, 8], [6, 9], [8, 10], [6, 8]
    ]) == [1, 2, 2, 1, 2, 2, 6, 3, 3, 3]


if __name__ == "__main__":
    test()
    main()
