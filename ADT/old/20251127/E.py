def solve(x_1, y_1, x_2, y_2):
    for x in range(x_1 - 2, x_1 + 3):
        for y in range(y_1 - 2, y_1 + 3):
            d_1 = (x_1 - x) ** 2 + (y_1 - y) ** 2
            d_2 = (x_2 - x) ** 2 + (y_2 - y) ** 2
            if d_1 == d_2 == 5:
                return "Yes"
    return "No"


def main():
    x_1, y_1, x_2, y_2 = map(int, input().split())
    res = solve(x_1, y_1, x_2, y_2)
    print(res)


def test():
    assert solve(0, 0, 3, 3) == "Yes"
    assert solve(0, 1, 2, 3) == "No"
    assert solve(1000000000, 1000000000, 999999999, 999999999) == "Yes"


if __name__ == "__main__":
    test()
    main()
