def solve(n, q, query_list):
    res = []
    before_list = [0] * (n + 1)
    next_list = [0] * (n + 1)
    for query in query_list:
        if query[0] == 1:
            x, y = query[1], query[2]
            before_list[y] = x
            next_list[x] = y
        elif query[0] == 2:
            x, y = query[1], query[2]
            before_list[y] = 0
            next_list[x] = 0
        else:
            x = query[1]
            r_next = []
            y = x
            while y != 0:
                r_next.append(y)
                y = next_list[y]
            r_before = []
            y = x
            while y != 0:
                r_before.append(y)
                y = before_list[y]
            # print(r_before)
            # print(r_next)
            r = list(reversed(r_before)) + r_next[1:]
            # print(r)
            res.append(str(len(r)) + " " + " ".join([str(a) for a in r]))
    return res


def main():
    n, q = map(int, input().split())
    query_list = [tuple(map(int, input().split())) for _ in range(q)]
    res = solve(n, q, query_list)
    for r in res:
        print(r)


def test():
    assert solve(7, 14, [
        (1, 6, 3),
        (1, 4, 1),
        (1, 5, 2),
        (1, 2, 7),
        (1, 3, 5),
        (3, 2),
        (3, 4),
        (3, 6),
        (2, 3, 5),
        (2, 4, 1),
        (1, 1, 5),
        (3, 2),
        (3, 4),
        (3, 6),
    ]) == [
        "5 6 3 5 2 7",
        "2 4 1",
        "5 6 3 5 2 7",
        "4 1 5 2 7",
        "1 4",
        "2 6 3"
    ]


if __name__ == "__main__":
    test()
    main()
