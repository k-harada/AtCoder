def solve(n, a):
    res = [[""] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            t = min(min(i, (n - 1 - i)), min(j, (n - 1 - j))) + 1
            if t % 4 == 0:
                res[i][j] = a[i][j]
            elif t % 4 == 1:
                res[i][j] = a[n - 1 - j][i]
            elif t % 4 == 2:
                res[i][j] = a[n - 1 - i][n - 1 - j]
            else:
                res[i][j] = a[j][n - 1 - i]
    return ["".join(r) for r in res]


def main():
    n = int(input())
    a = [input() for _ in range(n)]
    res = solve(n, a)
    for r in res:
        print(r)


def test():
    assert solve(8, [
        ".......#",
        ".......#",
        ".####..#",
        ".####..#",
        ".##....#",
        ".##....#",
        ".#######",
        ".#######"
    ]) == [
        "........",
        "#######.",
        "#.....#.",
        "#.###.#.",
        "#.#...#.",
        "#.#####.",
        "#.......",
        "########"
    ]
    assert solve(6, [
        ".#.#.#",
        "##.#..",
        "...###",
        "###...",
        "..#.##",
        "#.#.#."
    ]) == [
        "#.#.#.",
        ".#.#.#",
        "#.#.#.",
        ".#.#.#",
        "#.#.#.",
        ".#.#.#"
    ]


if __name__ == "__main__":
    test()
    main()
