def solve(n, k, s):
    res = 0
    ok = 0
    for c in s:
        if c == "O":
            ok += 1
        else:
            ok = 0
        if ok == k:
            res += 1
            ok = 0
    return res


def main():
    n, k = map(int, input().split())
    s = input()
    res = solve(n, k, s)
    print(res)


def test():
    assert solve(7, 3, "OOXOOOO") == 1
    assert solve(12, 2, "OXXOOOXOOOOX") == 3
    assert solve(22, 5, "XXOOOOOOOOXXOOOOOXXXXX") == 2


if __name__ == "__main__":
    test()
    main()
