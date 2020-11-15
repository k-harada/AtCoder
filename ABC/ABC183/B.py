def solve(s_x, s_y, g_x, g_y):
    return (s_y * g_x + g_y * s_x) / (s_y + g_y)


def main():
    s_x, s_y, g_x, g_y = map(int, input().split())
    res = solve(s_x, s_y, g_x, g_y)
    print(res)


def test():
    assert abs(solve(1, 1, 7, 2) - 3.0) < 10 ** (-9)
    assert abs(solve(1, 1, 3, 2) - 1.6666666667) < 10 ** (-9)
    assert abs(solve(-9, 99, -999, 9999) + 18.7058823529) < 10 ** (-9)


if __name__ == "__main__":
    test()
    main()
