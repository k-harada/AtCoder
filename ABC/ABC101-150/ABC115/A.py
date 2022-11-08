def solve(d):
    if d == 25:
        return "Christmas"
    elif d == 24:
        return "Christmas Eve"
    elif d == 23:
        return "Christmas Eve Eve"
    elif d == 22:
        return "Christmas Eve Eve Eve"
    else:
        return "Error"


def main():
    d = int(input())
    res = solve(d)
    print(res)


def test():
    assert solve(25) == "Christmas"
    assert solve(22) == "Christmas Eve Eve Eve"


if __name__ == "__main__":
    test()
    main()
