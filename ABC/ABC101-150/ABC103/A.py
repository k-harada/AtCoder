def solve(a1, a2, a3):
    b1 = max([a1, a2, a3])
    b3 = min([a1, a2, a3])
    b2 = sum([a1, a2, a3]) - b1 - b3
    res = b1 - b3
    return res


def main():
    a1, a2, a3 = map(int, input().split())
    res = solve(a1, a2, a3)
    print(res)


def test():
    assert solve(1, 6, 3) == 5
    assert solve(11, 5, 5) == 6
    assert solve(100, 100, 100) == 0


if __name__ == "__main__":
    test()
    main()
