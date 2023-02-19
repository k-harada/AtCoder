def solve(n, k, s):
    res = []
    count = k
    for c in s:
        if c == "o" and count > 0:
            count -= 1
            res.append("o")
        else:
            res.append("x")
    return "".join(res)


def main():
    n, k = map(int, input().split())
    s = input()
    res = solve(n, k, s)
    print(res)


def test():
    assert solve(10, 3, "oxxoxooxox") == "oxxoxoxxxx"


if __name__ == "__main__":
    test()
    main()
