def solve(a, b, k):
    res = 0
    x = a
    while x < b:
        x *= k
        res += 1
    return res


def main():
    a, b, k = map(int, input().split())
    res = solve(a, b, k)
    print(res)


def test():
    assert solve(1, 4, 2) == 2
    assert solve(7, 7, 10) == 0
    assert solve(31, 415926, 5) == 6


if __name__ == "__main__":
    test()
    main()
