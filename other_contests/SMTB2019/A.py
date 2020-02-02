def solve(m1, d1, m2, d2):
    if m1 == m2:
        return 0
    else:
        return 1


def main():
    m1, d1 = map(int, input().split())
    m2, d2 = map(int, input().split())
    res = solve(m1, d1, m2, d2)
    print(res)


def test():
    assert solve(11, 16, 11, 17) == 0
    assert solve(11, 30, 12, 1) == 1


if __name__ == "__main__":
    test()
    main()
