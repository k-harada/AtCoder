def solve(a, b, c):
    if c % 2 == 0:
        if abs(a) < abs(b):
            return "<"
        elif abs(a) > abs(b):
            return ">"
        else:
            return "="
    else:
        if a < b:
            return "<"
        elif a > b:
            return ">"
        else:
            return "="


def main():
    a, b, c = map(int, input().split())
    res = solve(a, b, c)
    print(res)


def test():
    assert solve(3, 2, 4) == ">"
    assert solve(-7, 7, 2) == "="
    assert solve(-8, 6, 3) == "<"


if __name__ == "__main__":
    test()
    main()
