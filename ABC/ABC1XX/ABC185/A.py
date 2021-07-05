def solve(a1, a2, a3, a4):
    return min([a1, a2, a3, a4])


def main():
    a1, a2, a3, a4 = map(int, input().split())
    res = solve(a1, a2, a3, a4)
    print(res)


def test():
    assert solve(5, 3, 7, 11) == 3
    assert solve(100, 100, 1, 100) == 1


if __name__ == "__main__":
    test()
    main()
