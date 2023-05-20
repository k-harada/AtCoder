def solve(n, m, s):
    res = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            r = 1
            for k in range(m):
                if s[i][k] == "x" and s[j][k] == "x":
                    r = 0
            res += r
    return res


def main():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    res = solve(n, m, s)
    print(res)


def test():
    assert solve(5, 5, [
        "ooooo",
        "oooxx",
        "xxooo",
        "oxoxo",
        "xxxxx",
    ]) == 5
    assert solve(3, 2, ["ox", "xo", "xx"]) == 1
    assert solve(2, 4, ["xxxx", "oxox"]) == 0


if __name__ == "__main__":
    test()
    main()
