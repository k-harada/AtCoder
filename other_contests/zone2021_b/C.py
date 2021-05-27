def solve(n, m, ab_list):

    g = [[] for _ in range(n)]
    for a, b in ab_list:
        g[a].append(b)
        g[b].append(a)

    ijk_max = 1, 2, 3
    v_max = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                neighbors = [0] * n
                neighbors[i] = 1
                neighbors[j] = 1
                neighbors[k] = 1
                for p in g[i]:
                    neighbors[p] = 1
                for p in g[j]:
                    neighbors[p] = 1
                for p in g[k]:
                    neighbors[p] = 1
                v = sum(neighbors)
                if v > v_max:
                    ijk_max = i, j, k
                    v_max = v
    return ijk_max


def main():
    n, m = map(int, input().split())
    ab_list = [tuple(map(int, input().split())) for _ in range(m)]
    res = solve(n, m, ab_list)
    print(res)


def test():
    assert solve(15, 23, [
        (0, 3), (0, 4), (0, 13), (1, 5), (1, 8),
        (1, 9), (1, 12), (2, 6), (2, 7), (2, 10),
        (2, 11), (2, 12), (3, 5), (3, 8), (4, 5),
        (4, 9), (6, 7), (6, 9), (6, 12), (8, 10),
        (10, 11), (10, 12), (11, 14)
    ]) == (0, 1, 2)


if __name__ == "__main__":
    test()
    main()
