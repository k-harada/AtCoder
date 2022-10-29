def solve(a, b):
    if a == 0:
        return "Silver"
    elif b == 0:
        return "Gold"
    else:
        return "Alloy"


def main():
    a, b = map(int, input().split())
    res = solve(a, b)
    print(res)


def test():
    assert solve(50, 50) == "Alloy"
    assert solve(100, 0) == "Gold"
    assert solve(0, 100) == "Silver"
    assert solve(100, 2) == "Alloy"


if __name__ == "__main__":
    test()
    main()
