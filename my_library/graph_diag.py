from collections import deque


def solve(n, ab_list):
    g = [[] for _ in range(n + 1)]
    for a, b in ab_list:
        g[a].append(b)
        g[b].append(a)

    # bfs
    dist_1 = [n + 1] * (n + 1)
    dist_1[1] = 0
    dist_1[0] = 0
    queue = deque([1])
    while len(queue):
        p = queue.popleft()
        for q in g[p]:
            if dist_1[q] == n + 1:
                dist_1[q] = dist_1[p] + 1
                queue.append(q)

    m = max(dist_1)
    for a in range(1, n + 1):
        if dist_1[a] == m:
            break

    # bfs
    dist_a = [n + 1] * (n + 1)
    dist_a[a] = 0
    dist_a[0] = 0
    queue = deque([a])
    while len(queue):
        p = queue.popleft()
        for q in g[p]:
            if dist_a[q] == n + 1:
                dist_a[q] = dist_a[p] + 1
                queue.append(q)
    return max(dist_a) + 1


def main():
    n = int(input())
    ab_list = [tuple(map(int, input().split())) for _ in range(n - 1)]
    res = solve(n, ab_list)
    print(res)


def test():
    assert solve(3, [(1, 2), (2, 3)]) == 3
    assert solve(5, [(1, 2), (2, 3), (3, 4), (3, 5)]) == 4


if __name__ == "__main__":
    test()
    main()
