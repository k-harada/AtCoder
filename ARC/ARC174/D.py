import math


def solve(t, n_list):
    # 1, 80
    # 999999
    max_dict = dict()
    min_dict = dict()
    for y in [9, 99, 999, 9999, 99999, 999999, 9999999, 99999999, 999999999]:
        min_dict[y] = y * (y + 1)
        max_dict[y] = (y + 1) ** 2 - 1
        min_dict[y + 1] = (y + 1) ** 2
        max_dict[y + 1] = (y + 1) * (y + 2) - 1
        if y > 9:
            min_dict[y - 1] = (y - 1) * (y + 1)
            max_dict[y - 1] = (y - 1) * (y + 1)
    res_list = []
    for n in n_list:
        res = 0
        if n >= 1:
            res += 1
        if n >= 80:
            res += 1
        for y in max_dict.keys():
            if n >= max_dict[y]:
                res += max_dict[y] - min_dict[y] + 1
            elif n >= min_dict[y]:
                res += n - min_dict[y] + 1
        res_list.append(res)
    # print(res_list)
    return res_list


def solve_sub_greed(n):
    res = 0
    for x in range(1, n + 1):
        y = int(math.sqrt(x))
        if str(y) == str(x)[:len(str(y))]:
            print(x, y)
            res += 1
    print(res)


def main():
    t = int(input())
    n_list = [int(input()) for _ in range(t)]
    res = solve(t, n_list)
    for r in res:
        print(r)


def test():
    assert solve(2, [1, 174]) == [1, 22]
    assert solve(1, [1100000]) == [2224]


def test_greed():
    solve_sub_greed(1100000)


if __name__ == "__main__":
    test()
    # test_greed()
    main()
