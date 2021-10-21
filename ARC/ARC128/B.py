def solve(t, rgb_list):
    res_list = []
    for r, g, b in rgb_list:
        res = 10 ** 14 + 7
        if (r - g) % 3 == 0:
            res = min(res, abs(r - g) // 3 + (abs(r - g) // 3 + (r + g)) // 2)
        if (g - b) % 3 == 0:
            res = min(res, abs(g - b) // 3 + (abs(g - b) // 3 + (g + b)) // 2)
        if (b - r) % 3 == 0:
            res = min(res, abs(b - r) // 3 + (abs(b - r) // 3 + (b + r)) // 2)
        if res == 10 ** 14 + 7:
            res_list.append(-1)
        else:
            res_list.append(res)
    return res_list


def main():
    t = int(input())
    rgb_list = [tuple(map(int, input().split())) for _ in range(t)]
    res = solve(t, rgb_list)
    for r in res:
        print(r)


def test():
    assert solve(3, [(1, 2, 2), (1, 2, 3), (1, 2, 4)]) == [2, -1, 4]


if __name__ == "__main__":
    test()
    main()
