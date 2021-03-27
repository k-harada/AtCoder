def solve(h, w, x, y, s_list):
    res = 1
    for j in range(y, w):
        if s_list[x - 1][j] == ".":
            res += 1
        else:
            break
    for j in range(y - 2, -1, -1):
        if s_list[x - 1][j] == ".":
            res += 1
        else:
            break
    for i in range(x, h):
        if s_list[i][y - 1] == ".":
            res += 1
        else:
            break
    for i in range(x - 2, -1, -1):
        if s_list[i][y - 1] == ".":
            res += 1
        else:
            break
    return res


def main():
    h, w, x, y = map(int, input().split())
    s_list = [input() for _ in range(h)]
    res = solve(h, w, x, y, s_list)
    print(res)


def test():
    assert solve(4, 4, 2, 2, ["##..", "...#", "#.#.", ".#.#"]) == 4
    assert solve(3, 5, 1, 4, ["#....", "#####", "....#"]) == 4
    assert solve(5, 5, 4, 2, [".#..#", "#.###", "##...", "#..#.", "#.###"]) == 3


if __name__ == "__main__":
    test()
    main()
