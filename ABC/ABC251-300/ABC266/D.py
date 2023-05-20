def solve(n, txa_list):
    t_max = txa_list[-1][0]
    dp = [[0] * 5 for _ in range(t_max + 1)]
    next_t = txa_list[0][0]
    next_ind = 0
    dp[0][1] = - 10 ** 10
    dp[0][2] = - 10 ** 10
    dp[0][3] = - 10 ** 10
    dp[0][4] = - 10 ** 10
    for t in range(t_max):
        if t == next_t:
            t, x, a = txa_list[next_ind]
            dp[t][x] += a
            next_ind += 1
            if next_ind < n:
                next_t = txa_list[next_ind][0]
            else:
                next_t = t_max + 1
        for j in range(5):
            dp[t + 1][j] = max([dp[t][max(j - 1, 0)], dp[t][j], dp[t][min(j + 1, 4)]])
    t, x, a = txa_list[-1]
    dp[t][x] += a
    # print(dp)
    return max(dp[-1])


def main():
    n = int(input())
    txa_list = [tuple(map(int, input().split())) for _ in range(n)]
    res = solve(n, txa_list)
    print(res)


def test():
    assert solve(3, [(1, 0, 100), (3, 3, 10), (5, 4, 1)]) == 101
    assert solve(3, [(1, 4, 1), (2, 4, 1), (3, 4, 1)]) == 0


if __name__ == "__main__":
    test()
    main()
