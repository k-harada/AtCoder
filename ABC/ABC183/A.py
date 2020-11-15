def solve(x):
    return max(x, 0)


def main():
    x = int(input())
    res = solve(x)
    print(res)


def test():
    assert solve(1) == 1
    assert solve(0) == 0
    assert solve(-1) == 0


if __name__ == "__main__":
    test()
    main()
