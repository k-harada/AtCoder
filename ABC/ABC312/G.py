from collections import deque


def solve(n, ab_list):
    g = [[] for _ in range(n)]
    for a, b in ab_list:
        g[a - 1].append(b - 1)
        g[b - 1].append(a - 1)
    parent = [0] * n
    children = [[] for _ in range(n)]
    queue = deque([0])
    tour = []
    while len(queue):
        p = queue.popleft()
        tour.append(p)
        for q in g[p]:
            if q == parent[p]:
                continue
            parent[q] = p
            children[p].append(q)
            queue.append(q)
    # print(parent)
    # print(children)
    count_children = [1] * n
    for p in reversed(tour):
        for q in children[p]:
            count_children[p] += count_children[q]
    # print(count_children)
    res_negative = 0
    cnt_negative_parts = [0] * n
    for p in reversed(tour):
        sq_s = 0
        s = 0
        for q in children[p]:
            sq_s += count_children[q] ** 2
            s += count_children[q]
        r = (s ** 2 - sq_s) // 2
        res_negative += r

        cnt_negative_parts[p] = count_children[p] - 1
        s1 = 0
        s2 = 0
        s3 = 0
        for q in children[p]:
            cnt_negative_parts[p] += cnt_negative_parts[q]
            s1 += cnt_negative_parts[q] * count_children[q]
            s2 += cnt_negative_parts[q]
            s3 += count_children[q]
        r = s2 * s3 - s1
        # print(r)
        res_negative += r + s2
    # print(cnt_negative_parts)
    # print(res_negative)
    res_all = n * (n - 1) * (n - 2) // 6
    return res_all - res_negative


def main():
    n = int(input())
    ab_list = [tuple(map(int, input().split())) for _ in range(n - 1)]
    res = solve(n, ab_list)
    print(res)


def test():
    assert solve(5, [(1, 2), (2, 3), (2, 4), (1, 5)]) == 2
    assert solve(6, [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]) == 0
    assert solve(12, [
        (1, 6), (3, 4), (10, 4), (5, 9), (3, 1), (2, 3),
        (7, 2), (2, 12), (1, 5), (6, 8), (4, 11)
    ]) == 91


if __name__ == "__main__":
    test()
    main()
