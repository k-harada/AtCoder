def solve(n, xy_list):
    res = [0] * n
    d_list = [0] * n
    for i in range(n):
        xi, yi = xy_list[i]
        for j in range(n):
            xj, yj = xy_list[j]
            d = (xi - xj) ** 2 + (yi - yj) ** 2
            if d > d_list[i]:
                d_list[i] = d
                res[i] = j + 1
    return res


def main():
    n = int(input())
    xy_list = [tuple(map(int, input().split())) for _ in range(n)]
    res = solve(n, xy_list)
    for r in res:
        print(r)


def test():
    assert solve(4, [(0, 0), (2, 4), (5, 0), (3, 4)]) == [3, 3, 1, 1]
    assert solve(6, [(3, 2), (1, 6), (4, 5), (1, 3), (5, 5), (9, 8)]) == [6, 6, 6, 6, 6, 4]


if __name__ == "__main__":
    test()
    main()
