from collections import deque


def solve(n, a, b, s):
    queue = deque()
    queue.append((0, a[0] - 1, a[1] - 1, -1))
    d_mat = [[10 ** 9] * n for _ in range(n)]
    d_mat[a[0] - 1][a[1] - 1] = 0
    while len(queue):
        d, x, y, direction = queue.popleft()
        # print(d, x, y, direction)
        if d > d_mat[x][y]:
            continue
        if x > 0 and y > 0:
            x_, y_ = x - 1, y - 1
            if s[x_][y_] == ".":
                if direction == 0:
                    if d_mat[x_][y_] >= d:
                        d_mat[x_][y_] = d
                        queue.appendleft((d, x_, y_, 0))
                else:
                    if d_mat[x_][y_] >= d + 1:
                        d_mat[x_][y_] = d + 1
                        queue.append((d + 1, x_, y_, 0))
        if x > 0 and y < n - 1:
            x_, y_ = x - 1, y + 1
            if s[x_][y_] == ".":
                if direction == 1:
                    if d_mat[x_][y_] >= d:
                        d_mat[x_][y_] = d
                        queue.appendleft((d, x_, y_, 1))
                else:
                    if d_mat[x_][y_] >= d + 1:
                        d_mat[x_][y_] = d + 1
                        queue.append((d + 1, x_, y_, 1))
        if x < n - 1 and y < n - 1:
            x_, y_ = x + 1, y + 1
            if s[x_][y_] == ".":
                if direction == 2:
                    if d_mat[x_][y_] >= d:
                        d_mat[x_][y_] = d
                        queue.appendleft((d, x_, y_, 2))
                else:
                    if d_mat[x_][y_] >= d + 1:
                        d_mat[x_][y_] = d + 1
                        queue.append((d + 1, x_, y_, 2))
        if x < n - 1 and y > 0:
            x_, y_ = x + 1, y - 1
            if s[x_][y_] == ".":
                if direction == 3:
                    if d_mat[x_][y_] >= d:
                        d_mat[x_][y_] = d
                        queue.appendleft((d, x_, y_, 3))
                else:
                    if d_mat[x_][y_] >= d + 1:
                        d_mat[x_][y_] = d + 1
                        queue.append((d + 1, x_, y_, 3))

    res = d_mat[b[0] - 1][b[1] - 1]
    # print(d_mat)
    if res == 10 ** 9:
        res = -1
    return res


def main():
    n = int(input())
    a = tuple(map(int, input().split()))
    b = tuple(map(int, input().split()))
    s = [input() for _ in range(n)]
    res = solve(n, a, b, s)
    print(res)


def test():
    assert solve(5, (1, 3), (3, 5), [
        ".... #",
        "...#.",
        ".....",
        ".#...",
        "#...."
    ]) == 3
    assert solve(4, (3, 2), (4, 2), [
        "....",
        "....",
        "....",
        "....",
    ]) == -1
    assert solve(18, (18, 1), (1, 18), [
        "..................",
        ".####.............",
        ".#..#..####.......",
        ".####..#..#..####.",
        ".#..#..###...#....",
        ".#..#..#..#..#....",
        ".......####..#....",
        ".............####.",
        "..................",
        "..................",
        ".####.............",
        "....#..#..#.......",
        ".####..#..#..####.",
        ".#.....####..#....",
        ".####.....#..####.",
        "..........#..#..#.",
        ".............####.",
        "..................",
    ]) == 9


if __name__ == "__main__":
    test()
    main()
