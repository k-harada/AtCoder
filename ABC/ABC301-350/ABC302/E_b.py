def solve(n, q, query_list):
    g = [dict() for _ in range(n)]
    counter = [0] * n
    r = n
    res = []
    for query in query_list:
        if query[0] == 1:
            p, q = query[1] - 1, query[2] - 1
            if counter[p] == 0:
                r -= 1
            counter[p] += 1
            if counter[q] == 0:
                r -= 1
            counter[q] += 1
            g[p][q] = 1
            g[q][p] = 1
        else:
            p = query[1] - 1
            if counter[p] > 0:
                r += 1
            counter[p] = 0
            for q in g[p].keys():
                _ = g[q].pop(p)
                counter[q] -= 1
                if counter[q] == 0:
                    r += 1
            g[p] = dict()
        res.append(r)
    return res


def main():
    n, q = map(int, input().split())
    query_list = [tuple(map(int, input().split())) for _ in range(q)]
    res = solve(n, q, query_list)
    for r in res:
        print(r)


def test():
    assert solve(3, 7, [
        (1, 1, 2), (1, 1, 3), (1, 2, 3), (2, 1),
        (1, 1, 2), (2, 2), (1, 1, 2)
    ]) == [1, 0, 0, 1, 0, 3, 1]
    assert solve(2, 1, [(2, 1)]) == [2]


if __name__ == "__main__":
    test()
    main()
