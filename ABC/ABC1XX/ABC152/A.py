def solve(n, m):
    if n == m:
        return "Yes"
    else:
        return "No"


def main():
    n, m = map(int, input().split())
    res = solve(n, m)
    print(res)


def test():
    assert solve(3, 3) == "Yes"
    assert solve(3, 2) == "No"
    assert solve(1, 1) == "Yes"


if __name__ == "__main__":
    test()
    main()
