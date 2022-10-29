def solve(n, x, s):
    res = x
    for t in s:
        if t == 'o':
            res += 1
        else:
            res -= 1
            res = max(res, 0)
    return res


def main():
    n, x = map(int, input().split())
    s = input()
    res = solve(n, x, s)
    print(res)


def test():
    assert solve(3, 0, 'xox') == 0
    assert solve(20, 199999, 'oooooooooxoooooooooo') == 200017
    assert solve(20, 10, 'xxxxxxxxxxxxxxxxxxxx') == 0


if __name__ == "__main__":
    test()
    main()
