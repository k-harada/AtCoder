from heapq import heappop, heappush


def solve(n, m, st_list):
    g = [dict() for _ in range(n + 1)]
    for s, t in st_list:
        g[s][t] = 1
    # shortest path
    h = [(0, 1)]
    visited = [0] * (n + 1)
    visited[1] = 1
    parent = [0] * (n + 1)

    while len(h):
        d, p = heappop(h)
        for q in g[p].keys():
            if not visited[q]:
                heappush(h, (d + g[p][q], q))
                parent[q] = p
                visited[q] = 1
    # print(parent)

    # reverse track
    if visited[n] == 0:
        return [-1] * m
    shortest_path = dict()
    for i in range(n + 1):
        shortest_path[i] = 0
    min_dist = 0
    q = n
    while q != 1:
        shortest_path[parent[q]] = q
        q = parent[q]
        min_dist += 1

    # print(min_dist, shortest_path)
    res = []
    for s, t in st_list:
        if shortest_path[s] == t:
            del g[s][t]
            h = [(0, 1)]
            visited = [0] * (n + 1)
            dn = 1000000
            while len(h):
                d, p = heappop(h)
                if p == n:
                    dn = d
                    break
                for q in g[p].keys():
                    if not visited[q]:
                        heappush(h, (d + g[p][q], q))
                        visited[q] = 1
            if dn >= 100000:
                res.append(-1)
            else:
                res.append(dn)
            g[s][t] = 1
        else:
            res.append(min_dist)
    # print(res)
    return res


def main():
    n, m = map(int, input().split())
    st_list = [tuple(map(int, input().split())) for _ in range(m)]
    res = solve(n, m, st_list)
    for r in res:
        print(r)


def test():
    assert solve(3, 3, [(1, 2), (1, 3), (2, 3)]) == [1, 2, 1]
    assert solve(4, 4, [(1, 2), (2, 3), (2, 4), (3, 4)]) == [-1, 2, 3, 2]
    assert solve(5, 10, [(1, 2), (1, 4), (1, 5), (2, 1), (2, 3), (3, 1), (3, 2), (3, 5), (4, 2), (4, 3)]) == [
        1, 1, 3, 1, 1, 1, 1, 1, 1, 1
    ]
    assert solve(4, 1, [(1, 2)]) == [-1]


def test_large():
    assert solve(400, 399, [(i, i + 1) for i in range(1, 400)]) == [-1] * 399


if __name__ == "__main__":
    test()
    # test_large()
    main()
