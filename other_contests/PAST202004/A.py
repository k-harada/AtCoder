def solve(s1, s2):
    if s1[0] == s2[0] == "B":
        return abs(int(s1[1:]) - int(s2[1:]))
    elif s1[-1] == s2[-1] == "F":
        return abs(int(s1[:-1]) - int(s2[:-1]))
    elif s1[0] == "B":
        return int(s1[1:]) + int(s2[:-1]) - 1
    else:
        return int(s1[:-1]) + int(s2[1:]) - 1


def main():
    s1, s2 = input().split()
    res = solve(s1, s2)
    print(res)


def test():
    assert solve("1F", "5F") == 4
    assert solve("B1", "B7") == 6
    assert solve("1F", "B1") == 1
    assert solve("B9", "9F") == 17


if __name__ == "__main__":
    test()
    main()
