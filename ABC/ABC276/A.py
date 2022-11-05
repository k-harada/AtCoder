def solve(s):
    res = -1
    for i, c in enumerate(s):
        if c == "a":
            res = i + 1
    return res


def main():
    s = input()
    res = solve(s)
    print(res)


def test():
    assert solve("abcdaxayz") == 7
    assert solve("bcbbbz") == -1
    assert solve("aaaaa") == 5


if __name__ == "__main__":
    test()
    main()
