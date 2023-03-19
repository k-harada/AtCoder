def solve(l, n1, n2, vl_list):
    event_list = []
    t = 0
    event_list.append((0, vl_list[0][0], 1))
    for i in range(n1 - 1):
        v, le = vl_list[i]
        t += le
        v, le = vl_list[i + 1]
        event_list.append((t, v, 1))
    event_list.append((l, -1, 1))
    t = 0
    event_list.append((0, vl_list[n1][0], 2))
    for i in range(n1, n1 + n2 - 1):
        v, le = vl_list[i]
        t += le
        v, le = vl_list[i + 1]
        event_list.append((t, v, 2))
    event_list.append((l, -2, 2))

    event_list = list(sorted(event_list, key=lambda x: (x[0], x[2], x[1])))
    # print(event_list)

    t_now = 0
    a = -1
    b = -2
    res = 0
    for t, v, x in event_list:
        # print(t_now, t, a, b)
        if a == b:
            res += t - t_now
        t_now = t
        if x == 1:
            a = v
        else:
            b = v
    # print(res)
    return res


def main():
    l, n1, n2 = map(int, input().split())
    vl_list = [tuple(map(int, input().split())) for _ in range(n1 + n2)]
    res = solve(l, n1, n2, vl_list)
    print(res)


def test():
    assert solve(8, 4, 3, [(1, 2), (3, 2), (2, 3), (3, 1), (1, 4), (2, 1), (3, 3)]) == 4
    assert solve(10000000000, 1, 1, [(1, 10000000000), (1, 10000000000)]) == 10000000000
    assert solve(1000, 4, 7, [
        (19, 79), (33, 463), (19, 178), (33, 280),
        (19, 255), (33, 92), (34, 25), (19, 96), (12, 11), (19, 490), (33, 31)
    ]) == 380


if __name__ == "__main__":
    test()
    main()
