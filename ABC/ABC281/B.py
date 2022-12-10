def solve(s):
    if len(s) != 8:
        return "No"
    if s[0] not in list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        return "No"
    if s[-1] not in list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        return "No"
    for i in range(1, 7):
        if not s[i].isdigit():
            return "No"
    if s[1] == "0":
        return "No"
    return "Yes"


def main():
    s = input()
    res = solve(s)
    print(res)


def test():
    assert solve("Q142857Z") == "Yes"
    assert solve("AB912278C") == "No"
    assert solve("X900000") == "No"
    assert solve("K012345K") == "No"


if __name__ == "__main__":
    test()
    main()
