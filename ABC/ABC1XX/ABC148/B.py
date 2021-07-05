def solve(n, s, t):
    res = ""
    for i in range(n):
        res += s[i] + t[i]
    return res


def main():
    n = int(input())
    s, t = input().split()
    res = solve(n, s, t)
    print(res)


def test():
    assert solve(2, "ip", "cc") == "icpc"
    assert solve(8, "hmhmnknk", "uuuuuuuu") == "humuhumunukunuku"
    assert solve(5, "aaaaa", "aaaaa") == "aaaaaaaaaa"


if __name__ == "__main__":
    test()
    main()
