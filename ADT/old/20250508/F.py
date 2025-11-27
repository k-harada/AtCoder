def solve(n, a_list):
    res_1 = 0
    res_2 = 0
    for i, a in enumerate(a_list):
        if i + 1 == a:
            res_1 += 1
        else:
            if a_list[a - 1] == i + 1:
                res_2 += 1
    # print(res_1, res_2)
    res = res_1 * (res_1 - 1) // 2 + res_2 // 2
    return res


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(4, [1, 3, 2, 4]) == 2
    assert solve(10, [5, 8, 2, 2, 1, 6, 7, 2, 9, 10]) == 8


if __name__ == "__main__":
    test()
    main()
