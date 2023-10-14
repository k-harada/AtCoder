def solve(n):
    z = n
    while z % 2 == 0:
        z //= 2
    while z % 3 == 0:
        z //= 3
    if z == 1:
        return "Yes"
    else:
        return "No"


def main():
    n = int(input())
    res = solve(n)
    print(res)


def test():
    assert solve(324) == "Yes"
    assert solve(5) == "No"
    assert solve(32) == "Yes"
    assert solve(37748736) == "Yes"


if __name__ == "__main__":
    test()
    main()
