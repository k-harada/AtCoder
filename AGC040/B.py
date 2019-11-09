from heapq import heappop, heappush


def solve_b(n, l_list, r_list):

    l_max = max(l_list)
    r_min = min(r_list)

    # l_max and r_min in same contest
    res_1 = max(0, r_min - l_max + 1)
    # one problem contest
    res_1 += max([r_list[i] - l_list[i] + 1 for i in range(n)])

    # l_max in one, r_min in the other
    hr = []
    for i in range(n):
        if r_list[i] > r_min:
            heappush(hr, (r_list[i], i))
    r_need = min([r_list[i] for i in range(n) if l_list[i] == l_max])
    l_temp = max([l_list[i] for i in range(n) if r_list[i] == r_min])

    res_2 = 0
    while len(hr) > 0:
        r, i = heappop(hr)
        res_2 = max(res_2, max(0, min(r, r_need) - l_max + 1) + max(0, r_min - l_temp + 1))
        l_temp = max(l_temp, l_list[i])
    res_2 = max(res_2, max(0, r_need - l_max + 1) + max(0, r_min - l_temp + 1))

    return max(res_1, res_2)


def main():
    n = int(input())
    l_list = [0] * n
    r_list = [0] * n
    for i in range(n):
        l, r = map(int, input().split())
        l_list[i] = l
        r_list[i] = r
    res = solve_b(n, l_list, r_list)
    print(res)


def test():
    assert solve_b(4, [4, 1, 5, 2], [7, 4, 8, 5]) == 6
    assert solve_b(4, [1, 2, 3, 4], [20, 19, 18, 17]) == 34


if __name__ == "__main__":
    test()
    main()
