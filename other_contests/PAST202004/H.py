from collections import deque


def solve(n, m, a_list):
    points = [[] for _ in range(11)]
    for i in range(n):
        for j in range(m):
            if a_list[i][j] == "S":
                points[0].append([i, j, 0])
            elif a_list[i][j] == "G":
                points[10].append([i, j, 100000000])
            else:
                points[int(a_list[i][j])].append([i, j, 100000000])

    if min([len(p) for p in points]) == 0:
        return -1

    for i in range(1, 11):
        for k in range(len(points[i])):
            x, y = points[i][k][0], points[i][k][1]
            for x0, y0, d0 in points[i - 1]:
                points[i][k][2] = min(points[i][k][2], d0 + abs(x - x0) + abs(y - y0))

    return points[10][0][2]


def main():
    n, m = map(int, input().split())
    a_list = [input() for _ in range(n)]
    res = solve(n, m, a_list)
    print(res)


def test():
    assert solve(3, 4, ["1S23", "4567", "89G1"]) == 17
    assert solve(1, 11, ["S134258976G"]) == 20
    assert solve(3, 3, ["S12", "4G7", "593"]) == -1


if __name__ == "__main__":
    test()
    main()
