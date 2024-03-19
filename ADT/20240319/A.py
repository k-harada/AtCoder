def solve(h, w, r, c):
    res = 0
    if r > 1:
        res += 1
    if r < h:
        res += 1
    if c > 1:
        res += 1
    if c < w:
        res += 1
    return res


def main():
    h, w = map(int, input().split())
    r, c = map(int, input().split())
    res = solve(h, w, r, c)
    print(res)


def test():
    assert solve(3, 4, 2, 2) == 4
    assert solve(3, 4, 1, 3) == 3
    assert solve(3, 4, 3, 4) == 2
    assert solve(1, 10, 1, 5) == 2
    assert solve(8, 1, 8, 1) == 1
    assert solve(1, 1, 1, 1) == 0


if __name__ == "__main__":
    test()
    main()
