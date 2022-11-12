def solve(n, m, abc_list):
    res = 0
    for t in range(8):
        r_list = []
        d = t // 4
        if d == 0:
            d = -1
        e = (t // 2) % 2
        if e == 0:
            e = -1
        f = t % 2
        if f == 0:
            f = -1
        for a, b, c in abc_list:
            r = a * d + b * e + c * f
            r_list.append(r)

        r_list_s = list(sorted(r_list, reverse=True))
        res = max(res, sum(r_list_s[:m]))
    return res


def main():
    n, m = map(int, input().split())
    abc_list = [tuple(map(int, input().split())) for _ in range(n)]
    res = solve(n, m, abc_list)
    print(res)


def test():
    assert solve(5, 3, [[3, 1, 4], [1, 5, 9], [2, 6, 5], [3, 5, 8], [9, 7, 9]]) == 56
    assert solve(5, 3, [[1, -2, 3], [-4, 5, -6], [7, -8, -9], [-10, 11, -12], [13, -14, 15]]) == 54
    assert solve(10, 5, [
        [10, -80, 21], [23, 8, 38], [-94, 28, 11], [-26, -2, 18], [-69, 72, 79],
        [-26, -86, -54], [-72, -50, 59], [21, 65, -32], [40, -94, 87], [-62, 18, 82]
    ]) == 638
    assert solve(3, 2, [
        [2000000000, -9000000000, 4000000000],
        [7000000000, -5000000000, 3000000000],
        [6000000000, -1000000000, 8000000000]
    ]) == 30000000000


if __name__ == "__main__":
    test()
    main()
