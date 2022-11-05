def solve(x):
    if x in [3, 5, 7]:
        return "YES"
    else:
        return "NO"


def main():
    x = int(input())
    res = solve(x)
    print(res)


def test():
    assert solve(5) == "YES"
    assert solve(6) == "NO"


if __name__ == "__main__":
    test()
    main()
