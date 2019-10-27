def solve_f(n, g):
    e_base = [0.0] * (n + 1)
    p_base = [0.0] * (n + 1)

    # e_base
    for i in range(n - 1, 0, -1):
        e_base[i] = sum([e_base[j] for j in g[i]]) / len(g[i]) + 1.0

    # p_base
    p_base[1] = 1.0
    for i in range(1, n):
        for j in g[i]:
            p_base[j] += p_base[i] / len(g[i])

    # print(p_base, e_base)

    # find maximal gap
    gap = 0.0
    for i in range(1, n):
        if len(g[i]) == 1:
            continue
        total = sum([e_base[j] + 1 for j in g[i]])
        maxim = max([e_base[j] + 1 for j in g[i]])
        gap_i = (total / len(g[i]) - (total - maxim) / (len(g[i]) - 1)) * p_base[i]
        gap = max(gap_i, gap)

    return e_base[1] - gap


def main():
    # input
    n, m = map(int, input().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        s, t = map(int, input().split())
        g[s].append(t)
    res = solve_f(n, g)
    print(res)


def test():
    assert abs(solve_f(4, [[], [2, 3, 4], [3, 4], [4]]) - 1.5) < 0.000001
    assert abs(solve_f(3, [[], [2], [3]]) - 2.0) < 0.000001


if __name__ == "__main__":
    test()
    main()
