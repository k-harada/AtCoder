def solve(l1, r1, l2, r2):
    if l1 <= l2 <= r1:
        return min(r1, r2) - l2
    elif l1 <= r2 <= r1:
        return r2 - max(l1, l2)
    elif l2 <= l1 <= r1 <= r2:
        return r1 - l1
    else:
        return 0


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
