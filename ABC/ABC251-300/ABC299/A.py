def solve(n, s):
    x = []
    y = 0
    for i in range(n):
        if s[i] == "|":
            x.append(i)
        elif s[i] == "*":
            y = i
    if x[0] < y < x[1]:
        return "in"
    else:
        return "out"


def main():
    n = int(input())
    s = input()
    res = solve(n, s)
    print(res)


def test():
    assert solve(10, ".|..*...|.") == "in"
    assert solve(10, ".|..|.*...") == "out"
    assert solve(3, "|*|") == "in"


if __name__ == "__main__":
    test()
    main()
