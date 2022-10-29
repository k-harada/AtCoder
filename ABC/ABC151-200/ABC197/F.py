from collections import deque


def solve(n, m, abc_list):

    edges_dict = dict()
    single_edges = dict()
    for a, b, c in abc_list:
        if c in edges_dict.keys():
            edges_dict[c].append((int(a), int(b)))
        else:
            edges_dict[c] = [(int(a), int(b))]
        if int(a) * (n + 1) + int(b) not in single_edges.keys():
            single_edges[int(a) * (n + 1) + int(b)] = 1
            single_edges[int(b) * (n + 1) + int(a)] = 1

    double_edges = [[] for _ in range((n + 1) ** 2)]
    for c in edges_dict.keys():
        k = len(edges_dict[c])
        for i in range(k - 1):
            p0, q0 = edges_dict[c][i]
            for j in range(i + 1, k):
                p1, q1 = edges_dict[c][j]
                double_edges[p0 * (n + 1) + p1].append(q0 * (n + 1) + q1)
                double_edges[p0 * (n + 1) + p1].append(q1 * (n + 1) + q0)
                double_edges[q0 * (n + 1) + q1].append(p0 * (n + 1) + p1)
                double_edges[q0 * (n + 1) + q1].append(p1 * (n + 1) + p0)
                double_edges[p0 * (n + 1) + q1].append(q0 * (n + 1) + p1)
                double_edges[p0 * (n + 1) + q1].append(p1 * (n + 1) + q0)
                double_edges[q0 * (n + 1) + p1].append(p0 * (n + 1) + q1)
                double_edges[q0 * (n + 1) + p1].append(q1 * (n + 1) + p0)
                double_edges[p1 * (n + 1) + p0].append(q1 * (n + 1) + q0)
                double_edges[p1 * (n + 1) + p0].append(q0 * (n + 1) + q1)
                double_edges[q1 * (n + 1) + q0].append(p1 * (n + 1) + p0)
                double_edges[q1 * (n + 1) + q0].append(p0 * (n + 1) + p1)
                double_edges[q1 * (n + 1) + p0].append(q0 * (n + 1) + p1)
                double_edges[q1 * (n + 1) + p0].append(p1 * (n + 1) + q0)
                double_edges[q0 * (n + 1) + p1].append(q1 * (n + 1) + p0)
                double_edges[q0 * (n + 1) + p1].append(p0 * (n + 1) + q1)

    queue = deque([1 * (n + 1) + n, 1 + (n + 1) * n])
    distance = [10 ** 10] * ((n + 1) ** 2)
    distance[1 * (n + 1) + n] = 0
    distance[1 + (n + 1) * n] = 0
    while len(queue):
        p = queue.popleft()
        for q in double_edges[p]:
            if distance[q] == 10 ** 10:
                distance[q] = distance[p] + 2
                queue.append(q)
    res = 10 ** 10
    for k in single_edges.keys():
        res = min(res, distance[k] + 1)
    for i in range(1, n + 1):
        res = min(res, distance[i * (n + 2)])
    # print(res)
    if res < 10 ** 10:
        return res
    else:
        return -1


def main():
    n, m = map(int, input().split())
    abc_list = [tuple(input().split()) for _ in range(m)]
    res = solve(n, m, abc_list)
    print(res)


def test():
    assert solve(8, 8, [
        (1, 2, "a"), (2, 3, "b"), (1, 3, "c"), (3, 4, "b"), (4, 5, "a"), (5, 6, "c"), (6, 7, "b"), (7, 8, "a")
    ]) == 10
    assert solve(4, 5, [
        (1, 1, "a"), (1, 2, "a"), (2, 3, "a"), (3, 4, "b"), (4, 4, "a")
    ]) == 5
    assert solve(3, 4, [
        (1, 1, "a"), (1, 2, "a"), (2, 3, "b"), (3, 3, "b")
    ]) == -1


if __name__ == "__main__":
    test()
    main()
