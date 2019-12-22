def solve(a, b):
    base = [1, 2, 3]
    base.remove(a)
    base.remove(b)
    return base[0]


def main():
    a = int(input())
    b = int(input())
    res = solve(a, b)
    print(res)


def test():
    assert solve(3, 1) == 2
    assert solve(1, 2) == 3


if __name__ == "__main__":
    test()
    main()
