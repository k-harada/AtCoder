from heapq import heappop, heappush


def solve(n, ab_list):
    res_list = []
    b_list_dict = dict()
    for i in range(n):
        b_list_dict[i + 1] = []
    for i in range(n):
        a, b = ab_list[i]
        b_list_dict[a].append(b)
    res = 0
    h = []
    for i in range(1, n + 1):
        for b in b_list_dict[i]:
            heappush(h, -b)
        c = heappop(h)
        res -= c
        res_list.append(res)
    return res_list


def main():
    n = int(input())
    ab_list = []
    for _ in range(n):
        a, b = map(int, input().split())
        ab_list.append((a, b))
    res = solve(n, ab_list)
    for r in res:
        print(r)


def test():
    assert solve(3, [(1, 3), (2, 2), (2, 4)]) == [3, 7, 9]
    assert solve(5, [(5, 3), (4, 1), (3, 4), (2, 1), (1, 5)]) == [5, 6, 10, 11, 14]
    assert solve(6, [(1, 8), (1, 6), (2, 9), (3, 1), (3, 2), (4, 1)]) == [8, 17, 23, 25, 26, 27]


if __name__ == "__main__":
    test()
    main()
