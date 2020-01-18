def solve(h, w, n):
    s = max(h, w)
    return (n + (s - 1)) // s


def main():
    h = int(input())
    w = int(input())
    n = int(input())
    res = solve(h, w, n)
    print(res)


def test():
    assert solve(3, 7, 10) == 2
    assert solve(14, 12, 112) == 8
    assert solve(2, 100, 200) == 2


if __name__ == "__main__":
    test()
    main()
