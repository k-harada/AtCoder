import sortedcontainers


def solve(h, w, q, rc_list):
    status = [[1] * w for _ in range(h)]
    map_lr = [sortedcontainers.SortedList(list(range(y * w, (y + 1) * w))) for y in range(h)]
    map_ud = [sortedcontainers.SortedList(list(range(x, x + w * h, w))) for x in range(w)]
    for r, c in rc_list:

        x = (r - 1) * w + (c - 1)
        # 壁がある
        if status[r - 1][c - 1] == 1:
            status[r - 1][c - 1] = 0
            map_lr[r - 1].discard(x)
            map_ud[c - 1].discard(x)
        else:
            # delete left
            pos_lr = map_lr[r - 1].bisect_left(x)
            if pos_lr > 0:
                del_left = map_lr[r - 1][pos_lr - 1]
                status[del_left // w][del_left % w] = 0
                map_lr[del_left // w].discard(del_left)
                map_ud[del_left % w].discard(del_left)
            # delete right
            pos_lr = map_lr[r - 1].bisect_left(x)
            if len(map_lr[r - 1]) > pos_lr:
                del_right = map_lr[r - 1][pos_lr]
                status[del_right // w][del_right % w] = 0
                map_lr[del_right // w].discard(del_right)
                map_ud[del_right % w].discard(del_right)

            # delete up
            pos_ud = map_ud[c - 1].bisect_left(x)
            if pos_ud > 0:
                del_up = map_ud[c - 1][pos_ud - 1]
                status[del_up // w][del_up % w] = 0
                map_lr[del_up // w].discard(del_up)
                map_ud[del_up % w].discard(del_up)
            # delete right
            pos_ud = map_ud[c - 1].bisect_left(x)
            if len(map_ud[c - 1]) > pos_ud:
                del_down = map_ud[c - 1][pos_ud]
                status[del_down // w][del_down % w] = 0
                map_lr[del_down // w].discard(del_down)
                map_ud[del_down % w].discard(del_down)

        # print(status)

    res = sum([sum(status[r]) for r in range(h)])
    return res


def main():
    h, w, q = map(int, input().split())
    rc_list = [tuple(map(int, input().split())) for _ in range(q)]
    res = solve(h, w, q, rc_list)
    print(res)


def test():
    assert solve(2, 4, 3, [(1, 2), (1, 2), (1, 3)]) == 2
    assert solve(5, 5, 5, [(3, 3), (3, 3), (3, 2), (2, 2), (1, 2)]) == 10
    assert solve(4, 3, 10, [
        (2, 2), (4, 1), (1, 1), (4, 2), (2, 1),
        (3, 1), (1, 3), (1, 2), (4, 3), (4, 2),
    ]) == 2


if __name__ == "__main__":
    test()
    main()
