from collections import deque


def solve(n, abc_list):
    g = [[] for _ in range(n)]
    edge_sum = 0
    for a, b, c in abc_list:
        g[a - 1].append((b - 1, c))
        g[b - 1].append((a - 1, c))
        edge_sum += c
    # 直径を求める
    dist_0 = [10 ** 18] * n
    dist_0[0] = 0
    queue = deque([0])
    while len(queue):
        p = queue.popleft()
        for q, d in g[p]:
            if dist_0[q] == 10 ** 18:
                dist_0[q] = dist_0[p] + d
                queue.append(q)
    # print(dist_0)
    m = max(dist_0)
    for i in range(n):
        if dist_0[i] == m:
            r = i
    dist_1 = [10 ** 18] * n
    dist_1[r] = 0
    queue = deque([r])
    while len(queue):
        p = queue.popleft()
        for q, d in g[p]:
            if dist_1[q] == 10 ** 18:
                dist_1[q] = dist_1[p] + d
                queue.append(q)
    # print(max(dist_1))
    return 2 * edge_sum - max(dist_1)


def main():
    n = int(input())
    abc_list = [tuple(map(int, input().split())) for _ in range(n - 1)]
    res = solve(n, abc_list)
    print(res)


def test():
    assert solve(4, [(1, 2, 2), (1, 3, 3), (1, 4, 4)]) == 11
    assert solve(10, [
        (10, 9, 1000000000),
        (9, 8, 1000000000),
        (8, 7, 1000000000),
        (7, 6, 1000000000),
        (6, 5, 1000000000),
        (5, 4, 1000000000),
        (4, 3, 1000000000),
        (3, 2, 1000000000),
        (2, 1, 1000000000),
    ]) == 9000000000


if __name__ == "__main__":
    test()
    main()
