def solve(x):
    s = 0
    for i in range(360):
        s += x
        if s % 360 == 0:
            return i + 1
    return 0


def main():
    x = int(input())
    res = solve(x)
    print(res)


def test():
    assert solve(90) == 4
    assert solve(1) == 360


if __name__ == "__main__":
    test()
    main()
