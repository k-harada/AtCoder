def solve(n):
    f = [0] * (n + 1)
    f[0] = 1
    for k in range(1, n + 1):
        f[k] = k * f[k - 1]
    return f[n]


def main():
    n = int(input())
    res = solve(n)
    print(res)


def test():
    assert solve(2) == 2
    assert solve(3) == 6
    assert solve(0) == 1
    assert solve(10) == 3628800


if __name__ == "__main__":
    test()
    main()
