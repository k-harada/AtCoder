from collections import deque


def solve(h, w, s_list):

    g = dict()
    for i in range(h):
        for j in range(w):
            if s_list[i][j] == ".":
                g[i * 100 + j] = dict()

    for i in range(h):
        for j in range(w - 1):
            if s_list[i][j] == "." and s_list[i][j + 1] == ".":
                g[i * 100 + j][i * 100 + j + 1] = 1
                g[i * 100 + j + 1][i * 100 + j] = 1

    for i in range(h - 1):
        for j in range(w):
            if s_list[i][j] == "." and s_list[i + 1][j] == ".":
                g[i * 100 + j][i * 100 + j + 100] = 1
                g[i * 100 + j + 100][i * 100 + j] = 1

    d_max = 0
    for x in g.keys():
        d_dict = {v: 10000 for v in g.keys()}
        queue = deque([x])
        d_dict[x] = 0
        while len(queue) > 0:
            p = queue.popleft()
            for q in g[p].keys():
                if d_dict[q] > d_dict[p] + 1:
                    d_dict[q] = d_dict[p] + 1
                    queue.append(q)
        d_max = max(d_max, max(d_dict.values()))

    return d_max


def main():
    h, w = map(int, input().split())
    s_list = []
    for _ in range(h):
        s = input()
        s_list.append(s)
    res = solve(h, w, s_list)
    print(res)


def test():
    assert solve(3, 3, ["...", "...", "..."]) == 4
    assert solve(3, 5, ["...#.", ".#.#.", ".#..."]) == 10


if __name__ == "__main__":
    test()
    main()
