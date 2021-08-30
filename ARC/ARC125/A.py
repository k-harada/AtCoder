def solve(n, m, a_list, b_list):

    if min(a_list) > min(b_list):
        # print(min(a_list), min(b_list))
        return -1
    if max(a_list) < max(b_list):
        # print(max(a_list), max(b_list))
        return -1
    a0 = a_list[0]
    d_min = n
    for i in range(n):
        if a0 != a_list[i]:
            d_min = min(d_min, min(i, n - i))

    cnt = 0
    for i in range(m - 1):
        if b_list[i + 1] != b_list[i]:
            cnt += 1
    if cnt == 0:
        if a_list[0] == b_list[0]:
            return m
        else:
            return m + d_min
    else:
        if a_list[0] == b_list[0]:
            return m + cnt - 1 + d_min
        else:
            return m + cnt + d_min


def main():
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    res = solve(n, m, a_list, b_list)
    print(res)


def test():
    assert solve(3, 4, [0, 0, 1], [0, 1, 1, 0]) == 6
    assert solve(1, 1, [0], [1]) == -1
    assert solve(4, 5, [0, 1, 0, 1], [1, 0, 0, 1, 0]) == 9


if __name__ == "__main__":
    test()
    main()
