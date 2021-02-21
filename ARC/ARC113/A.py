def solve(k):
    res = 0
    # a < b < c
    for a in range(1, k + 1):
        if a ** 3 > k:
            break
        for b in range(a + 1, k + 1):
            c_max = k // (a * b)
            if c_max > b:
                res += 6 * (c_max - b)
            else:
                break
    # a = b < c
    for a in range(1, k + 1):
        if a ** 3 > k:
            break
        b = a
        c_max = k // (a * b)
        if c_max > b:
            res += 3 * (c_max - b)
    # a < b = c
    for a in range(1, k + 1):
        if a ** 3 > k:
            break
        for b in range(a + 1, k + 1):
            if a * b * b <= k:
                res += 3
            else:
                break
    # a = b = c
    for a in range(1, k + 1):
        if a ** 3 > k:
            break
        else:
            res += 1
    return res


def main():
    k = int(input())
    res = solve(k)
    print(res)


def test():
    assert solve(2) == 4
    assert solve(10) == 53
    assert solve(31415) == 1937281


if __name__ == "__main__":
    test()
    main()
