from bisect import bisect_left


def solve(n, m, q, train_list, query_list):
    train_list_s = list(sorted(train_list, key=lambda x: x[2]))
    next_edge = [[0] * (m + 1) for _ in range(18)]
    next_edge[0][m] = m
    edge_dict = dict()
    time_list = [[] for _ in range(n + 1)]
    for i in range(m):
        a, b, s, t = train_list_s[i]
        edge_dict[s] = (a, b, s, t, i)
        time_list[a].append(s)
    time_len_list = [len(time_list[i]) for i in range(n + 1)]
    for i in range(m):
        a, b, s, t = train_list_s[i]
        s_i = bisect_left(time_list[b], t)
        if s_i == time_len_list[b]:
            next_edge[0][i] = m
        else:
            s = time_list[b][s_i]
            next_edge[0][i] = edge_dict[s][4]
    for t in range(17):
        for p in range(m + 1):
            next_edge[t + 1][p] = next_edge[t][next_edge[t][p]]

    def get_bus_time(u, k):
        u_ = u
        k_ = k
        jump = 0
        while k_ > 0:
            if k_ % 2 == 1:
                u_ = next_edge[jump][u_]
            jump += 1
            k_ >>= 1
        if u_ == m:
            return 10 ** 9 + 7
        else:
            return train_list_s[u_][2]

    res = []
    for x, y, z in query_list:
        s_i = bisect_left(time_list[y], x)
        if s_i == time_len_list[y]:
            res.append(str(y))
            continue
        s = time_list[y][s_i]
        if s >= z:
            res.append(str(y))
            continue
        v = edge_dict[s][4]
        left = 0
        right = m
        while left < right - 1:
            middle = (left + right) // 2
            t = get_bus_time(v, middle)
            if t < z:
                left = middle
            else:
                right = middle
        edge_time = get_bus_time(v, left)
        bus_id = edge_dict[edge_time][4]
        a_, b_, s_, t_ = train_list_s[bus_id]
        if t_ < z:
            res.append(str(b_))
        else:
            res.append(str(a_) + " " + str(b_))

    # print(next_edge[0])
    # print(res)
    return res


def main():
    n, m, q = map(int, input().split())
    train_list = [tuple(map(int, input().split())) for _ in range(m)]
    query_list = [tuple(map(int, input().split())) for _ in range(q)]
    res = solve(n, m, q, train_list, query_list)
    for r in res:
        print(r)


def test():
    assert solve(3, 2, 3, [(1, 2, 1, 3), (2, 3, 3, 5)], [(1, 1, 5), (2, 2, 3), (1, 3, 2)]) == ["2 3", "2", "3"]
    assert solve(8, 10, 10, [
        (4, 3, 329982133, 872113932),
        (6, 8, 101082040, 756263297),
        (4, 7, 515073851, 793074419),
        (8, 7, 899017043, 941751547),
        (5, 7, 295510441, 597348810),
        (7, 2, 688716395, 890599546),
        (6, 1, 414221915, 748470452),
        (6, 4, 810915860, 904512496),
        (3, 1, 497469654, 973509612),
        (4, 1, 307142272, 8721781570)
    ], [
        (374358788, 4, 509276232),
        (243448834, 6, 585993193),
        (156350864, 4, 682491610),
        (131643541, 8, 836902943),
        (152874385, 6, 495945159),
        (382276121, 1, 481368090),
        (552433623, 2, 884584430),
        (580376205, 2, 639442239),
        (108790644, 7, 879874292),
        (883275610, 1, 994982498)
    ]) == ["4", "6 1", "4 1", "8", "6 1", "1", "2", "2", "7 2", "1"]


if __name__ == "__main__":
    test()
    main()
