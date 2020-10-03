def solve(a, b):
    x = (a + b) // 2
    y = (a - b) // 2
    return " ".join([str(x), str(y)])


def main():
    a, b = map(int, input().split())
    res = solve(a, b)
    print(res)


def test():
    assert solve(2, -2) == "0 2"
    assert solve(3, 1) == "2 1"


if __name__ == "__main__":
    test()
    main()
