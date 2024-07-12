def solve(a, b, c, d, e, f, g, h, i, j, k, l):
    # どれかの頂点が内点になってればいい
    res_x = 0
    for x in range(1000):
        if a < x + 0.5 < d and g < x + 0.5 < j:
            res_x = 1
    res_y = 0
    for y in range(1000):
        if b < y + 0.5 < e and h < y + 0.5 < k:
            res_y = 1
    res_z = 0
    for z in range(1000):
        if c < z + 0.5 < f and i < z + 0.5 < l:
            res_z = 1
    res = res_x * res_y * res_z
    if res == 1:
        return "Yes"
    else:
        return "No"


def main():
    a, b, c, d, e, f = map(int, input().split())
    g, h, i, j, k, l = map(int, input().split())
    res = solve(a, b, c, d, e, f, g, h, i, j, k, l)
    print(res)


def test():
    assert solve(0, 0, 0, 4, 5, 6, 2, 3, 4, 5, 6, 7) == "Yes"
    assert solve(0, 0, 0, 2, 2, 2, 0, 0, 2, 2, 2, 4) == "No"
    assert solve(0, 0, 0, 1000, 1000, 1000, 10, 10, 10, 100, 100, 100) == "Yes"


if __name__ == "__main__":
    test()
    main()
