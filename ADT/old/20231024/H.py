from collections import defaultdict


def solve(n, q, query_list):
    count_list = [0] * (n + 1)
    r = n
    edge_list = [[] for _ in range(n + 1)]
    res = []
    for query in query_list:
        if query[0] == 1:
            p, q = query[1], query[2]
            if count_list[p] == 0:
                r -= 1
            count_list[p] += 1
            if count_list[q] == 0:
                r -= 1
            count_list[q] += 1
            edge_list[p].append(q)
            edge_list[q].append(p)
        else:
            p = query[1]
            if count_list[p] > 0:
                r += 1
            count_list[p] = 0
            seen = defaultdict(int)
            while len(edge_list[p]):
                q = edge_list[p].pop()
                if seen[abs(q)] == 0:
                    seen[abs(q)] = 1
                    if q > 0:
                        if count_list[q] == 1:
                            r += 1
                        count_list[q] -= 1
                        edge_list[q].append(-p)
                    else:
                        continue
                else:
                    continue
        # print(count_list)
        res.append(r)
    # print(res)
    return res


def main():
    n, q = map(int, input().split())
    query_list = [tuple(map(int, input().split())) for _ in range(q)]
    res = solve(n, q, query_list)
    for r in res:
        print(r)


def test():
    assert solve(3, 7, [
        (1, 1, 2), (1, 1, 3), (1, 2, 3), (2, 1), (1, 1, 2), (2, 2), (1, 1, 2)
    ]) == [1, 0, 0, 1, 0, 3, 1]
    assert solve(2, 1, [(2, 1)]) == [2]


if __name__ == "__main__":
    test()
    main()
