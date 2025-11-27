def solve(r, c, b):
    empty = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if b[i][j].isdigit():
                d = int(b[i][j])
                for p in range(r):
                    for q in range(c):
                        if abs(p - i) + abs(q - j) <= d:
                            empty[p][q] = 1
    res = []
    for i in range(r):
        r = ""
        for j in range(c):
            if empty[i][j] == 1:
                r += "."
            else:
                r += b[i][j]
        res.append(r)
    return res


def main():
    r, c = map(int, input().split())
    b = [input() for _ in range(r)]
    res = solve(r, c, b)
    for r in res:
        print(r)


def test():
    assert solve(4, 4, [
        ".1.#",
        "###.",
        ".#2.",
        "#.##"
    ]) == ["...#", "#...", "....", "#..."]
    assert solve(2, 5, ["..#.#", "###.#"]) == ["..#.#", "###.#"]
    assert solve(2, 3, ["11#", "###"]) == ["...", "..#"]
    assert solve(4, 6, ["#.#3#.", "###.#.", "##.###", "#1..#."]) == ["......", "#.....", "#....#", "....#."]


if __name__ == "__main__":
    test()
    main()
