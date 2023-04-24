def solve(n, s):
    if "-" not in s:
        return -1
    if "o" not in s:
        return -1
    cmax = 0
    c = 0
    for i in range(n):
        if s[i] == "o":
            c += 1
        else:
            c = 0
        cmax = max(cmax, c)
    return cmax


def main():
    n = int(input())
    s = input()
    res = solve(n, s)
    print(res)


def test():
    assert solve(10, "o-oooo---o") == 4
    assert solve(1, "-") == -1
    assert solve(30, "-o-o-oooo-oo-o-ooooooo--oooo-o") == 7


if __name__ == "__main__":
    test()
    main()
