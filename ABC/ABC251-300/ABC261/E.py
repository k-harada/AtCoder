def solve(n, c, ta_list):
    base_00_list = [0]
    base_30_list = [2 ** 30 - 1]
    for t, a in ta_list:
        if t == 1:
            base_00_list.append(base_00_list[-1] & a)
            base_30_list.append(base_30_list[-1] & a)
        elif t == 2:
            base_00_list.append(base_00_list[-1] | a)
            base_30_list.append(base_30_list[-1] | a)
        else:
            base_00_list.append(base_00_list[-1] ^ a)
            base_30_list.append(base_30_list[-1] ^ a)
    res_list = []
    r = c
    for i in range(n):
        r = (r & base_30_list[i + 1]) | ((r ^ (2 ** 30 - 1)) & base_00_list[i + 1])
        res_list.append(r)
    return res_list


def main():
    n, c = map(int, input().split())
    ta_list = [tuple(map(int, input().split())) for _ in range(n)]
    res = solve(n, c, ta_list)
    for r in res:
        print(r)


def test():
    assert solve(3, 10, [(3, 3), (2, 5), (1, 12)]) == [9, 15, 12]


if __name__ == "__main__":
    test()
    main()
