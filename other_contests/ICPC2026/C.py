def solve(n, d_list):
    from_left = [0] * (n + 1)
    mi = d_list[0]
    from_left[0] = mi
    for i, d in enumerate(d_list):
        mi = min(mi, d)
        from_left[i + 1] = mi
    from_right = [0] * (n + 1)
    mi = d_list[-1]
    from_right[-1] = mi
    for i, d in enumerate(reversed(d_list)):
        mi = min(mi, d)
        from_right[-(i + 2)] = mi
    # print(from_left)
    # print(from_right)
    res = 0
    for i, d in enumerate(d_list):
        # print(from_left[i], from_right[i], d)
        res += max(0, d - max(from_left[i], from_right[i]))
    return res


def main():
    n = int(input())
    d_list = list(map(int, input().split()))
    res = solve(n, d_list)
    print(res)


def test():
    assert solve(5, [3, 8, 7, 4, 6]) == 7
    assert solve(9, [11, 15, 14, 1, 7, 5, 11, 4, 9]) == 18
    assert solve(6, [4, 6, 6, 6, 4, 3]) == 6
    assert solve(6, [5, 9, 7, 8, 9, 4]) == 13
    assert solve(1, [300]) == 0
    assert solve(2, [300, 400]) == 0


if __name__ == "__main__":
    test()
    main()
