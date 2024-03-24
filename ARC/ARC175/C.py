def solve(n, lr_list):
    # 最小値を出す
    # 常に\_/になる
    dp = [[0] * 3 for _ in range(n)]
    dp[n - 1][0] = lr_list[n - 1][0]
    dp[n - 1][1] = lr_list[n - 1][1]
    for i in range(n - 2, -1, -1):
        l0, r0 = lr_list[i]
        if r0 <= dp[i + 1][0]:
            dp[i][0] = r0
            dp[i][1] = r0
            dp[i][2] = dp[i + 1][2] + dp[i + 1][0] - r0
        elif dp[i + 1][1] <= l0:
            dp[i][0] = l0
            dp[i][1] = l0
            dp[i][2] = dp[i + 1][2] + l0 - dp[i + 1][0]
        else:
            dp[i][2] = dp[i + 1][2]
            if dp[i + 1][0] < l0:
                dp[i][0] = l0
            else:
                dp[i][0] = dp[i + 1][0]
            if dp[i + 1][1] > r0:
                dp[i][1] = r0
            else:
                dp[i][1] = dp[i + 1][1]
    # print(dp[0][2])
    # print(dp)
    res_list = [dp[0][0]]
    for i in range(1, n):
        p = res_list[i - 1]
        l1, r1 = lr_list[i]
        if p < l1:
            res_list.append(l1)
        elif l1 <= p <= dp[i][1]:
            res_list.append(p)
        elif dp[i][1] <= p:
            res_list.append(dp[i][1])
    # print(res_list)
    res = " ".join([str(r) for r in res_list])
    return res


def main():
    n = int(input())
    lr_list = [tuple(map(int, input().split())) for _ in range(n)]
    res = solve(n, lr_list)
    print(res)


def test():
    assert solve(4, [(1, 10), (8, 13), (3, 4), (5, 20)]) == "8 8 4 5"
    assert solve(3, [(20, 24), (3, 24), (1, 75)]) == "20 20 20"
    assert solve(15, [
        (335279264, 849598327),
        (446755913, 822889311),
        (526239859, 548830120),
        (181424399, 715477619),
        (342858071, 625711486),
        (448565595, 480845266),
        (467825612, 647639160),
        (160714711, 449656269),
        (336869678, 545923679),
        (61020590, 573085537),
        (626006012, 816372580),
        (135599877, 389312924),
        (511429216, 547865075),
        (561330066, 605997004),
        (539239436, 921749002),
    ]) == "526239859 526239859 526239859 467825612 467825612 467825612 467825612 449656269 449656269 449656269 626006012 389312924 511429216 561330066 561330066"


if __name__ == "__main__":
    test()
    main()
