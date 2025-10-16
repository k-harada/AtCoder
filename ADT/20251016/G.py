from collections import deque


def solve(h, w, s_list):
    res_list = [[s_list[i][j] for j in range(w)] for i in range(h)]
    queue = deque()
    visited = [[0] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if s_list[i][j] == "E":
                queue.append((i, j))
                visited[i][j] = 1
            elif s_list[i][j] == "#":
                visited[i][j] = 1
    # BFS
    while len(queue):
        i, j = queue.popleft()
        if i > 0:
            i0, j0 = i - 1, j
            if visited[i0][j0] == 0:
                res_list[i0][j0] = "v"
                visited[i0][j0] = 1
                queue.append((i0, j0))
        if i < h - 1:
            i0, j0 = i + 1, j
            if visited[i0][j0] == 0:
                res_list[i0][j0] = "^"
                visited[i0][j0] = 1
                queue.append((i0, j0))
        if j > 0:
            i0, j0 = i, j - 1
            if visited[i0][j0] == 0:
                res_list[i0][j0] = ">"
                visited[i0][j0] = 1
                queue.append((i0, j0))
        if j < w - 1:
            i0, j0 = i, j + 1
            if visited[i0][j0] == 0:
                res_list[i0][j0] = "<"
                visited[i0][j0] = 1
                queue.append((i0, j0))
    res = ["".join(res_list[i]) for i in range(h)]
    # print(res)
    return res


def main():
    h, w = map(int, input().split())
    s_list = [list(input()) for _ in range(h)]
    res = solve(h, w, s_list)
    for r in res:
        print(r)


def test():
    assert solve(3, 4, [
        "...E",
        ".#..",
        "...."
    ]) == [
        ">>>E",
        "^#>^",
        ">>>^"
    ]
    assert solve(3, 2, ["##", "##", "##"]) == ["##", "##", "##"]


if __name__ == "__main__":
    test()
    main()
