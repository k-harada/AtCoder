def solve_a(a, b):
    if max(a, b) > 9:
        res = -1
    else:
        res = a * b
    return res


def main():
    # input
    a, b = map(int, input().split())
    res = solve_a(a, b)
    print(res)


def test():
    assert solve_a(2, 5) == 10
    assert solve_a(5, 10) == -1
    assert solve_a(9, 9) == 81


if __name__ == "__main__":
    test()
    main()
