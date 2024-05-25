def solve(n, xyz_list):
    set_list = []
    cut_x = [[[-1] * 101 for _1 in range(101)] for _ in range(101)]
    cut_y = [[[-1] * 101 for _1 in range(101)] for _ in range(101)]
    cut_z = [[[-1] * 101 for _1 in range(101)] for _ in range(101)]
    for i, (x1, y1, z1, x2, y2, z2) in enumerate(xyz_list):
        for y in range(y1, y2):
            for z in range(z1, z2):
                if cut_x[x1][y][z] != -1:
                    set_list.append((i, cut_x[x1][y][z]))
                else:
                    cut_x[x1][y][z] = i
                if cut_x[x2][y][z] != -1:
                    set_list.append((i, cut_x[x2][y][z]))
                else:
                    cut_x[x2][y][z] = i
        for x in range(x1, x2):
            for z in range(z1, z2):
                if cut_y[x][y1][z] != -1:
                    set_list.append((i, cut_y[x][y1][z]))
                else:
                    cut_y[x][y1][z] = i
                if cut_y[x][y2][z] != -1:
                    set_list.append((i, cut_y[x][y2][z]))
                else:
                    cut_y[x][y2][z] = i
        for y in range(y1, y2):
            for x in range(x1, x2):
                if cut_z[x][y][z1] != -1:
                    set_list.append((i, cut_z[x][y][z1]))
                else:
                    cut_z[x][y][z1] = i
                if cut_z[x][y][z2] != -1:
                    set_list.append((i, cut_z[x][y][z2]))
                else:
                    cut_z[x][y][z2] = i

    res = [0] * n
    for i, j in set(set_list):
        res[i] += 1
        res[j] += 1
    return res


def main():
    n = int(input())
    xyz_list = [tuple(map(int, input().split())) for _ in range(n)]
    res = solve(n, xyz_list)
    for r in res:
        print(r)


def test():
    assert solve(4, [
        (0, 0, 0, 1, 1, 1),
        (0, 0, 1, 1, 1, 2),
        (1, 1, 1, 2, 2, 2),
        (3, 3, 3, 4, 4, 4),
    ]) == [1, 1, 0, 0]
    assert solve(3, [
        (0, 0, 10, 10, 10, 20),
        (3, 4, 1, 15, 6, 10),
        (0, 9, 6, 1, 20, 10),
    ]) == [2, 1, 1]
    assert solve(8, [
        (0, 0, 0, 1, 1, 1),
        (0, 0, 1, 1, 1, 2),
        (0, 1, 0, 1, 2, 1),
        (0, 1, 1, 1, 2, 2),
        (1, 0, 0, 2, 1, 1),
        (1, 0, 1, 2, 1, 2),
        (1, 1, 0, 2, 2, 1),
        (1, 1, 1, 2, 2, 2),
    ]) == [3, 3, 3, 3, 3, 3, 3, 3]


if __name__ == "__main__":
    # test()
    main()
