def solve(n, le, ri):
    res_list = list(range(1, le)) + list(reversed(list(range(le, ri + 1)))) + list(range(ri + 1, n + 1))
    return " ".join([str(a) for a in res_list])


def main():
    n, le, ri = map(int, input().split())
    res = solve(n, le, ri)
    print(res)


def test():
    assert solve(5, 2, 3) == "1 3 2 4 5"
    assert solve(7, 1, 1) == "1 2 3 4 5 6 7"
    assert solve(10, 1, 10) == "10 9 8 7 6 5 4 3 2 1"


if __name__ == "__main__":
    test()
    main()
