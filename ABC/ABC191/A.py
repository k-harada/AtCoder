def solve(v, t, s, d):
    if v * t <= d <= v * s:
        return "No"
    else:
        return "Yes"


def main():
    v, t, s, d = map(int, input().split())
    res = solve(v, t, s, d)
    print(res)


def test():
    assert solve(10, 3, 5, 20) == "Yes"
    assert solve(10, 3, 5, 30) == "No"


if __name__ == "__main__":
    test()
    main()
