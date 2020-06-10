def solve(h1, m1, h2, m2, k):
    res = (h2 - h1) * 60 + (m2 - m1) - k
    return res


def main():
    h1, m1, h2, m2, k = map(int, input().split())
    res = solve(h1, m1, h2, m2, k)
    print(res)


def test():
    assert solve(10, 0, 15, 0, 30) == 270
    assert solve(10, 0, 12, 0, 120) == 0


if __name__ == "__main__":
    test()
    main()
