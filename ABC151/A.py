def solve(c):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    i = alpha.index(c)
    return alpha[i + 1]


def main():
    c = input()
    res = solve(c)
    print(res)


def test():
    assert solve("a") == "b"
    assert solve("y") == "z"


if __name__ == "__main__":
    test()
    main()
