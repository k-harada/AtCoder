def solve(a, b, c, d):
    return [(a + b) * (c - d), "Takahashi"]


def main():
    a, b, c, d = map(int, input().split())
    res = solve(a, b, c, d)
    for r in res:
        print(r)


def test():
    assert solve(1, 2, 5, 3) == [6, "Takahashi"]
    assert solve(10, -20, 30, -40) == [-700, "Takahashi"]
    assert solve(100, 100, 100, -100) == [40000, "Takahashi"]


if __name__ == "__main__":
    test()
    main()
