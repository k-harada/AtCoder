x_base = [1, 1, 1, 2, 1, 2, 1, 5, 2, 2, 1, 5, 1, 2, 1, 14, 1, 5, 1, 5, 2, 2, 1, 15, 2, 2, 5, 4, 1, 4, 1, 51]


def solve(k):
    return x_base[k - 1]


def main():
    k = int(input())
    res = solve(k)
    print(res)


def test():
    assert solve(6) == 2
    assert solve(27) == 5


if __name__ == "__main__":
    test()
    main()
