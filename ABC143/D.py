from heapq import heappush, heappop
from bisect import bisect_left, bisect_right


def solve_d(n, l_list):
    res = 0
    l_list_s = sorted(l_list)
    for i in range(1, n - 1):
        b = l_list_s[i]
        for j in range(0, i):
            a = l_list_s[j]
            res += bisect_left(l_list_s, a + b) - (i + 1)

    return res


def solve_d_(n, l_list):
    res = 0
    l_list_s = sorted(l_list)
    h = []
    for i in range(1, n - 1):
        for j in range(0, i):
            heappush(h, l_list_s[i] + l_list_s[j])
        while len(h) > 0:
            a = heappop(h)
            if a > l_list_s[i + 1]:
                heappush(h, a)
                break
        res += len(h)

    return res


def main():
    n = int(input())
    l_list = list(map(int, input().split()))
    res = solve_d(n, l_list)
    print(res)


def test():
    assert solve_d(4, [3, 4, 2, 1]) == 1
    assert solve_d(3, [1, 1000, 1]) == 0
    assert solve_d(7, [218, 786, 704, 233, 645, 728, 389]) == 23


if __name__ == "__main__":
    test()
    main()
