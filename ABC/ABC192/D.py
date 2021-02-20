def base_x(x, n):
    res = 0
    for i, c in enumerate(reversed(x)):
        res += int(c) * (n ** i)
    return res


def solve(x, m):
    d = max([int(c) for c in x])
    left = d + 1
    right = 10 ** 18 + 10

    if len(x) == 1:
        if int(x) <= m:
            return 1
        else:
            return 0
    if base_x(x, left) > m:
        return 0

    while left < right - 1:
        center = (left + right) // 2
        if base_x(x, center) > m:
            right = center
        else:
            left = center
    # print(left, right)
    return left - (d + 1) + 1


def main():
    x = input()
    m = int(input())
    res = solve(x, m)
    print(res)


def test():
    assert solve("22", 10) == 2
    assert solve("999", 1500) == 3
    assert solve("100000000000000000000000000000000000000000000000000000000000", 1000000000000000000) == 1


if __name__ == "__main__":
    test()
    main()
