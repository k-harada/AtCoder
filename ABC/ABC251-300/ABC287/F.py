from collections import deque


MOD = 998244353


def solve(n, ab_list):
    g = [[] for _ in range(n + 1)]
    for a, b in ab_list:
        g[a].append(b)
        g[b].append(a)

    queue = deque([1])
    visited = [0] * (n + 1)
    visit_list = []
    parent_list = [0] * (n + 1)
    while len(queue):
        p = queue.popleft()
        visited[p] = 1
        visit_list.append(p)
        for q in g[p]:
            if visited[q]:
                continue
            parent_list[q] = p
            queue.append(q)
    # print(visit_list)

    dp_open = [[0] * (n + 1)for _ in range(n + 1)]
    dp_closed = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp_open[i][1] = 1
        dp_closed[i][0] = 1

    count_list = [1] * (n + 1)
    for q in reversed(visit_list):
        if q == 1:
            break
        p = parent_list[q]
        temp_closed = [0] * (count_list[p] + count_list[q] + 1)
        for i in range(count_list[p] + 1):
            for j in range(count_list[q] + 1):
                temp_closed[i + j] += dp_closed[p][i] * (dp_open[q][j] + dp_closed[q][j]) % MOD
        for k in range(count_list[p] + count_list[q] + 1):
            dp_closed[p][k] = temp_closed[k] % MOD

        temp_open = [0] * (count_list[p] + count_list[q] + 1)
        for i in range(count_list[p] + 1):
            for j in range(count_list[q] + 1):
                temp_open[i + j] += dp_open[p][i] * (dp_open[q][j + 1] + dp_closed[q][j]) % MOD
        for k in range(count_list[p] + count_list[q] + 1):
            dp_open[p][k] = temp_open[k] % MOD
        # print(p, q)
        # print(dp_open[p])
        # print(dp_closed[p])
        count_list[p] += count_list[q]

    res = []
    for i in range(1, n + 1):
        res.append((dp_open[1][i] + dp_closed[1][i]) % MOD)
    return res


def main():
    n = int(input())
    ab_list = [tuple(map(int, input().split())) for _ in range(n - 1)]
    res = solve(n, ab_list)
    for r in res:
        print(r)


def test():
    assert solve(4, [(1, 2), (2, 3), (3, 4)]) == [10, 5, 0, 0]
    assert solve(2, [(1, 2)]) == [3, 0]
    assert solve(10, [(3, 4), (3, 6), (6, 9), (1, 3), (2, 4), (5, 6), (6, 10), (1, 8), (5, 7)]) == [
        140, 281, 352, 195, 52, 3, 0, 0, 0, 0
    ]


if __name__ == "__main__":
    test()
    main()
