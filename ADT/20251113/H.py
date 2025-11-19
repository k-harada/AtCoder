def solve(n, m, uv_list):
    g = [[] for _ in range(n + 1)]
    for u, v in uv_list:
        g[u].append(v)
        g[v].append(u)
    res = 0
    visited_list = [0] * (n + 1)
    queue = [1]
    while len(queue):
        u = queue.pop()
        if u < 0:
            visited_list[-u] = 0
            continue
        res += 1
        if res == 10 ** 6:
            break
        visited_list[u] = 1
        # if res < 10:
        #     print(res, visited_list)
        #     print(u, g[u])
        #     print(queue)
        queue.append(-u)
        for v in g[u]:
            if visited_list[v] == 0:
                queue.append(v)
    # print(res)
    return res


def main():
    n, m = map(int, input().split())
    uv_list = [tuple(map(int, input().split())) for _ in range(m)]
    res = solve(n, m, uv_list)
    print(res)


def test():
    assert solve(4, 2, [(1, 2), (2, 3)]) == 3
    assert solve(4, 6, [
        (1, 2), (1, 3), (1, 4),
        (2, 3), (2, 4), (3, 4)
    ]) == 16
    assert solve(8, 21, [
        (2, 6), (1, 3), (5, 6), (3, 8), (3, 6), (4, 7), (4, 6),
        (3, 4), (1, 5), (2, 4), (1, 2), (2, 7), (1, 4), (3, 5),
        (2, 5), (2, 3), (4, 5), (3, 7), (6, 7), (5, 7), (2, 8)
    ]) == 2023


if __name__ == "__main__":
    test()
    main()
