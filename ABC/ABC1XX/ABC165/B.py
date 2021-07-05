def solve(x):
    res = 0
    v = 100
    while True:
        v = int(v * 1.01)
        res += 1
        if v >= x:
            return res


def main():
    x = int(input())
    res = solve(x)
    print(res)


def test():
    assert solve(103) == 3
    assert solve(1000000000000000000) == 3760
    assert solve(1333333333) == 1706


if __name__ == "__main__":
    test()
    main()
