def solve(n, m, q, wv_list, x_list, query_list):
    res_list = []
    x_list_sorted = list(sorted(x_list))
    wv_list_sorted = list(sorted(wv_list, key=lambda wv: -wv[1]))
    x_list_args_ = list(sorted([(i, x_list[i]) for i in range(m)], key=lambda ix: ix[1]))
    x_list_args = [0] * m
    for i in range(m):
        x_list_args[x_list_args_[i][0]] = i

    for l, r in query_list:
        occupied = [False] * m
        for j in range(l - 1, r):
            occupied[x_list_args[j]] = True
        # print(occupied)
        res = 0
        for w, v in wv_list_sorted:
            for i in range(m):
                if w <= x_list_sorted[i] and not occupied[i]:
                    occupied[i] = True
                    res += v
                    break
        res_list.append(res)
    # print(res_list)
    return res_list


def main():
    n, m, q = map(int, input().split())
    wv_list = [tuple(map(int, input().split())) for _ in range(n)]
    x_list = list(map(int, input().split()))
    query_list = [tuple(map(int, input().split())) for _ in range(q)]
    res_list = solve(n, m, q, wv_list, x_list, query_list)
    for res in res_list:
        print(res)


def test():
    assert solve(3, 4, 3, [(1, 9), (5, 3), (7, 8)], [1, 8, 6, 9], [(4, 4), (1, 4), (1, 3)]) == [20, 0, 9]


if __name__ == "__main__":
    test()
    main()
