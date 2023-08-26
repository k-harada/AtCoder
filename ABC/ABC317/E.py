from collections import deque


def solve(h, w, a):
    b = [[-1] * w for _ in range(h)]
    s = None
    t = None
    for i in range(h):
        for j in range(w):
            if a[i][j] in ["#", ">", "v", "<", "^"]:
                b[i][j] = 2
            elif a[i][j] == "S":
                s = (i, j)
            elif a[i][j] == "G":
                t = (i, j)
    for i in range(h):
        for j in range(w):
            if a[i][j] == ">":
                for j_ in range(j + 1, w):
                    if b[i][j_] == 2:
                        break
                    b[i][j_] = 1
            if a[i][j] == "v":
                for i_ in range(i + 1, h):
                    if b[i_][j] == 2:
                        break
                    b[i_][j] = 1
            if a[i][j] == "<":
                for j_ in range(j - 1, -1, -1):
                    if b[i][j_] == 2:
                        break
                    b[i][j_] = 1
            if a[i][j] == "^":
                for i_ in range(i - 1, -1, -1):
                    if b[i_][j] == 2:
                        break
                    b[i_][j] = 1
    # print(b)
    b[s[0]][s[1]] = 0
    queue = deque([s])
    while len(queue):
        x, y = queue.popleft()
        if x > 0:
            if b[x - 1][y] == -1:
                b[x - 1][y] = b[x][y] + 1
                queue.append((x - 1, y))
        if x < h - 1:
            if b[x + 1][y] == -1:
                b[x + 1][y] = b[x][y] + 1
                queue.append((x + 1, y))
        if y > 0:
            if b[x][y - 1] == -1:
                b[x][y - 1] = b[x][y] + 1
                queue.append((x, y - 1))
        if y < w - 1:
            if b[x][y + 1] == -1:
                b[x][y + 1] = b[x][y] + 1
                queue.append((x, y + 1))
    # print(b)
    return b[t[0]][t[1]]


def main():
    h, w = map(int, input().split())
    a = [input() for _ in range(h)]
    res = solve(h, w, a)
    print(res)


def test():
    assert solve(5, 7, [
        "....Sv.",
        ".>.....",
        ".......",
        ">..<.#<",
        "^G....>"
    ]) == 15
    assert solve(4, 3, [
        "S..",
        ".<.",
        ".>.",
        "..G",
    ]) == -1


if __name__ == "__main__":
    test()
    main()
