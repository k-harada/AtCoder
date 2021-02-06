def solve(x, y, r):
    x_int = round(x * 10000)
    y_int = round(y * 10000)
    r_int = round(r * 10000)
    res = 0

    a = (x_int + r_int) // 10000 * 10000
    a += 10000
    b_low = y_int // 10000 * 10000
    b_high = y_int // 10000 * 10000 + 10000
    while a >= x_int:
        y_sq = r_int ** 2 - (a - x_int) ** 2
        while True:
            if (b_high - y_int) ** 2 <= y_sq:
                res += (a - x_int) // 10000 + 1
                b_high += 10000
            else:
                break
        while True:
            if (b_low - y_int) ** 2 <= y_sq:
                res += (a - x_int) // 10000 + 1
                b_low -= 10000
            else:
                break
        a -= 10000

    a = (x_int - r_int) // 10000 * 10000
    b_low = y_int // 10000 * 10000
    b_high = y_int // 10000 * 10000 + 10000
    while a < x_int:
        y_sq = r_int ** 2 - (a - x_int) ** 2
        while True:
            if (b_high - y_int) ** 2 <= y_sq:
                res += (x_int - a + 9999) // 10000
                b_high += 10000
            else:
                break
        while True:
            if (b_low - y_int) ** 2 <= y_sq:
                res += (x_int - a + 9999) // 10000
                b_low -= 10000
            else:
                break
        a += 10000
    # print(res)
    return res


def main():
    x, y, r = map(float, input().split())
    res = solve(x, y, r)
    print(res)


def test():
    assert solve(0.2, 0.8, 1.1) == 3
    assert solve(100, 100, 1) == 5
    assert solve(42782.4720, 31949.0192, 99999.99) == 31415920098


if __name__ == "__main__":
    test()
    main()
