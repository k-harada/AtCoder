def solve(n, xy_list):
    res = 0
    for i in range(n - 1):
        x_i, y_i = xy_list[i]
        for j in range(i + 1, n):
            x_j, y_j = xy_list[j]
            if x_i == x_j:
                pass
            else:
                if abs(y_i - y_j) <= abs(x_i - x_j):
                    res += 1
    return res


def main():
    n = int(input())
    xy_list = [tuple(map(int, input().split())) for _ in range(n)]
    res = solve(n, xy_list)
    print(res)


def test():
    assert solve(3, [(0, 0), (1, 2), (2, 1)]) == 2
    assert solve(1, [(-691, 273)]) == 0


if __name__ == "__main__":
    test()
    main()
