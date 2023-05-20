def solve(s):
    res = ""
    for i in range(len(s) // 2):
        res = res + s[2 * i + 1]
        res = res + s[2 * i]
    return res


def main():
    s = input()
    res = solve(s)
    print(res)


def test():
    assert solve("abcdef") == "badcfe"
    assert solve("aaaa") == "aaaa"
    assert solve("atcoderbeginnercontest") == "taocedbrgeniencrnoetts"


if __name__ == "__main__":
    test()
    main()
