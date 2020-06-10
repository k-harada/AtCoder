from collections import deque


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


def solve(n, kt_list, m, a_list):
    min_1_list = []
    min_2_list = []
    value_key = dict()
    queue_list = []
    for i in range(n):
        queue_list.append(deque(kt_list[i][1:]))
        min_1_list.append(kt_list[i][1])
        if len(kt_list[i]) >= 3:
            min_2_list.append(max(kt_list[i][1], kt_list[i][2]))
        else:
            min_2_list.append(kt_list[i][1])
        for v in kt_list[i][1:]:
            value_key[v] = i

    min_1_seg = SegmentTree(min_1_list, max, -1)
    min_2_seg = SegmentTree(min_2_list, max, -1)

    res_list = []
    for i in range(m):
        if a_list[i] == 1:
            res = min_1_seg.query(0, n)
            j = value_key[res]
            _ = queue_list[j].popleft()
        else:
            res = min_2_seg.query(0, n)
            j = value_key[res]
            r0 = queue_list[j].popleft()
            if r0 != res:
                r1 = queue_list[j].popleft()
                queue_list[j].appendleft(r0)
        # update
        if len(queue_list[j]) == 0:
            min_1_seg.update(j, -1)
            min_2_seg.update(j, -1)
        else:
            min_1 = queue_list[j].popleft()
            if len(queue_list[j]) > 0:
                m2 = queue_list[j].popleft()
                min_2 = max(min_1, m2)
                queue_list[j].appendleft(m2)
            else:
                min_2 = min_1
            queue_list[j].appendleft(min_1)
            min_1_seg.update(j, min_1)
            min_2_seg.update(j, min_2)

        res_list.append(res)
    return res_list


def main():
    n = int(input())
    kt_list = [list(map(int, input().split())) for _ in range(n)]
    m = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, kt_list, m, a_list)
    for r in res:
        print(r)


def test():
    assert solve(2, [[3, 1, 200, 1000], [5, 20, 30, 40, 50, 2]], 5, [1, 1, 1, 2, 2]) == [20, 30, 40, 200, 1000]


if __name__ == "__main__":
    test()
    main()
