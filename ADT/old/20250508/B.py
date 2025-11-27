def solve(r):
    if r % 100 == 0:
        return 100
    else:
        return 100 - (r % 100)


def main():
    r = int(input())
    res = solve(r)
    print(res)


def test():
    assert solve(123) == 77
    assert solve(250) == 50
    assert solve(100) == 100


if __name__ == "__main__":
    test()
    main()
