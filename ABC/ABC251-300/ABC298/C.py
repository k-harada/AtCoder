def solve(n, q, query_list):
    list_2 = [[] for _ in range(n + 1)]
    list_3 = [[] for _ in range(200001)]
    res = []
    for query in query_list:
        if query[0] == 1:
            i, j = query[1], query[2]
            list_2[j].append(i)
            list_3[i].append(j)
        elif query[0] == 2:
            list_2[query[1]] = list(sorted(list_2[query[1]]))
            res.append(" ".join([str(a) for a in list_2[query[1]]]))
        elif query[0] == 3:
            list_3[query[1]] = list(sorted(list(set(list_3[query[1]]))))
            res.append(" ".join([str(a) for a in list_3[query[1]]]))
        else:
            raise
    # print(res)
    return res


def main():
    n = int(input())
    q = int(input())
    query_list = [tuple(map(int, input().split())) for _ in range(q)]
    res = solve(n, q, query_list)
    for r in res:
        print(r)


def test():
    assert solve(5, 8, [(1, 1, 1), (1, 2, 4), (1, 1, 4), (2, 4), (1, 1, 4), (2, 4), (3, 1), (3, 2)]) == [
        "1 2", "1 1 2", "1 4", "4"
    ]
    assert solve(1, 5, [(1, 1, 1), (1, 2, 1), (1, 200000, 1), (2, 1), (3, 200000)]) == ["1 2 200000", "1"]


if __name__ == "__main__":
    test()
    main()
