def solve(n, d, xy_list):
    res = 0
    d_square = d * d
    for i in range(n):
        x, y = xy_list[i]
        if x ** 2 + y ** 2 <= d_square:
            res += 1
    return res


def main():
    n, d = map(int, input().split())
    xy_list = [list(map(int, input().split())) for _ in range(n)]
    res = solve(n, d, xy_list)
    print(res)


def test():
    assert solve(4, 5, [[0, 5], [-2, 4], [3, 4], [4, -4]]) == 3
    assert solve(12, 3, [
        [1, 1], [1, 1], [1, 1], [1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3]
    ]) == 7


if __name__ == "__main__":
    test()
    main()
