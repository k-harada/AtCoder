def solve_sub(x):
    if x == 2:
        return 1
    res = 2
    d = 2
    while 2 ** d <= x:
        left = 1
        right = x
        while left < right - 1:
            mid = (left + right) // 2
            if mid ** d <= x:
                left = mid
            else:
                right = mid
        # left is the only candidate
        b = left
        z = b ** d
        while z * b <= x:
            z *= b
            d += 1
        r = 1
        y = x
        while y > 0:
            if y % b >= 2:
                r = 0
                break
            y //= b
        # print(d, b, r)
        res += r
        d += 1
    # print(res)
    return res


def solve(t, x_list):
    return [solve_sub(x) for x in x_list]


def main():
    t = int(input())
    x_list = [int(input()) for _ in range(t)]
    res = solve(t, x_list)
    for r in res:
        print(r)


def test():
    assert solve(3, [12, 2, 36]) == [4, 1, 5]
    assert solve(3, [2, 3, 4]) == [1, 2, 3]


if __name__ == "__main__":
    test()
    main()
