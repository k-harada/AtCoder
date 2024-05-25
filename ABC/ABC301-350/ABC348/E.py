from collections import deque


def solve(n, ab_list, c_list):
    g = [[] for _ in range(n)]
    for a, b in ab_list:
        g[a - 1].append(b - 1)
        g[b - 1].append(a - 1)
    children_list = [[] for _ in range(n)]
    parent_list = [-1] * n
    bfs_tour = []
    queue = deque([0])
    while len(queue):
        p = queue.popleft()
        bfs_tour.append(p)
        for q in g[p]:
            if q == parent_list[p]:
                continue
            else:
                parent_list[q] = p
                children_list[p].append(q)
                queue.append(q)
    # print(parent_list)
    # print(children_list)
    # print(bfs_tour)
    count_children = [0] * n
    weight_children = [0] * n
    res_children = [0] * n
    for q in reversed(bfs_tour):
        if q == 0:
            continue
        p = parent_list[q]
        count_children[p] += count_children[q] + 1
        weight_children[p] += weight_children[q] + c_list[q]
        res_children[p] += res_children[q] + weight_children[q] + c_list[q]

    count_parents = [0] * n
    weight_parents = [0] * n
    res_parents = [0] * n
    for p in bfs_tour:
        for q in children_list[p]:
            count_parents[q] = count_parents[p] + 1 + count_children[p] - count_children[q] - 1
            weight_parents[q] = weight_parents[p] + c_list[p] + weight_children[p] - weight_children[q] - c_list[q]
            res_parents[q] = (res_parents[p] + weight_parents[p] + c_list[p]) + (
                    res_children[p] - (res_children[q] + weight_children[q] + c_list[q])
            ) + weight_children[p] - (weight_children[q] + c_list[q])
    # print(res_children)
    # print(weight_parents)
    # print(count_parents)
    # print(res_parents)
    res = [(x + y) for x, y in zip(res_children, res_parents)]
    # print(res)
    return min(res)


def main():
    n = int(input())
    ab_list = [tuple(map(int, input().split())) for _ in range(n - 1)]
    c_list = list(map(int, input().split()))
    res = solve(n, ab_list, c_list)
    print(res)


def test():
    assert solve(4, [(1, 2), (1, 3), (2, 4)], [1, 1, 1, 2]) == 5
    assert solve(2, [(2, 1)], [1, 1000000000]) == 1
    assert solve(7, [(7, 3), (2, 5), (2, 4), (3, 1), (3, 6), (2, 1)], [2, 7, 6, 9, 3, 4, 6]) == 56


if __name__ == "__main__":
    test()
    main()
