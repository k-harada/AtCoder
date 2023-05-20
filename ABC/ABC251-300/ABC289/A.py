def solve(s):
    res = ""
    for c in s:
        if c == "0":
            res = res + "1"
        else:
            res = res + "0"
    return res


def main():
    s = input()
    res = solve(s)
    print(res)


def test():
    assert solve("01") == "10"
    assert solve("1011") == "0100"
    assert solve("100100001") == "011011110"


if __name__ == "__main__":
    test()
    main()
