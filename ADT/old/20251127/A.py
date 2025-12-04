ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def solve(n, x):
    q = (x - 1) // n
    res = ALPHABET[q]
    return res


def main():
    n, x = map(int, input().split())
    res = solve(n, x)
    print(res)


def test():
    assert solve(1, 3) == "C"
    assert solve(2, 12) == "F"


if __name__ == "__main__":
    test()
    main()
