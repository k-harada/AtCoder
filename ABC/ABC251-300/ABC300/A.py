def solve(n, a, b, c_list):
    r = a + b
    return c_list.index(r) + 1


def main():
    n, a, b = map(int, input().split())
    c_list = list(map(int, input().split()))
    res = solve(n, a, b, c_list)
    print(res)


def test():
    assert solve(3, 125, 175, [200, 300, 400]) == 2
    assert solve(1, 1, 1, [2]) == 1
    assert solve(5, 123, 456, [135, 246, 357, 468, 579]) == 5


if __name__ == "__main__":
    test()
    main()
