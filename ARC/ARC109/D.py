def solve(t, abc_list):

    res_list = []

    for ax, ay, bx, by, cx, cy in abc_list:

        res_list.append(res)

    return res_list


def main():
    t = int(input())
    abc_list = [tuple(map(int, input().split())) for _ in range(t)]
    res = solve(t, abc_list)
    for r in res:
        print(r)


def test():
    assert solve(1, [(5, 4, 5, 3, 4, 4)]) == [9]
    assert solve(1, [(3, 2, 2, 2, 2, 1)]) == [4]


if __name__ == "__main__":
    test()
    main()
