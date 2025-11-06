def solve(a, b):
    q = a / b
    r = q - int(q)
    if r < 0.5:
        return a // b
    else:
        return a // b + 1


def main():
    a, b = map(int, input().split())
    res = solve(a, b)
    print(res)


def test():
    assert solve(4, 7) == 1
    assert solve(407, 29) == 14
    assert solve(22, 11) == 2


if __name__ == "__main__":
    test()
    main()
