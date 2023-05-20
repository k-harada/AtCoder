def solve(n, s):
    t = []
    for i in range(n):
        if s[i:i + 2] == "na":
            t.append("ny")
        else:
            t.append(s[i])
    return "".join(t)


def main():
    n = int(input())
    s = input()
    res = solve(n, s)
    print(res)


def test():
    assert solve(4, "naan") == "nyaan"
    assert solve(4, "near") == "near"
    assert solve(8, "national") == "nyationyal"


if __name__ == "__main__":
    test()
    main()
