from collections import deque


def solve(h, w, d, s):
    queue = deque()
    res_map = [[d + 1] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if s[i][j] == "H":
                queue.append((i, j, 0))
                res_map[i][j] = 0

    while len(queue):
        i, j, p = queue.popleft()
        if i > 0:
            i1, j1 = i - 1, j
            if s[i1][j1] != "#" and res_map[i1][j1] > p:
                res_map[i1][j1] = p + 1
                if p + 1 < d:
                    queue.append((i1, j1, p + 1))
        if j > 0:
            i1, j1 = i, j - 1
            if s[i1][j1] != "#" and res_map[i1][j1] > p:
                res_map[i1][j1] = p + 1
                if p + 1< d:
                    queue.append((i1, j1, p + 1))
        if i < h - 1:
            i1, j1 = i + 1, j
            if s[i1][j1] != "#" and res_map[i1][j1] > p:
                res_map[i1][j1] = p + 1
                if p + 1 < d:
                    queue.append((i1, j1, p + 1))
        if j < w - 1:
            i1, j1 = i, j + 1
            if s[i1][j1] != "#" and res_map[i1][j1] > p:
                res_map[i1][j1] = p + 1
                if p + 1 < d:
                    queue.append((i1, j1, p + 1))

    res = 0
    for i in range(h):
        for j in range(w):
            if res_map[i][j] <= d:
                res += 1
    return res


def main():
    h, w, d = map(int, input().split())
    s = [input() for _ in range(h)]
    res = solve(h, w, d, s)
    print(res)


def test():
    assert solve(3, 4, 1, ["H...", "#..H", ".#.#"]) == 5
    assert solve(5, 6, 2, ["##...H", "H.....", "..H.#.", ".HH...", ".###.."]) == 21
    assert solve(1, 6, 3, ["...#.."]) == 0


if __name__ == "__main__":
    test()
    main()
