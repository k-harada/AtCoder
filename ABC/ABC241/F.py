from bisect import bisect_left, bisect_right
from collections import deque


def solve(h, w, n, sx, sy, gx, gy, xy_list):

    # 可能性のある点を全列挙
    p_dict = dict()
    p_dict[(sx - 1) * w + (sy - 1)] = []
    for x, y in xy_list:
        x -= 1
        y -= 1
        if x > 0:
            p_dict[(x - 1) * w + y] = []
        if x < h - 1:
            p_dict[(x + 1) * w + y] = []
        if y > 0:
            p_dict[x * w + y - 1] = []
        if y < w - 1:
            p_dict[x * w + y + 1] = []

    # edgeをひく
    # 上から下と下から上
    px_dict = dict()
    for x, y in xy_list:
        x -= 1
        y -= 1
        if y not in px_dict.keys():
            px_dict[y] = [x]
        else:
            px_dict[y].append(x)
    for y in px_dict.keys():
        px_dict[y] = list(sorted(px_dict[y]))

    # 左から右と右から左
    py_dict = dict()
    for x, y in xy_list:
        x -= 1
        y -= 1
        if x not in py_dict.keys():
            py_dict[x] = [y]
        else:
            py_dict[x].append(y)
    for x in py_dict.keys():
        py_dict[x] = list(sorted(py_dict[x]))

    for p in p_dict.keys():
        px, py = p // w, p % w

        if py in px_dict.keys():
            # 上から下
            idx = bisect_left(px_dict[py], px)
            if idx == len(px_dict[py]):
                pass
            elif px_dict[py][idx] - 1 == px:
                pass
            else:
                q = (px_dict[py][idx] - 1) * w + py
                p_dict[p].append(q)

            # 下から上
            idx = bisect_right(px_dict[py], px)
            if idx == 0:
                pass
            elif px_dict[py][idx - 1] + 1 == px:
                pass
            else:
                q = (px_dict[py][idx - 1] + 1) * w + py
                p_dict[p].append(q)

        if px in py_dict.keys():
            # 左から右
            idx = bisect_left(py_dict[px], py)
            if idx == len(py_dict[px]):
                pass
            elif py_dict[px][idx] - 1 == py:
                pass
            else:
                q = px * w + (py_dict[px][idx] - 1)
                p_dict[p].append(q)

            # 右から左
            idx = bisect_right(py_dict[px], py)
            if idx == 0:
                pass
            elif py_dict[px][idx - 1] + 1 == py:
                pass
            else:
                q = px * w + (py_dict[px][idx - 1] + 1)
                p_dict[p].append(q)

    # BFS
    dist = dict()
    for p in p_dict.keys():
        dist[p] = -1
    st = (sx - 1) * w + (sy - 1)
    dist[st] = 0
    goal = (gx - 1) * w + (gy - 1)
    queue = deque([st])
    while len(queue):
        p = queue.popleft()
        if p == goal:
            return dist[p]
        for q in p_dict[p]:
            if dist[q] == -1:
                dist[q] = dist[p] + 1
                queue.append(q)

    return -1


def main():
    h, w, n = map(int, input().split())
    sx, sy = map(int, input().split())
    gx, gy = map(int, input().split())
    xy_list = [tuple(map(int, input().split())) for _ in range(n)]
    res = solve(h, w, n, sx, sy, gx, gy, xy_list)
    print(res)


def test():
    assert solve(7, 8, 7, 3, 4, 5, 6, [(1, 4), (2, 1), (2, 8), (4, 5), (5, 7), (6, 2), (6, 6)]) == 4
    assert solve(4, 6, 2, 3, 2, 3, 5, [(4, 5), (2, 5)]) == -1
    assert solve(1, 10, 1, 1, 5, 1, 1, [(1, 7)]) == -1


if __name__ == "__main__":
    test()
    main()
