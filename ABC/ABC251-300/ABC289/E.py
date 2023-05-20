from collections import deque


def solve_sub(n, m, c_list, uv_list):
    g = [[] for _ in range(n + 1)]
    for u, v in uv_list:
        g[u].append(v)
        g[v].append(u)
    queue = deque([(1, n)])
    d_list = [[-1] * (n + 1) for _ in range(n + 1)]
    d_list[1][n] = 0
    while len(queue):
        p, q = queue.popleft()
        for r in g[p]:
            for s in g[q]:
                if c_list[r - 1] == c_list[s - 1]:
                    continue
                if d_list[r][s] == -1:
                    d_list[r][s] = d_list[p][q] + 1
                    queue.append((r, s))
    return d_list[n][1]


def solve(t, case_list):
    res = []
    for n, m, c_list, uv_list in case_list:
        if c_list[0] == c_list[-1]:
            res.append(-1)
        else:
            res.append(solve_sub(n, m, c_list, uv_list))
    return res


def main():
    t = int(input())
    case_list = []
    for _ in range(t):
        n, m = map(int, input().split())
        c_list = list(map(int, input().split()))
        uv_list = [tuple(map(int, input().split())) for _ in range(m)]
        case_list.append((n, m, c_list, uv_list))
    res = solve(t, case_list)
    for r in res:
        print(r)


def test():
    assert solve(3, [
        (4, 4, [0, 1, 0, 1], [(1, 2), (2, 3), (1, 3), (2, 4)]),
        (3, 3, [0, 1, 0], [(1, 2), (2, 3), (1, 3)]),
        (6, 6, [0, 0, 1, 1, 0, 1], [(1, 2), (2, 6), (3, 6), (4, 6), (4, 5), (2, 4)])
    ]) == [3, -1, 3]


if __name__ == "__main__":
    test()
    main()
