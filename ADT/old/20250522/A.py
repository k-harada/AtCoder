def solve(a, b):
    res = str(round(round(b / a, 3) + 0.0001, 4))[:-1]
    # print(res)
    return res


def main():
    a, b = map(int, input().split())
    res = solve(a, b)
    print(res)


def test():
    assert solve(7, 4) == "0.571"
    assert solve(7, 3) == "0.429"
    assert solve(2, 1) == "0.500"
    assert solve(10, 10) == "1.000"
    assert solve(1, 0) == "0.000"


if __name__ == "__main__":
    test()
    main()
