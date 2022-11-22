from collections import deque


def solve(n, ab_list):
    g = dict()
    visited = dict()
    for a, b in ab_list:
        if a not in g.keys():
            g[a] = dict()
        g[a][b] = 1
        if b not in g.keys():
            g[b] = dict()
        g[b][a] = 1
        visited[a] = 0
        visited[b] = 0

    queue = deque()
    if 1 in g.keys():
        queue.append(1)
    visited[1] = 1
    res = 1

    while len(queue):
        p = queue.popleft()
        for q in g[p].keys():
            if visited[q] == 0:
                visited[q] = 1
                res = max(res, q)
                queue.append(q)
    return res


def main():
    n = int(input())
    ab_list = [tuple(map(int, input().split())) for _ in range(n)]
    res = solve(n, ab_list)
    print(res)


def test():
    assert solve(4, [(1, 4), (4, 3), (4, 10), (8, 3)]) == 10
    assert solve(6, [(1, 3), (1, 5), (1, 12), (3, 5), (3, 12), (5, 12)]) == 12
    assert solve(3, [(5, 6), (6, 7), (7, 8)]) == 1


def test_large():
    assert solve(200000, [(i, i + 1) for i in range(1, 200001)]) == 200001


if __name__ == "__main__":
    # test()
    # test_large()
    main()
