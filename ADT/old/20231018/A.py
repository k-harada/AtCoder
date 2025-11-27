def solve(k):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return alphabet[:k]


def main():
    k = int(input())
    res = solve(k)
    print(res)


def test():
    assert solve(3) == "ABC"
    assert solve(1) == "A"


if __name__ == "__main__":
    test()
    main()
