def solve(n, m, a_list):
    if m == 0:
        return 1
    last_a = 0
    width_list = []
    for a in sorted(a_list):
        width_list.append(a - last_a - 1)
        last_a = a
    width_list.append(n - max(a_list))

    # width
    width = n
    for w in width_list:
        if w > 0:
            width = min(width, w)

    res = 0
    for w in width_list:
        res += w // width
        if w % width > 0:
            res += 1

    return res


def main():
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, m, a_list)
    print(res)


def test():
    assert solve(5, 2, [1, 3]) == 3
    assert solve(13, 3, [13, 3, 9]) == 6
    assert solve(5, 5, [5, 2, 1, 4, 3]) == 0
    assert solve(1, 0, []) == 1


if __name__ == "__main__":
    test()
    main()
