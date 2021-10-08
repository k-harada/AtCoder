def solve(k, a, b):
    a10 = int(str(a), k)
    b10 = int(str(b), k)
    return a10 * b10


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
