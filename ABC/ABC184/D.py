def solve(a, b, c):
    e_table = [[[0.0] * 101 for _1 in range(101)] for _2 in range(101)]
    for x in range(100, a - 1, -1):
        for y in range(100, b - 1, -1):
            for z in range(100, c - 1, -1):
                if max([x, y, z]) == 100:
                    continue
                e_table[x][y][z] = (
                        x * e_table[x + 1][y][z] + y * e_table[x][y + 1][z] + z * e_table[x][y][z + 1]
                ) / (x + y + z) + 1.0
    # print(e_table[a][b][c])
    return e_table[a][b][c]


def main():
    a, b, c = map(int, input().split())
    res = solve(a, b, c)
    print(res)


def test():
    assert abs(solve(99, 99, 99) - 1.0) < 10 ** (-9)
    assert abs(solve(98, 99, 99) - 1.331081081) < 10 ** (-9)
    # assert abs(solve(0, 0, 1) - 99.0) < 10 ** (-9)
    # assert abs(solve(31, 41, 59) - 91.835008202) < 10 ** (-9)


if __name__ == "__main__":
    test()
    main()
