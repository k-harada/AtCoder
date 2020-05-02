def solve(n, s_list):
    res_list = [[] for _ in range(n)]
    res_list[n - 1] = list(s_list[-1])
    for i in range(n - 2, -1, -1):
        res_list[i].append(".")
        for j in range(1, 2 * n - 2):
            if s_list[i][j] == "#":
                if res_list[i + 1][j - 1] == "X" or res_list[i + 1][j] == "X" or res_list[i + 1][j + 1] == "X":
                    res_list[i].append("X")
                else:
                    res_list[i].append("#")
            else:
                res_list[i].append(s_list[i][j])
        res_list[i].append(".")
    # print(["".join(res) for res in res_list])
    return ["".join(res) for res in res_list]


def main():
    n = int(input())
    s_list = [input() for _ in range(n)]
    res = solve(n, s_list)
    for r in res:
        print(r)


def test():
    assert solve(5, ["....#....", "...##X...", "..#####..", ".#X#####.", "#########"]) == [
        "....X....", "...XXX...", "..XX###..", ".#X#####.", "#########"
    ]
    assert solve(2, [".#.", "#X#"]) == [".X.", "#X#"]


if __name__ == "__main__":
    test()
    main()
