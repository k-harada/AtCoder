def solve(s, l, r):
    if s < l:
        return l
    elif s > r:
        return r
    else:
        return s


def main():
    s, l, r = map(int, input().split())
    res = solve(s, l, r)
    print(res)


def test():
    assert solve(5, 1, 5) == 5
    assert solve(2, 7, 10) == 7
    assert solve(20, 3, 5) == 5


if __name__ == "__main__":
    test()
    main()
