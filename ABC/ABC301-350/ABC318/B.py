def solve(n, abcd_list):
    field = [[0] * 100 for _ in range(100)]
    for a, b, c, d in abcd_list:
        for i in range(a, b):
            for j in range(c, d):
                field[i][j] = 1
    res = 0
    for i in range(100):
        for j in range(100):
            res += field[i][j]

    return res


def main():
    n = int(input())
    abcd_list = [tuple(map(int, input().split())) for _ in range(n)]
    res = solve(n, abcd_list)
    print(res)


def test():
    assert solve(3, [(0, 5, 1, 3), (1, 4, 0, 5), (2, 5, 2, 4)]) == 20
    assert solve(2, [(0, 100, 0, 100), (0, 100, 0, 100)]) == 10000
    assert solve(3, [(0, 1, 0, 1), (0, 3, 0, 5), (5, 10, 0, 10)]) == 65


if __name__ == "__main__":
    test()
    main()
