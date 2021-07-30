def solve(n, rect_list):
    diff_diff = [[0] * 1001 for _ in range(1001)]
    for lx, ly, rx, ry in rect_list:
        diff_diff[lx][ly] += 1
        diff_diff[lx][ry] -= 1
        diff_diff[rx][ly] -= 1
        diff_diff[rx][ry] += 1

    diff = [0] * 1001
    r = 0
    res = [0] * (n + 1)
    for x in range(1001):
        for y in range(1001):
            diff[y] += diff_diff[x][y]
            r += diff[y]
            res[r] += 1
    # print(res)
    return res[1:]


def main():
    n = int(input())
    rect_list = [tuple(map(int, input().split())) for _ in range(n)]
    res = solve(n, rect_list)
    for r in res:
        print(r)


def test():
    assert solve(2, [(1, 1, 3, 2), (2, 1, 4, 2)]) == [2, 1]
    assert solve(2, [(1, 1, 3, 4), (3, 4, 6, 5)]) == [9, 0]


if __name__ == "__main__":
    # test()
    main()
