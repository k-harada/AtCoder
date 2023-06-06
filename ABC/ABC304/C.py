from collections import deque


def solve(n, d, xy_list):
    g = [[] for _ in range(n)]
    for i in range(n - 1):
        x_i, y_i = xy_list[i]
        for j in range(i + 1, n):
            x_j, y_j = xy_list[j]
            if (x_j - x_i) ** 2 + (y_j - y_i) ** 2 <= d ** 2:
                g[i].append(j)
                g[j].append(i)

    visited = [0] * n
    queue = deque([0])
    while len(queue):
        p = queue.popleft()
        if visited[p]:
            continue
        visited[p] = 1
        for q in g[p]:
            if visited[q] == 0:
                queue.append(q)
    res = []
    for i in range(n):
        if visited[i] == 1:
            res.append("Yes")
        else:
            res.append("No")
    return res


def main():
    n, d = map(int, input().split())
    xy_list = [tuple(map(int, input().split())) for _ in range(n)]
    res = solve(n, d, xy_list)
    for r in res:
        print(r)


def test():
    assert solve(4, 5, [(2, -1), (3, 1), (8, 8), (0, 5)]) == ["Yes", "Yes", "No", "Yes"]
    assert solve(3, 1, [(0, 0), (-1000, -1000), (1000, 1000)]) == ["Yes", "No", "No"]


if __name__ == "__main__":
    test()
    main()
