def solve(n, d, s):
    flags = [1] * d
    for i in range(n):
        for j in range(d):
            if s[i][j] == "x":
                flags[j] = 0
    res = 0
    r = 0
    for i in range(d):
        if flags[i] == 1:
            r += 1
        else:
            res = max(res, r)
            r = 0
    res = max(res, r)
    return res


def main():
    n, d = map(int, input().split())
    s = [input() for _ in range(n)]
    res = solve(n, d, s)
    print(res)


def test():
    assert solve(3, 5, ["xooox", "oooxx", "oooxo"]) == 2
    assert solve(3, 3, ["oxo", "oxo", "oxo"]) == 1
    assert solve(3, 3, ["oox", "oxo", "xoo"]) == 0
    assert solve(1, 7, ["ooooooo"]) == 7
    assert solve(5, 15, [
        "oxooooooooooooo",
        "oxooxooooooooox",
        "oxoooooooooooox",
        "oxxxooooooxooox",
        "oxooooooooxooox"
    ]) == 5


if __name__ == "__main__":
    test()
    main()
