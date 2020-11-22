def solve(r1, c1, r2, c2):
    # 0
    if r1 == r2 and c1 == c2:
        return 0
    # 1
    if r1 + c1 == r2 + c2 or r1 - c1 == r2 - c2 or abs(r1 - r2) + abs(c1 - c2) <= 3:
        return 1
    # 2
    if (r1 + c1) % 2 == (r2 + c2) % 2:
        return 2
    for x1 in range(r1 - 3, r1 + 4):
        for y1 in range(c1 - 3, c1 + 4):
            if abs(r1 - x1) + abs(c1 - y1) <= 3:
                if x1 + y1 == r2 + c2 or x1 - y1 == r2 - c2 or abs(x1 - r2) + abs(y1 - c2) <= 3:
                    return 2
    return 3


def main():
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())
    res = solve(r1, c1, r2, c2)
    print(res)


def test():
    assert solve(1, 1, 5, 6) == 2
    assert solve(1, 1, 1, 200001) == 2
    assert solve(2, 3, 998244353, 998244853) == 3
    assert solve(1, 1, 1, 1) == 0


if __name__ == "__main__":
    test()
    main()
