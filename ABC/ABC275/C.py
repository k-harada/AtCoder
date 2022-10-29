def solve(s_list):
    res = 0
    # 左上を決める
    for i in range(9):
        for j in range(9):
            if s_list[i][j] == ".":
                continue
            # 右下を決める
            for u in range(i, 9):
                for v in range(j + 1, 9):
                    if s_list[u][v] == ".":
                        continue
                    # 残りの頂点を求める
                    p = u + (v - j)
                    q = v - (u - i)
                    if min(p, q) < 0 or max(p, q) > 8:
                        continue
                    if s_list[p][q] == ".":
                        continue
                    s = p - (u - i)
                    t = q - (v - j)
                    if min(s, t) < 0 or max(s, t) > 8:
                        continue
                    if s_list[s][t] == ".":
                        continue
                    res += 1

    return res


def main():
    s_list = [input() for _ in range(9)]
    res = solve(s_list)
    print(res)


def test():
    assert solve([
        "##.......",
        "##.......",
        ".........",
        ".......#.",
        ".....#...",
        "........#",
        "......#..",
        ".........",
        "........."
    ]) == 2
    assert solve([
        ".#.......",
        "#.#......",
        ".#.......",
        ".........",
        "....#.#.#",
        ".........",
        "....#.#.#",
        "........#",
        "........."
    ]) == 3


if __name__ == "__main__":
    test()
    main()
