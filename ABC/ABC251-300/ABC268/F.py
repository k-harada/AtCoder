def solve(n, s_list):
    ratio = [0] * n
    sc_list = [0] * n
    x_list = [0] * n
    res = 0
    for i, st in enumerate(s_list):
        x = 0
        s = 0
        for c in st:
            if c == "X":
                x += 1
            else:
                s += int(c)
                # inner score
                res += int(c) * x
        if x != 0:
            ratio[i] = s / x
        else:
            ratio[i] = 100000000
        sc_list[i] = s
        x_list[i] = x
    sort_list = list(sorted([(r, i) for i, r in enumerate(ratio)], key=lambda v: v[0]))
    xx = 0
    for _, k in sort_list:
        s, x = sc_list[k], x_list[k]
        res += xx * s
        xx += x
    # print(res)
    return res


def main():
    n = int(input())
    s_list = [input() for _ in range(n)]
    res = solve(n, s_list)
    print(res)


def test():
    assert solve(3, ["1X3", "59", "XXX"]) == 71
    assert solve(10, [
        "X63X395XX", "X2XX3X22X", "13", "3716XXX6", "45X",
        "X6XX", "9238", "281X92", "1XX4X4XX6", "54X9X711X1"
    ]) == 3010


if __name__ == "__main__":
    test()
    main()
