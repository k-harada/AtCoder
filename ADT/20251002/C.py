direction_map = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def solve(h, w, n):
    field = [["."] * w for _ in range(h)]
    x = 0
    y = 0
    d = 2
    for _ in range(n):
        if field[y][x] == ".":
            field[y][x] = "#"
            d = (d - 1) % 4
            x = (x + direction_map[d][0]) % w
            y = (y + direction_map[d][1]) % h
        else:
            field[y][x] = "."
            d = (d + 1) % 4
            x = (x + direction_map[d][0]) % w
            y = (y + direction_map[d][1]) % h
    res_list = ["".join(r) for r in field]
    # print(res_list)
    return res_list


def main():
    h, w, n = map(int, input().split())
    res = solve(h, w, n)
    for r in res:
        print(r)


def test():
    assert solve(3, 4, 5) == [".#..", "##..", "...."]
    assert solve(2, 2, 1000) == ["..", ".."]
    assert solve(10, 10, 10) == [
        "##........",
        "##........",
        "..........",
        "..........",
        "..........",
        "..........",
        "..........",
        "..........",
        "..........",
        "#........#",
    ]


if __name__ == "__main__":
    test()
    main()
