def solve_a(a, b):
    res = max(0, a - 2 * b)
    return res


def main():
    a, b = map(int, input().split())
    res = solve_a(a, b)
    print(res)


def test():
    assert solve_a(12, 4) == 4
    assert solve_a(20, 15) == 0
    assert solve_a(20, 30) == 0


if __name__ == "__main__":
    test()
    main()
