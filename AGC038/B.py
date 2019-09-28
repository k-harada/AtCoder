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


def solve_b(n, k, p_list):

    min_tree = SegmentTree(p_list)
    max_tree = SegmentTree(p_list, max, -1)

    min_list = [0] * n
    max_list = [0] * n

    for i in range(n - k + 1):
        if p_list[i] == min_tree.query(i, i + k):
            min_list[i] = 1

    for i in range(n - k + 1):
        if p_list[i + k - 1] == max_tree.query(i, i + k):
            max_list[i + k - 1] = 1

    res = 1
    # print(min_list, max_list)

    for i in range(n - k):
        if min_list[i] == 0 or max_list[i + k] == 0:
            res += 1

    # count invariant
    straight = 1
    count_k = 0
    for i in range(n - 1):
        if p_list[i] < p_list[i + 1]:
            straight += 1
        else:
            straight = 1
        if straight == k:
            count_k += 1

    if count_k > 0:
        res -= count_k - 1

    return res


def solve_b_greedy(n, k, p_list):

    count_dict = dict()

    for i in range(n - k + 1):
        p_list_new = p_list[:i] + list(sorted(p_list[i:i + k])) + p_list[i + k:]
        p_list_new_hash = ".".join([str(p) for p in p_list_new])
        if p_list_new_hash in count_dict.keys():
            print(i, p_list_new_hash)
        count_dict[p_list_new_hash] = 1

    return len(count_dict)


def main_greed():
    n, k = map(int, input().split())
    p_list = list(map(int, input().split()))
    res = solve_b_greedy(n, k, p_list)
    print(res)


def main():
    n, k = map(int, input().split())
    p_list = list(map(int, input().split()))
    res = solve_b(n, k, p_list)
    print(res)


if __name__ == "__main__":
    main()
