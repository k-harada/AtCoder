from collections import deque


def solve(n, q, ab_list, cd_list):
    g = [[] for _ in range(n + 1)]
    for a, b in ab_list:
        g[a].append(b)
        g[b].append(a)

    color = [-1] * (n + 1)
    color[1] = 1
    queue = deque([1])
    while len(queue):
        p = queue.popleft()
        for q in g[p]:
            if color[q] == -1:
                color[q] = 1 - color[p]
                queue.append(q)
    res = []
    for c, d in cd_list:
        if color[c] == color[d]:
            res.append("Town")
        else:
            res.append("Road")
    return res


def main():
    n, q = map(int, input().split())
    ab_list = [tuple(map(int, input().split())) for _ in range(n - 1)]
    cd_list = [tuple(map(int, input().split())) for _ in range(q)]
    res = solve(n, q, ab_list, cd_list)
    for r in res:
        print(r)


def test():
    assert solve(4, 1, [(1, 2), (2, 3), (2, 4)], [(1, 2)]) == ["Road"]
    assert solve(5, 2, [(1, 2), (2, 3), (3, 4), (4, 5)], [(1, 3), (1, 5)]) == ["Town", "Town"]


if __name__ == "__main__":
    test()
    main()
