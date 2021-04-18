from collections import deque


def solve(n, ab_list):
    g = [[] for _ in range(n + 1)]
    for a, b in ab_list:
        g[a].append(b)
        g[b].append(a)

    d_list_1 = [n] * (n + 1)
    d_list_1[1] = 0
    queue = deque([1])
    while len(queue):
        p = queue.popleft()
        for q in g[p]:
            if d_list_1[q] == n:
                d_list_1[q] = d_list_1[p] + 1
                queue.append(q)
    # print(d_list_1)
    d_max = 0
    new_p = 1
    for i in range(1, n + 1):
        if d_list_1[i] > d_max:
            d_max = d_list_1[i]
            new_p = i

    d_list_p = [n] * (n + 1)
    d_list_p[new_p] = 0
    parent_p = [0] * (n + 1)
    queue = deque([new_p])
    while len(queue):
        p = queue.popleft()
        for q in g[p]:
            if d_list_p[q] == n:
                parent_p[q] = p
                d_list_p[q] = d_list_p[p] + 1
                queue.append(q)
    d_max = 0
    new_q = 1
    for i in range(1, n + 1):
        if d_list_p[i] > d_max:
            d_max = d_list_p[i]
            new_q = i

    long_path = []
    p = new_q
    in_the_path = [0] * (n + 1)
    while p != 0:
        in_the_path[p] = 1
        long_path.append(p)
        p = parent_p[p]
    # print(long_path)

    # dfs
    res_list = [0] * (n + 1)
    visited = [0] * (n + 1)
    queue = deque(long_path)
    e = 0
    while len(queue):
        p = queue.popleft()
        e += 1
        if visited[p]:
            continue
        res_list[p] = e
        visited[p] = 1
        for q in g[p]:
            if visited[q] == 0:
                if in_the_path[p] and in_the_path[q]:
                    pass
                else:
                    queue.appendleft(p)
                    queue.appendleft(q)
    # assert max(res_list[1:]) == 2 * n - 1 - len(long_path) + 1
    return " ".join([str(res) for res in res_list[1:]])


def main():
    n = int(input())
    ab_list = [tuple(map(int, input().split())) for _ in range(n - 1)]
    res = solve(n, ab_list)
    print(res)


def test():
    assert solve(2, [(1, 2)]) == "1 2"
    assert solve(4, [(1, 2), (1, 4), (2, 3)]) == "2 3 4 1"


if __name__ == "__main__":
    test()
    main()
