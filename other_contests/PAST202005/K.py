def solve(n, q, query_list):
    tables_top = [i for i in range(n + 1)]
    parent = [-i for i in range(n + 1)]
    for f, t, x in query_list:
        tables_top[t], tables_top[f], parent[x] = tables_top[f], parent[x], tables_top[t]

    res_list = [i for i in range(n + 1)]
    for i in range(1, n + 1):
        p = tables_top[i]
        while p > 0:
            res_list[p] = i
            p = parent[p]

    return res_list[1:]


def main():
    n, q = map(int, input().split())
    query_list = [list(map(int, input().split())) for _ in range(q)]
    res = solve(n, q, query_list)
    for r in res:
        print(r)


def test():
    assert solve(3, 4, [[1, 2, 1], [2, 3, 2], [3, 1, 3], [1, 3, 2]]) == [3, 3, 1]


if __name__ == "__main__":
    test()
    main()
