def solve(s):
    a_list = list(map(int, s.split()))
    res = 0
    for i, a in enumerate(a_list):
        res += a * (2 ** i)
    return res


def main():
    s = input()
    res = solve(s)
    print(res)


def test():
    assert solve("1 0 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0") == 13
    assert solve("1 0 1 0 1 0 0 0 0 1 0 0 1 1 0 1 1 1 1 0 0 0 1 0 0 1 1 1 1 1 1 0 0 0 0 1 0 1 0 1 0 1 1 1 1 0 0 1 1 0 0 0 0 1 0 1 0 1 0 1 0 0 0 0") == 766067858140017173


if __name__ == "__main__":
    test()
    main()
