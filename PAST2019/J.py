from collections import deque
LARGE = 1000000000


def solve(h, w, a_array):

    d0_array = [[LARGE] * w for _ in range(h)]
    d1_array = [[LARGE] * w for _ in range(h)]
    d2_array = [[LARGE] * w for _ in range(h)]

    # d0
    d0_array[h - 1][0] = 0
    queue = deque([[h - 1, 0]])
    while len(queue) > 0:
        py, px = queue.popleft()
        if px > 0:
            qx = px - 1
            qy = py
            new_v = d0_array[py][px] + a_array[qy][qx]
            if d0_array[qy][qx] > new_v:
                d0_array[qy][qx] = new_v
                queue.append([qy, qx])
        if px < w - 1:
            qx = px + 1
            qy = py
            new_v = d0_array[py][px] + a_array[qy][qx]
            if d0_array[qy][qx] > new_v:
                d0_array[qy][qx] = new_v
                queue.append([qy, qx])
        if py > 0:
            qx = px
            qy = py - 1
            new_v = d0_array[py][px] + a_array[qy][qx]
            if d0_array[qy][qx] > new_v:
                d0_array[qy][qx] = new_v
                queue.append([qy, qx])
        if py < h - 1:
            qx = px
            qy = py + 1
            new_v = d0_array[py][px] + a_array[qy][qx]
            if d0_array[qy][qx] > new_v:
                d0_array[qy][qx] = new_v
                queue.append([qy, qx])

    # d1
    d1_array[h - 1][w - 1] = 0
    queue = deque([[h - 1, w - 1]])
    while len(queue) > 0:
        py, px = queue.popleft()
        if px > 0:
            qx = px - 1
            qy = py
            new_v = d1_array[py][px] + a_array[qy][qx]
            if d1_array[qy][qx] > new_v:
                d1_array[qy][qx] = new_v
                queue.append([qy, qx])
        if px < w - 1:
            qx = px + 1
            qy = py
            new_v = d1_array[py][px] + a_array[qy][qx]
            if d1_array[qy][qx] > new_v:
                d1_array[qy][qx] = new_v
                queue.append([qy, qx])
        if py > 0:
            qx = px
            qy = py - 1
            new_v = d1_array[py][px] + a_array[qy][qx]
            if d1_array[qy][qx] > new_v:
                d1_array[qy][qx] = new_v
                queue.append([qy, qx])
        if py < h - 1:
            qx = px
            qy = py + 1
            new_v = d1_array[py][px] + a_array[qy][qx]
            if d1_array[qy][qx] > new_v:
                d1_array[qy][qx] = new_v
                queue.append([qy, qx])

    # d2
    d2_array[0][w - 1] = 0
    queue = deque([[0, w - 1]])
    while len(queue) > 0:
        py, px = queue.popleft()
        if px > 0:
            qx = px - 1
            qy = py
            new_v = d2_array[py][px] + a_array[qy][qx]
            if d2_array[qy][qx] > new_v:
                d2_array[qy][qx] = new_v
                queue.append([qy, qx])
        if px < w - 1:
            qx = px + 1
            qy = py
            new_v = d2_array[py][px] + a_array[qy][qx]
            if d2_array[qy][qx] > new_v:
                d2_array[qy][qx] = new_v
                queue.append([qy, qx])
        if py > 0:
            qx = px
            qy = py - 1
            new_v = d2_array[py][px] + a_array[qy][qx]
            if d2_array[qy][qx] > new_v:
                d2_array[qy][qx] = new_v
                queue.append([qy, qx])
        if py < h - 1:
            qx = px
            qy = py + 1
            new_v = d2_array[py][px] + a_array[qy][qx]
            if d2_array[qy][qx] > new_v:
                d2_array[qy][qx] = new_v
                queue.append([qy, qx])

    res = LARGE
    for i in range(h):
        for j in range(w):
            res = min(res, d0_array[i][j] + d1_array[i][j] + d2_array[i][j] - 2 * a_array[i][j])

    return res


def main():
    h, w = map(int, input().split())
    a_array = []
    for _ in range(h):
        a_array.append(list(map(int, input().split())))
    res = solve(h, w, a_array)
    print(res)


def test():
    assert solve(5, 6, [
        [9, 9, 9, 9, 1, 0],
        [9, 9, 9, 9, 1, 9],
        [9, 9, 9, 1, 1, 1],
        [9, 1, 1, 1, 9, 1],
        [0, 1, 9, 9, 9, 0]
    ]) == 10


if __name__ == "__main__":
    test()
    main()
