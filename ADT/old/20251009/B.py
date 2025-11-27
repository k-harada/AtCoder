def solve(n, d, s):
    c = s.count(".")
    return c + d


def main():
    n, d = map(int, input().split())
    s = input()
    res = solve(n, d, s)
    print(res)


def test():
    assert solve(5, 2, ".@@.@") == 4
    assert solve(3, 3, "@@@") == 3
    assert solve(10, 4, "@@@.@@.@@.") == 7


if __name__ == "__main__":
    test()
    main()
