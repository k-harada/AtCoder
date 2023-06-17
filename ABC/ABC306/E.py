from heapq import heappop, heappush
from collections import defaultdict


def solve_ex(n, k, q, xy_list):
    res = []
    a_list = [0] * (n + 1)
    s = 0
    for x, y in xy_list:
        z = a_list[x]
        s -= z
        s += y
        a_list[x] = y
        res.append(s)
    return res


def solve(n, k, q, xy_list):
    if k == n:
        return solve_ex(n, k, q, xy_list)
    res = []
    a_list = [0] * (n + 1)
    left = []
    right = []
    deleted_left = defaultdict(int)
    deleted_right = defaultdict(int)
    for _ in range(k):
        heappush(left, 0)
    for _ in range(n - k):
        heappush(right, 0)

    s = 0
    for x, y in xy_list:
        # check min of right
        while True:
            a = heappop(left)
            if deleted_left[a] == 0:
                break
            else:
                deleted_left[a] -= 1
        heappush(left, a)
        while True:
            b = - heappop(right)
            if deleted_right[b] == 0:
                break
            else:
                deleted_right[b] -= 1
        heappush(right, -b)

        z = a_list[x]
        if z >= a:
            deleted_left[z] += 1
            s -= z
            heappush(right, -y)
            w = - heappop(right)
            heappush(left, w)
            s += w
        else:
            deleted_right[z] += 1
            heappush(left, y)
            s += y
            w = heappop(left)
            s -= w
            heappush(right, -w)
        # print(left)
        # print(right)
        a_list[x] = y
        res.append(s)
    return res


def main():
    n, k, q = map(int, input().split())
    xy_list = [tuple(map(int, input().split())) for _ in range(q)]
    res = solve(n, k, q, xy_list)
    for r in res:
        print(r)


def test():
    assert solve(4, 2, 10, [
        (1, 5), (2, 1), (3, 3), (4, 2), (2, 10),
        (1, 0), (4, 0), (3, 1), (2, 0), (3, 0)
    ]) == [5, 6, 8, 8, 15, 13, 13, 11, 1, 0]
    assert solve(4, 4, 10, [
        (1, 5), (2, 1), (3, 3), (4, 2), (2, 10),
        (1, 0), (4, 0), (3, 1), (2, 0), (3, 0)
    ]) == [5, 6, 9, 11, 20, 15, 13, 11, 1, 0]


if __name__ == "__main__":
    test()
    main()
