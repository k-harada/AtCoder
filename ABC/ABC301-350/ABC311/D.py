from collections import deque


def solve(n, m, s):
    visited = [[[0] * 5 for _1 in range(m)] for _2 in range(n)]
    queue = deque([(1, 1, 0)])
    while len(queue):
        x, y, d = queue.popleft()
        # print(x, y, d)
        if visited[x][y][d] == 1:
            continue
        visited[x][y][d] = 1
        if d == 0:
            if s[x - 1][y] == ".":
                queue.append((x - 1, y, 1))
            if s[x][y + 1] == ".":
                queue.append((x, y + 1, 2))
            if s[x + 1][y] == ".":
                queue.append((x + 1, y, 3))
            if s[x][y - 1] == ".":
                queue.append((x, y - 1, 4))
        elif d == 1:
            if s[x - 1][y] == ".":
                queue.append((x - 1, y, 1))
            else:
                queue.append((x, y, 0))
        elif d == 2:
            if s[x][y + 1] == ".":
                queue.append((x, y + 1, 2))
            else:
                queue.append((x, y, 0))
        elif d == 3:
            if s[x + 1][y] == ".":
                queue.append((x + 1, y, 3))
            else:
                queue.append((x, y, 0))
        elif d == 4:
            if s[x][y - 1] == ".":
                queue.append((x, y - 1, 4))
            else:
                queue.append((x, y, 0))
    res = 0
    for i in range(n):
        for j in range(m):
            v = 0
            for k in range(5):
                if visited[i][j][k] == 1:
                    v = 1
            res += v
    # print(res)
    return res


def main():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    res = solve(n, m, s)
    print(res)


def test():
    assert solve(6, 6, [
        "######",
        "#....#",
        "#.#..#",
        "#..#.#",
        "#....#",
        "######"
    ]) == 12


if __name__ == "__main__":
    test()
    main()
