def solve(a, b):
    a_int = 0
    b_int = 0
    for a_d in str(a):
        a_int += int(a_d)
    for b_d in str(b):
        b_int += int(b_d)
    return max(a_int, b_int)


def main():
    a, b = map(int, input().split())
    res = solve(a, b)
    print(res)


def test():
    assert solve(123, 234) == 9
    assert solve(593, 953) == 17
    assert solve(100, 999) == 27


if __name__ == "__main__":
    test()
    main()
