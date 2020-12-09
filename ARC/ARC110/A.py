def solve(n):
    res = 16 * 27 * 25 * 7 * 11 * 13 * 17 * 19 * 23 * 29 + 1
    return res


def main():
    n = int(input())
    res = solve(n)
    print(res)


def test():
    res = solve(2)
    for i in range(2, 31):
        assert res % i == 1


if __name__ == "__main__":
    test()
    main()
