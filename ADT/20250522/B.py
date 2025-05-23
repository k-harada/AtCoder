def solve(a, b):
    if a % b == 0:
        res = a // b
    else:
        res = a // b + 1
    return res


def main():
    a, b = map(int, input().split())
    res = solve(a, b)
    print(res)


def test():
    assert solve(7, 3) == 3
    assert solve(123456789123456789, 987654321) == 124999999
    assert solve(999999999999999998, 2) == 499999999999999999


if __name__ == "__main__":
    test()
    main()
