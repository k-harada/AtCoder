def solve(s):
    res = 0
    for i in range(len(s) - 3):
        if s[i:i + 4] == "ZONe":
            res += 1
    return res


def main():
    s = input()
    res = solve(s)
    print(res)


def test():
    assert solve("abcdZONefghi") == 1
    assert solve("ZONeZONeZONe") == 3
    assert solve("helloAtZoner") == 0


if __name__ == "__main__":
    test()
    main()
