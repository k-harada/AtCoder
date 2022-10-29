from heapq import heappush, heappop


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


def solve(n, q, ab_list, cd_list):

    heap_list = [[] for _ in range(200001)]
    # rate_list
    rate_list = [0] * n
    # belongs
    belong_list = [0] * n
    # heappush
    for i in range(n):
        a, b = ab_list[i]
        rate_list[i] = a
        belong_list[i] = b
        heappush(heap_list[b], (-a, i))
    # initialize
    max_list = [10 ** 9 + 7] * 200001
    for b in range(200001):
        if len(heap_list[b]) == 0:
            pass
        else:
            a, i = heappop(heap_list[b])
            max_list[b] = -a
            heappush(heap_list[b], (a, i))

    seg = SegmentTree(max_list)
    # print(max_list[:4])
    # run
    res_list = []
    for c, d in cd_list:
        b = belong_list[c - 1]
        # change
        belong_list[c - 1] = d

        # update b
        while True:
            a, i = heappop(heap_list[b])
            if belong_list[i] == b:
                heappush(heap_list[b], (a, i))
                max_list[b] = -a
                seg.update(b, max_list[b])
                break
            if len(heap_list[b]) == 0:
                max_list[b] = 10 ** 9 + 7
                seg.update(b, max_list[b])
                break

        # update d
        if len(heap_list[d]) > 0:
            max_list[d] = max(max_list[d], rate_list[c - 1])
        else:
            max_list[d] = rate_list[c - 1]
        seg.update(d, max_list[d])
        heappush(heap_list[d], (-rate_list[c - 1], c - 1))

        res_list.append(seg.query(0, 200001))
        # print(max_list[:4])
    # print(res_list)
    return res_list


def main():
    n, q = map(int, input().split())
    ab_list = [list(map(int, input().split())) for _ in range(n)]
    cd_list = [list(map(int, input().split())) for _ in range(q)]
    res = solve(n, q, ab_list, cd_list)
    for r in res:
        print(r)


def test():
    assert solve(6, 3, [[8, 1], [6, 2], [9, 3], [1, 1], [2, 2], [1, 3]], [[4, 3], [2, 1], [1, 2]]) == [6, 2, 6]
    assert solve(2, 2, [[4208, 1234], [3056, 5678]], [[1, 2020], [2, 2020]]) == [3056, 4208]


if __name__ == "__main__":
    test()
    main()
