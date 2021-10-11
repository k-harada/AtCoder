def solve(n):
    res = '0' * (4 - len(str(n))) + str(n)
    return res


def main():
    n = int(input())
    res = solve(n)
    print(res)


def test():
    assert solve(321) == "0321"
    assert solve(7777) == "7777"
    assert solve(1) == "0001"


if __name__ == "__main__":
    test()
    main()
