def solve(n, s):
    c_max = 0
    # 横をサーチ
    for i in range(n):
        c = 0
        for j in range(6):
            if s[i][j] == "#":
                c += 1
        c_max = max(c_max, c)
        for j in range(6, n):
            if s[i][j] == "#":
                c += 1
            if s[i][j - 6] == "#":
                c -= 1
            c_max = max(c_max, c)

    # 縦をサーチ
    for j in range(n):
        c = 0
        for i in range(6):
            if s[i][j] == "#":
                c += 1
        c_max = max(c_max, c)
        for i in range(6, n):
            if s[i][j] == "#":
                c += 1
            if s[i - 6][j] == "#":
                c -= 1
            c_max = max(c_max, c)

    # 斜めをサーチ1
    for i in range(n - 5):
        c = 0
        for j in range(6):
            if s[i + j][j] == "#":
                c += 1
        c_max = max(c_max, c)
        for j in range(6, n - i):
            if s[i + j][j] == "#":
                c += 1
            if s[i + j - 6][j - 6] == "#":
                c -= 1
            c_max = max(c_max, c)

    # 斜めをサーチ2
    for i in range(n - 5):
        c = 0
        for j in range(6):
            if s[j][i + j] == "#":
                c += 1
        c_max = max(c_max, c)
        for j in range(6, n - i):
            if s[j][i + j] == "#":
                c += 1
            if s[j - 6][i + j - 6] == "#":
                c -= 1
            c_max = max(c_max, c)

    # 斜めをサーチ3
    for i in range(5, n):
        c = 0
        for j in range(6):
            if s[i - j][j] == "#":
                c += 1
        c_max = max(c_max, c)
        for j in range(6, i + 1):
            if s[i - j][j] == "#":
                c += 1
            if s[i - j + 6][j - 6] == "#":
                c -= 1
            c_max = max(c_max, c)

    # 斜めをサーチ4
    for i in range(n - 5):
        c = 0
        for j in range(6):
            if s[i + j][n - 1 - j] == "#":
                c += 1
        c_max = max(c_max, c)
        for j in range(6, n - i):
            if s[i + j][n - 1 - j] == "#":
                c += 1
            if s[i + j - 6][n - 1 - j + 6] == "#":
                c -= 1
            c_max = max(c_max, c)
    # print(c_max)
    if c_max >= 4:
        return "Yes"
    else:
        return "No"


def main():
    n = int(input())
    s = [input() for _ in range(n)]
    res = solve(n, s)
    print(res)


def test():
    assert solve(8, [
        "........",
        "........",
        ".#.##.#.",
        "........",
        "........",
        "........",
        "........",
        "........"
    ]) == "Yes"
    assert solve(6, [
        "######",
        "######",
        "######",
        "######",
        "######",
        "######"
    ]) == "Yes"
    assert solve(10, [
        "..........",
        "#..##.....",
        "..........",
        "..........",
        "....#.....",
        "....#.....",
        ".#...#..#.",
        "..........",
        "..........",
        ".........."
    ]) == "No"


if __name__ == "__main__":
    test()
    main()
