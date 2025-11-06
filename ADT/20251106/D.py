def solve(q, query_list):
    a_list = []
    res = []
    for query in query_list:
        if query[0] == 1:
            a_list.append(query[1])
        else:
            res.append(a_list[-query[1]])

    return res


def main():
    q = int(input())
    query_list = [tuple(map(int, input().split())) for _ in range(q)]
    res = solve(q, query_list)
    for r in res:
        print(r)


def test():
    assert solve(5, [(1, 20), (1, 30), (2, 1), (1, 40), (2, 3)]) == [30, 20]


if __name__ == "__main__":
    test()
    main()
