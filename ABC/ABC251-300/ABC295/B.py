def solve(r, c, b):
    res = [[b[i][j] for j in range(c) ] for i in range(r)]
    for i in range(r):
        for j in range(c):
            if b[i][j] in "123456789":
                d = int(b[i][j])
                for s in range(r):
                    for t in range(c):
                        if abs(i - s) + abs(t - j) <= d:
                            res[s][t] = "."
    return ["".join(res[i]) for i in range(r)]


def main():
    r, c = map(int, input().split())
    b = [input() for _ in range(r)]
    res = solve(r, c, b)
    for r in res:
        print(r)


def test():
    assert solve(4, 4, [".1.#", "###.", ".#2.", "#.##"]) == ["...#", "#...", "....", "#..."]
    assert solve(2, 5, ["..#.#", "###.#"]) == ["..#.#", "###.#"]
    assert solve(2, 3, ["11#", "###"]) == ["...", "..#"]


if __name__ == "__main__":
    test()
    main()
