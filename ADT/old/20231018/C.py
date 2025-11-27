def solve(k, a, b):
    a_10 = 0
    b_10 = 0
    for i, c in enumerate(reversed(str(a))):
        a_10 += int(c) * (k ** i)
    for i, c in enumerate(reversed(str(b))):
        b_10 += int(c) * (k ** i)
    return a_10 * b_10


def main():
    k = int(input())
    a, b = map(int, input().split())
    res = solve(k, a, b)
    print(res)


def test():
    assert solve(2, 1011, 10100) == 220
    assert solve(7, 123, 456) == 15642


if __name__ == "__main__":
    test()
    main()
