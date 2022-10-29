from collections import deque


def solve(n, a_list, b_list):

    # create graph
    g = {i: dict() for i in range(n)}
    for i in range(n - 1):
        a, b = a_list[i] - 1, b_list[i] - 1
        g[a][b] = -1
        g[b][a] = -1

    k = max([len(g[a]) for a in range(n)])

    used_color = [-1] * n
    used_color[0] = k - 1
    # BFS
    queue = deque([0])
    while len(queue) > 0:
        p = queue.popleft()
        c = used_color[p]
        for q in g[p].keys():
            if used_color[q] != -1:
                continue
            c += 1
            c %= k
            # print(p, q, c)
            g[p][q] = c
            g[q][p] = c
            used_color[q] = c
            queue.append(q)

    res_list = [0] * (n - 1)
    for i in range(n - 1):
        res_list[i] = g[a_list[i] - 1][b_list[i] - 1] + 1

    return k, res_list


def main():
    n = int(input())
    a_list = [0] * (n - 1)
    b_list = [0] * (n - 1)
    for i in range(n - 1):
        a, b = map(int, input().split())
        a_list[i] = a
        b_list[i] = b

    k, res_list = solve(n, a_list, b_list)
    print(k)
    for i in range(n - 1):
        print(res_list[i])


def test():
    print(solve(3, [1, 2], [2, 3]))
    print(solve(8, [1, 2, 2, 2, 4, 5, 6], [2, 3, 4, 5, 7, 6, 8]))


if __name__ == "__main__":
    # test()
    main()
