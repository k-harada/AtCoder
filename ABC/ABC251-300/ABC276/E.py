from collections import deque


def solve(h, w, c):
    g = [[] for _ in range(h * w)]
    # 左右隣接
    for i in range(h):
        for j in range(w - 1):
            if c[i][j] == c[i][j + 1] == ".":
                p = i * w + j
                q = p + 1
                g[p].append(q)
                g[q].append(p)
    # 上下隣接
    for i in range(h - 1):
        for j in range(w):
            if c[i][j] == c[i + 1][j] == ".":
                p = i * w + j
                q = p + w
                g[p].append(q)
                g[q].append(p)

    for i in range(h):
        for j in range(w):
            if c[i][j] == "S":
                i_s = i
                j_s = j
    st_list = []
    if i_s > 0:
        if c[i_s - 1][j_s] == ".":
            st_list.append((i_s - 1) * w + j_s)
    if j_s > 0:
        if c[i_s][j_s - 1] == ".":
            st_list.append(i_s * w + j_s - 1)
    if i_s < h - 1:
        if c[i_s + 1][j_s] == ".":
            st_list.append((i_s + 1) * w + j_s)
    if j_s < w - 1:
        if c[i_s][j_s + 1] == ".":
            st_list.append(i_s * w + j_s + 1)

    # print(st_list)

    visited = [0] * (h * w)
    while len(st_list) > 1:
        s = st_list.pop()
        visited[s] = 1
        queue = deque([s])

        while len(queue):
            p = queue.popleft()
            for q in g[p]:
                if visited[q] == 0:
                    visited[q] = 1
                    queue.append(q)

        for t in st_list:
            if visited[t] == 1:
                return "Yes"

    return "No"


def main():
    h, w = map(int, input().split())
    c = [input() for _ in range(h)]
    res = solve(h, w, c)
    print(res)


def test():
    assert solve(4, 4, ["....", "#.#.", ".S..", ".##."]) == "Yes"
    assert solve(2, 2, ["S.", ".#"]) == "No"
    assert solve(5, 7, [".#...#.", "..#.#..", "...S...", "..#.#..", ".#...#."]) == "No"


if __name__ == "__main__":
    test()
    main()
