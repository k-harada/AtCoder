def solve(n, m, q, uv_list, c_list, query_list):
    res_list = []
    color_list = [0] + c_list
    g = [[] for _ in range(n + 1)]
    for u, v in uv_list:
        g[u].append(v)
        g[v].append(u)

    for query in query_list:
        if query[0] == 1:
            p = query[1]
            for q in g[p]:
                color_list[q] = color_list[p]
            res_list.append(color_list[p])
        else:
            p, c = query[1], query[2]
            res_list.append(color_list[p])
            color_list[p] = c
    # print(res_list)
    return res_list


def main():
    n, m, q = map(int, input().split())
    uv_list = [list(map(int, input().split())) for _ in range(m)]
    c_list = list(map(int, input().split()))
    query_list = [list(map(int, input().split())) for _ in range(q)]
    res = solve(n, m, q, uv_list, c_list, query_list)
    for r in res:
        print(r)


def test():
    assert solve(3, 2, 3, [[1, 2], [2, 3]], [5, 10, 15], [[1, 2], [2, 1, 20], [1, 1]]) == [10, 10, 20]


if __name__ == "__main__":
    test()
    main()
