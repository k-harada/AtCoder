def solve(n, q, query_list):
    g = dict()
    res = []
    for t, a, b in query_list:
        if t == 1:
            if a not in g.keys():
                g[a] = {b: 1}
            else:
                g[a][b] = 1
        elif t == 2:
            if a not in g.keys():
                continue
            else:
                g[a][b] = 0
        else:
            r = "Yes"
            if a not in g.keys():
                r = "No"
            elif b not in g[a].keys():
                r = "No"
            elif g[a][b] == 0:
                r = "No"
            if b not in g.keys():
                r = "No"
            elif a not in g[b].keys():
                r = "No"
            elif g[b][a] == 0:
                r = "No"
            res.append(r)

    return res


def main():
    n, q = map(int, input().split())
    query_list = [tuple(map(int, input().split())) for _ in range(q)]
    res = solve(n, q, query_list)
    for r in res:
        print(r)


def test():
    assert solve(3, 9, [
        (1, 1, 2), (3, 1, 2), (1, 2, 1),
        (3, 1, 2), (1, 2, 3), (1, 3, 2),
        (3, 1, 3), (2, 1, 2), (3, 1, 2),
    ]) == ["No", "Yes", "No", "No"]
    assert solve(2, 8, [
        (1, 1, 2), (1, 2, 1), (3, 1, 2), (1, 1, 2),
        (1, 1, 2), (1, 1, 2), (2, 1, 2), (3, 1, 2),
    ]) == ["Yes", "No"]


if __name__ == "__main__":
    test()
    main()
