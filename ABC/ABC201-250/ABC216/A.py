def solve(xy):
    x, y = map(int, xy.split("."))
    if 0 <= y <= 2:
        return str(x) + "-"
    elif 3 <= y <= 6:
        return str(x)
    else:
        return str(x) + "+"


def main():
    xy = input()
    res = solve(xy)
    print(res)


def test():
    assert solve("15.8") == "15+"
    assert solve("1.0") == "1-"
    assert solve("12.5") == "12"


if __name__ == "__main__":
    test()
    main()
