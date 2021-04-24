def solve(n, m, xyz_list):
    q = 2 ** n
    dp = [[0] * q for _ in range(n + 1)]
    conditions_list = [[] for _ in range(n + 1)]
    for x, y, z in xyz_list:
        conditions_list[y].append((x, y, z))
    count_list = [[0] * q for _ in range(n + 1)]
    dp[0][0] = 1
    for p in range(q):
        for i in range(n):
            if (p >> i) % 2 == 1:
                count_list[i + 1][p] = count_list[i][p] + 1
            else:
                count_list[i + 1][p] = count_list[i][p]
    for i in range(n):
        # dp
        for p in range(q):
            if dp[i][p] == 0:
                continue
            for j in range(n):
                if p ^ (2 ** j) == p + 2 ** j:
                    dp[i + 1][p + 2 ** j] += dp[i][p]
        # check conditions
        for x, y, z in conditions_list[i + 1]:
            for p in range(q):
                if count_list[x][p] > z:
                    dp[i + 1][p] = 0
    # print(dp)
    return dp[-1][-1]


def main():
    n, m = map(int, input().split())
    xyz_list = [tuple(map(int, input().split())) for _ in range(m)]
    res = solve(n, m, xyz_list)
    print(res)


def test():
    assert solve(3, 1, [(2, 2, 1)]) == 4
    assert solve(5, 2, [(3, 3, 2), (4, 4, 3)]) == 90
    assert solve(18, 0, []) == 6402373705728000


if __name__ == "__main__":
    # test()
    main()
