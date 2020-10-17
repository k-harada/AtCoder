def d3(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1]) + max(0, y[2] - x[2])


def solve(n, xyz_list):
    # pre-compute dist
    dist_mat = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dist_mat[i][j] = d3(xyz_list[i], xyz_list[j])

    dp = [[-1] * n for _ in range(2 ** n)]

    def dfs(s, v, dp):
        if dp[s][v] != -1:  # 訪問済みならメモを返す
            return dp[s][v]
        if s == 2 ** n - 1 and v == 0:  # 全ての頂点を訪れて頂点0に戻ってきた
            return 0  # もう動く必要はない
        res = 10 ** 9 + 7
        for u in range(n):
            if s >> u & 1 == 0:  # 未訪問かどうか
                res = min(res, dfs(s | 1 << u, u, dp) + dist_mat[v][u])
        dp[s][v] = res
        return res

    return dfs(0, 0, dp)


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
