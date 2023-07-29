def solve(n, s):
    aa = 0
    bb = 0
    cc = 0
    for i, c in enumerate(s):
        if c == "A":
            aa += 1
        elif c == "B":
            bb += 1
        elif c == "C":
            cc += 1
        if aa > 0 and bb > 0 and cc > 0:
            return i + 1
    return 0


def main():
    n = int(input())
    s = input()
    res = solve(n, s)
    print(res)


def test():
    assert solve(5, "ACABB") == 4
    assert solve(4, "CABC") == 3
    assert solve(30, "AABABBBABABBABABCABACAABCBACCA") == 17


if __name__ == "__main__":
    test()
    main()
