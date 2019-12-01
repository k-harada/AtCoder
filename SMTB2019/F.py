def solve(t1, t2, a1, a2, b1, b2):
    sa = a1 * t1 + a2 * t2
    sb = b1 * t1 + b2 * t2
    if sa == sb:
        return "infinity"
    if a1 > b1:
        if sa >= sb:
            return 0
        else:
            d0 = a1 * t1 - b1 * t1
            d1 = sb - sa
            res = (d0 // d1 + 1) * 2 - 1
            if d0 % d1 == 0:
                res -= 1
    else:
        if sa <= sb:
            return 0
        else:
            d0 = b1 * t1 - a1 * t1
            d1 = sa - sb
            res = (d0 // d1 + 1) * 2 - 1
            if d0 % d1 == 0:
                res -= 1
    return res


def main():
    t1, t2 = map(int, input().split())
    a1, a2 = map(int, input().split())
    b1, b2 = map(int, input().split())
    res = solve(t1, t2, a1, a2, b1, b2)
    print(res)


def test():
    assert solve(1, 2, 10, 10, 12, 4) == 1
    assert solve(100, 1, 101, 101, 102, 1) == "infinity"
    assert solve(12000, 15700, 3390000000, 3810000000, 5550000000, 2130000000) == 113


if __name__ == "__main__":
    test()
    main()
