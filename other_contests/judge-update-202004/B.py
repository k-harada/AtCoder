def solve(n, xc_list):

    r_list = []
    b_list = []
    for i in range(n):
        x, c = xc_list[i]
        if c == "R":
            r_list.append(int(x))
        else:
            b_list.append(int(x))

    res = list(sorted(r_list)) + list(sorted(b_list))

    return res


def main():
    n = int(input())
    xc_list = [list(input().split()) for _ in range(n)]
    res = solve(n, xc_list)
    for r in res:
        print(r)


def test():
    assert solve(4, [[10, "B"], [6, "R"], [2, "R"], [4, "B"]]) == [2, 6, 4, 10]
    assert solve(2, [[5, "B"], [7, "B"]]) == [5, 7]


if __name__ == "__main__":
    test()
    main()
