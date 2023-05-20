def solve(n):
    return list(range(n, -1, -1))


def main():
    n = int(input())
    res = solve(n)
    for r in res:
        print(r)


def test():
    assert solve(3) == [3, 2, 1, 0]


if __name__ == "__main__":
    test()
    main()
