from itertools import permutations


def solve(n, a_list):
    counts = [0] * 5
    for a in a_list:
        counts[a] += 1
    positions = [1] * counts[1] + [2] * counts[2] + [3] * counts[3] + [4] * counts[4]
    g = [[0] * 5 for _ in range(5)]
    for i, a in enumerate(a_list):
        g[a][positions[i]] += 1
    # print(g)
    res = 0
    for i in range(1, 5):
        for j in range(i + 1, 5):
            # i-j
            d = min(g[i][j], g[j][i])
            g[i][j] -= d
            g[j][i] -= d
            g[i][i] += d
            g[j][j] += d
            res += d
    # print(g)
    # print(res)
    for i in range(1, 5):
        for j in range(i + 1, 5):
            for k in range(j + 1, 5):
                # i-j-k
                d = min(g[i][j], g[j][k], g[k][i])
                g[i][j] -= d
                g[j][k] -= d
                g[k][i] -= d
                g[i][i] += d
                g[j][j] += d
                g[k][k] += d
                res += 2 * d
                # i-k-j
                d = min(g[i][k], g[k][j], g[j][i])
                g[i][k] -= d
                g[k][j] -= d
                g[j][i] -= d
                g[i][i] += d
                g[j][j] += d
                g[k][k] += d
                res += 2 * d
    # print(g)
    # print(res)
    # quads
    for p in permutations(list(range(1, 5))):
        d = min(g[p[0]][p[1]], g[p[1]][p[2]], g[p[2]][p[3]], g[p[3]][p[0]])
        g[p[0]][p[1]] -= d
        g[p[1]][p[2]] -= d
        g[p[2]][p[3]] -= d
        g[p[3]][p[0]] -= d
        g[0][0] += d
        g[1][1] += d
        g[2][2] += d
        g[3][3] += d
        res += 3 * d
    return res


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(6, [3, 4, 1, 1, 2, 4]) == 3
    assert solve(4, [2, 3, 4, 1]) == 3


if __name__ == "__main__":
    test()
    main()
