def d3(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1]) + max(0, y[2] - x[2])


def solve(n, xyz_list):
    # pre-compute dist
    dist_mat = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dist_mat[i][j] = d3(xyz_list[i], xyz_list[j])

    dp = [[10 ** 9 + 7] * n for _1 in range(2 ** n)]

    u_list = []
    for u in range(2 ** n):
        s = 0
        for j in range(n):
            s += 1 & (u >> j)
        u_list.append([u, s])
    u_list_bit = [u[0] for u in sorted(u_list, key=lambda x: x[1])]
    dp[0][0] = 0
    for u in u_list_bit:
        for i in range(n):
            for j in range(n):
                v = u | (2 ** j)
                dp[v][j] = min(dp[v][j], dp[u][i] + dist_mat[i][j])
    return dp[2 ** n - 1][0]


def main():
    n = int(input())
    xyz_list = [list(map(int, input().split())) for _ in range(n)]
    res = solve(n, xyz_list)
    print(res)


def test():
    assert solve(2, [[0, 0, 0], [1, 2, 3]]) == 9
    assert solve(3, [[0, 0, 0], [1, 1, 1], [-1, -1, -1]]) == 10


if __name__ == "__main__":
    test()
    main()
