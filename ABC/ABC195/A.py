def solve(m, h):
    if h % m == 0:
        return "Yes"
    else:
        return "No"


def main():
    m, h = map(int, input().split())
    res = solve(m, h)
    print(res)


def test():
    assert solve(10, 120) == "Yes"
    assert solve(10, 125) == "No"


if __name__ == "__main__":
    test()
    main()
