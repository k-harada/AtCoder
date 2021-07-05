def solve(n):
    res = 0
    if n >= 10 ** 3:
        res += n - 10 ** 3 + 1
    if n >= 10 ** 6:
        res += n - 10 ** 6 + 1
    if n >= 10 ** 9:
        res += n - 10 ** 9 + 1
    if n >= 10 ** 12:
        res += n - 10 ** 12 + 1
    if n >= 10 ** 15:
        res += n - 10 ** 15 + 1
    return res


def main():
    n = int(input())
    res = solve(n)
    print(res)


def test():
    assert solve(1010) == 11
    assert solve(27182818284590) == 107730272137364


if __name__ == "__main__":
    test()
    main()
