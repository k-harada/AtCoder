def solve(t, lr_list):
    res_list = []
    for l, r in lr_list:
        if 2 * l > r:
            res_list.append(0)
        else:
            m = r - 2 * l + 1
            if m % 2 == 1:
                k = (m + 1) * (m + 1) // 4
            else:
                k = (m // 2) * (m // 2 + 1)
            d = (r - 2 * l) // 2 + 1
            res_list.append(2 * k - d)
    # print(res_list)
    return res_list


def main():
    t = int(input())
    lr_list = [tuple(map(int, input().split())) for _ in range(t)]
    res_list = solve(t, lr_list)
    for res in res_list:
        print(res)


def test():
    assert solve(5, [
        (2, 6), (0, 0), (1000000, 1000000), (12345, 67890), (0, 1000000)
    ]) == [6, 1, 0, 933184801, 500001500001]


if __name__ == "__main__":
    test()
    main()
