def solve(s):
    res = s.count("v") + 2 * s.count("w")
    return res


def main():
    s = input()
    res = solve(s)
    print(res)


def test():
    assert solve("vvwvw") == 7
    assert solve("v") == 1
    assert solve("wwwvvvvvv") == 12


if __name__ == "__main__":
    test()
    main()
