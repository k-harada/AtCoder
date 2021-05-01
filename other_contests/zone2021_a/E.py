from heapq import heappop, heappush


def solve(r, c, a_matrix, b_matrix):
    g = [[] for _ in range(2 * r * c)]
    for i in range(r):
        for j in range(c):
            # move 1 and 2
            if j < c - 1:
                p = c * i + j
                q = p + 1
                g[p].append((q, a_matrix[i][j]))
                g[q].append((p, a_matrix[i][j]))
            # move 3
            if i < r - 1:
                p = c * i + j
                q = p + c
                g[p].append((q, b_matrix[i][j]))
            # move 4
            p = c * i + j
            q = p + r * c
            g[p].append((q, 1))
            g[q].append((p, 0))
            if i > 0:
                p = c * i + j + r * c
                q = p - c
                g[p].append((q, 1))
    # dijkstra
    d_list = [10 ** 9 + 7] * (r * c * 2)
    h = [(0, 0)]
    while len(h):
        d, p = heappop(h)
        if d_list[p] <= d:
            continue
        d_list[p] = d
        for q, add_d in g[p]:
            heappush(h, (d + add_d, q))

    return d_list[r * c - 1]


def main():
    r, c = map(int, input().split())
    a_matrix = [list(map(int, input().split())) for _ in range(r)]
    b_matrix = [list(map(int, input().split())) for _ in range(r - 1)]
    res = solve(r, c, a_matrix, b_matrix)
    print(res)


def test():
    assert solve(3, 3, [[10, 1], [10, 10], [1, 10]], [[1, 10, 1], [1, 10, 1]]) == 9
    assert solve(4, 4, [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]) == 0


if __name__ == "__main__":
    test()
    main()
