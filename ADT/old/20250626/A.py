def solve(n):
    if 2 <= n <= 4:
        return "No"
    else:
        return "Yes"


def main():
    n = int(input())
    res = solve(n)
    print(res)


def test():
    assert solve(5) == "Yes"
    assert solve(2) == "No"
    assert solve(623947744) == "Yes"


if __name__ == "__main__":
    test()
    main()
