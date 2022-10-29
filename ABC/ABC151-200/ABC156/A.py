def solve(n, r):
    if n <= 10:
        return r + 100 * (10 - n)
    else:
        return r


def main():
    n, r = map(int, input().split())
    res = solve(n, r)
    print(res)


def test():
    assert solve(2, 2919) == 3719
    assert solve(22, 3051) == 3051


if __name__ == "__main__":
    test()
    main()
