def solve(n):
    return 2 ** n


def main():
    n = int(input())
    res = solve(n)
    print(res)


def test():
    assert solve(3) == 8
    assert solve(30) == 1073741824


if __name__ == "__main__":
    test()
    main()
