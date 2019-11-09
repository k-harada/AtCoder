def solve(n):
    if n % 2 == 0:
        return n // 2 - 1
    else:
        return (n - 1) // 2


def main():
    n = int(input())
    res = solve(n)
    print(res)


def test():
    assert solve(4) == 1
    assert solve(999999) == 499999


if __name__ == "__main__":
    test()
    main()
