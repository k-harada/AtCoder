from collections import deque


def solve(n, m, uv_list):
    g = [[] for _ in range(n + 1)]
    res_needs = 0
    for u, v in uv_list:
        g[u].append(v)

    for i in range(1, n + 1):
        visited = [0] * (n + 1)
        queue = deque([i])
        visited[i] = 1
        while len(queue):
            p = queue.pop()
            for q in g[p]:
                if visited[q]:
                    continue
                visited[q] = 1
                queue.append(q)
        res_needs += sum(visited) - 1
    return res_needs - m


def main():
    n, m = map(int, input().split())
    uv_list = [tuple(map(int, input().split())) for _ in range(m)]
    res = solve(n, m, uv_list)
    print(res)


def test():
    assert solve(4, 3, [(2, 4), (3, 1), (4, 3)]) == 3
    assert solve(292, 0, []) == 0
    assert solve(5, 8, [(1, 2), (2, 1), (1, 3), (3, 1), (1, 4), (4, 1), (1, 5), (5, 1)]) == 12


def test_large():
    print(solve(2000, 2000, [(i, i + 1) for i in range(1, 2000)] + [(2000, 1)]))


if __name__ == "__main__":
    test()
    # test_large()
    main()
