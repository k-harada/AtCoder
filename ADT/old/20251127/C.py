def solve(xy_list):
    d01 = (xy_list[0][0] - xy_list[1][0]) ** 2 + (xy_list[0][1] - xy_list[1][1]) ** 2
    d12 = (xy_list[1][0] - xy_list[2][0]) ** 2 + (xy_list[1][1] - xy_list[2][1]) ** 2
    d20 = (xy_list[2][0] - xy_list[0][0]) ** 2 + (xy_list[2][1] - xy_list[0][1]) ** 2
    # print(d01, d12, d20)
    if max([d01, d12, d20]) * 2 == d01 + d12 + d20:
        return "Yes"
    else:
        return "No"


def main():
    xy_list = [tuple(map(int, input().split())) for _ in range(3)]
    res = solve(xy_list)
    print(res)


def test():
    assert solve([(0, 0), (4, 0), (0, 3)]) == "Yes"
    assert solve([(-4, 3), (2, 1), (3, 4)]) == "Yes"
    assert solve([(2, 4), (-3, 2), (1, -2)]) == "No"


if __name__ == "__main__":
    test()
    main()
