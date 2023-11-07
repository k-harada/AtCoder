def solve(l1, r1, l2, r2):
    res = min(r1, r2) - max(l1, l2)
    if res < 0:
        res = 0
    return res


def main():
    l1, r1, l2, r2 = map(int, input().split())
    res = solve(l1, r1, l2, r2)
    print(res)


def test():
    assert solve(0, 3, 1, 5) == 2
    assert solve(0, 1, 4, 5) == 0
    assert solve(0, 3, 3, 7) == 0


if __name__ == "__main__":
    test()
    main()
