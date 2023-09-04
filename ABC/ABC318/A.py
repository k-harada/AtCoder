def solve(n, m, p):
    res = 0
    for i in range(m, n + 1, p):
        res += 1
    return res


def main():
    n, m, p = map(int, input().split())
    res = solve(n, m, p)
    print(res)


def test():
    assert solve(13, 3, 5) == 3
    assert solve(5, 6, 6) == 0
    assert solve(200000, 314, 318) == 628


if __name__ == "__main__":
    test()
    main()
