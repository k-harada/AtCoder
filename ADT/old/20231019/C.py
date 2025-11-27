def solve(s):
    flag_1 = 0
    flag_2 = 0
    for c in s:
        if c.isupper():
            flag_1 += 1
        else:
            flag_2 += 1
    if flag_1 * flag_2 == 0:
        return "No"
    if len(set(list(s))) < len(s):
        return "No"
    return "Yes"


def main():
    s = input()
    res = solve(s)
    print(res)


def test():
    assert solve("AtCoder") == "Yes"
    assert solve("Aa") == "Yes"
    assert solve("atcoder") == "No"
    assert solve("Perfect") == "No"


if __name__ == "__main__":
    test()
    main()
