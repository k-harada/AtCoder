from collections import deque


def solve(h, w, t, a):
    o_list = []
    for i in range(h):
        for j in range(w):
            if a[i][j] == "S":
                s_i, s_j = i, j
            elif a[i][j] == "G":
                g_i, g_j = i, j
            elif a[i][j] == "o":
                o_list.append((i, j))
    o_list = [(s_i, s_j)] + o_list + [(g_i, g_j)]
    co = len(o_list)
    d_mat = [[10 ** 7] * co for _ in range(co)]
    for i in range(co):
        dist = [[-1] * w for _ in range(h)]
        queue = deque([o_list[i]])
        dist[o_list[i][0]][o_list[i][1]] = 0
        while len(queue):
            x_s, y_s = queue.popleft()
            if x_s > 0:
                x_t = x_s - 1
                y_t = y_s
                if a[x_t][y_t] != "#" and dist[x_t][y_t] == -1:
                    dist[x_t][y_t] = dist[x_s][y_s] + 1
                    queue.append((x_t, y_t))
            if y_s > 0:
                x_t = x_s
                y_t = y_s - 1
                if a[x_t][y_t] != "#" and dist[x_t][y_t] == -1:
                    dist[x_t][y_t] = dist[x_s][y_s] + 1
                    queue.append((x_t, y_t))
            if x_s < h - 1:
                x_t = x_s + 1
                y_t = y_s
                if a[x_t][y_t] != "#" and dist[x_t][y_t] == -1:
                    dist[x_t][y_t] = dist[x_s][y_s] + 1
                    queue.append((x_t, y_t))
            if y_s < w - 1:
                x_t = x_s
                y_t = y_s + 1
                if a[x_t][y_t] != "#" and dist[x_t][y_t] == -1:
                    dist[x_t][y_t] = dist[x_s][y_s] + 1
                    queue.append((x_t, y_t))
        for j in range(co):
            d = dist[o_list[j][0]][o_list[j][1]]
            if d >= 0:
                d_mat[i][j] = d
    # print(d_mat)
    # bitDP
    coo = co - 2
    dp = [[[t + 1] * (2 ** coo) for _1 in range(coo)] for _2 in range(coo + 1)]
    for i in range(coo):
        dp[1][i][2 ** i] = d_mat[0][i + 1]

    for i in range(1, coo):
        for j in range(coo):
            for k in range(2 ** coo):
                if dp[i][j][k] <= t:
                    # print(i, j, k)
                    for m in range(coo):
                        if k | 2 ** m != k + 2 ** m:
                            continue
                        dp[i + 1][m][k | 2 ** m] = min(dp[i + 1][m][k | 2 ** m], dp[i][j][k] + d_mat[j + 1][m + 1])
    # print(dp)
    res = -1
    if d_mat[0][-1] <= t:
        res = 0
    for i in range(coo + 1):
        for j in range(2 ** coo):
            for k in range(coo):
                if dp[i][k][j] + d_mat[k + 1][-1] <= t:
                    res = i
    # print(res, t)
    return res


def main():
    h, w, t = map(int, input().split())
    a = [input() for _ in range(h)]
    res = solve(h, w, t, a)
    print(res)


def test():
    assert solve(3, 3, 5, ["S.G", "o#o", ".#."]) == 1
    assert solve(3, 3, 1, ["S.G", ".#o", "o#."]) == 0-1
    assert solve(5, 10, 2000000, [
        "S.o..ooo..",
        "..o..o.o..",
        "..o..ooo..",
        "..o..o.o..",
        "..o..ooo.G"
    ]) == 18


if __name__ == "__main__":
    test()
    main()
