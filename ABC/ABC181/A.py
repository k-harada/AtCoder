def solve(n):
    if n % 2 == 0:
        return 'White'
    else:
        return 'Black'


def main():
    n = int(input())
    res = solve(n)
    print(res)


def test():
    assert solve(2) == 'White'
    assert solve(5) == 'Black'


if __name__ == "__main__":
    test()
    main()
