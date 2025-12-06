from collections import deque


def solve(n, m, xy_list, q, query_list):
    g = [[] for _ in range(n + 1)]
    for x, y in xy_list:
        g[y].append(x)
    res = []
    status = ["No"] * (n + 1)

    for query in query_list:
        if query[0] == 1:
            v = query[1]
            if status[v] == "Yes":
                continue
            status[v] = "Yes"
            queue = deque([v])
            while queue:
                u = queue.pop()
                for v in g[u]:
                    if status[v] == "Yes":
                        continue
                    status[v] = "Yes"
                    queue.append(v)
            # print(status)
        else:
            v = query[1]
            res.append(status[v])
    # print(res)
    return res


def main():
    n, m = map(int, input().split())
    xy_list = [tuple(map(int, input().split())) for _ in range(m)]
    q = int(input())
    query_list = [tuple(map(int, input().split())) for _ in range(q)]
    res = solve(n, m, xy_list, q, query_list)
    for r in res:
        print(r)


def test():
    assert solve(5, 6, [
        (1, 2), (2, 3), (3, 1), (4, 5), (1, 4), (2, 5)
    ], 5, [
        (1, 3), (2, 1), (2, 4), (1, 5), (2, 4)
    ]) == ["Yes", "No", "Yes"]


if __name__ == "__main__":
    test()
    main()
