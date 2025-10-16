from heapq import heappop, heappush


def solve(n, m, k, a_list):
    if m == k:
        r = 0
        for j in range(k):
            r += a_list[j]
        res = [r]
        for j in range(m, n):
            r -= a_list[j - m]
            r += a_list[j]
            res.append(r)
        return res
    heap_low = []
    heap_high = []
    b_list = list(sorted([(a, i) for i, a in enumerate(a_list[:m])]))
    position_list = [0] * n
    r = 0
    for j in range(k):
        a, i = b_list[j]
        heappush(heap_low, (-a, i))
        position_list[i] = -1
        r += a
    for j in range(k, m):
        a, i = b_list[j]
        heappush(heap_high, (a, i))
        position_list[i] = 1
    res = [r]
    for i in range(m, n):
        # lowにいる
        if position_list[i - m] == -1:
            # 弾く
            r -= a_list[i - m]
            position_list[i - m] = 0
            # 補充する
            # 候補を抽出
            while True:
                a, j = heappop(heap_high)
                if position_list[j] == 1:
                    break
            if a <= a_list[i]:
                heappush(heap_low, (-a, j))
                position_list[j] = -1
                heappush(heap_high, (a_list[i], i))
                position_list[i] = 1
                r += a
            else:
                heappush(heap_high, (a, j))
                position_list[j] = 1
                heappush(heap_low, (-a_list[i], i))
                position_list[i] = -1
                r += a_list[i]
        else:
            # highにいる
            position_list[i - m] = 0
            # 補充する
            # 候補を抽出
            while True:
                a_, j = heappop(heap_low)
                if position_list[j] == -1:
                    a = (-1) * a_
                    break
            r -= a
            if a <= a_list[i]:
                heappush(heap_low, (-a, j))
                position_list[j] = -1
                heappush(heap_high, (a_list[i], i))
                position_list[i] = 1
                r += a
            else:
                heappush(heap_high, (a, j))
                position_list[j] = 1
                heappush(heap_low, (-a_list[i], i))
                position_list[i] = -1
                r += a_list[i]
        res.append(r)
    return res


def main():
    n, m, k = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, m, k, a_list)
    for r in res:
        print(r)


def test():
    assert solve(6, 4, 3, [3, 1, 4, 1, 5, 9]) == [5, 6, 10]
    assert solve(10, 6, 3, [12, 2, 17, 11, 19, 8, 4, 3, 6, 20]) == [21, 14, 15, 13, 13]


if __name__ == "__main__":
    test()
    main()
