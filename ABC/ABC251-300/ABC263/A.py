def solve(a, b, c, d, e):
    hands = [a, b, c, d, e]
    if len(set(hands)) == 2 and 2 <= hands.count(a) <= 3:
        return "Yes"
    else:
        return "No"


def main():
    a, b, c, d, e = map(int, input().split())
    res = solve(a, b, c, d, e)
    print(res)


def test():
    assert solve(1, 2, 1, 2, 1) == "Yes"
    assert solve(12, 12, 11, 1, 2) == "No"
    assert solve(1, 1, 1, 1, 2) == "No"


if __name__ == "__main__":
    test()
    main()
