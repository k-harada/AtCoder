def solve(n):
    if - 2 ** 31 <= n < 2 ** 31:
        return "Yes"
    else:
        return "No"


def main():
    n = int(input())
    res = solve(n)
    print(res)


def test():
    assert solve(10) == "Yes"
    assert solve(-9876543210) == "No"
    assert solve(483597848400000) == "No"


if __name__ == "__main__":
    test()
    main()
