def solve(s):
    res = " ".join(list(s))
    return res


def main():
    s = input()
    res = solve(s)
    print(res)


def test():
    assert solve("ABC") == "A B C"
    assert solve("ZZZZZZZ") == "Z Z Z Z Z Z Z"
    assert solve("OOXXOO") == "O O X X O O"


if __name__ == "__main__":
    test()
    main()
