def solve(n, dcs_list):
    d_max = max([d for d, c, s in dcs_list])
    dp = [0] * (d_max + 1)
    dcs_list_s = list(sorted(dcs_list, key=lambda x: x[0]))
    for d, c, s in dcs_list_s:
        for d_s in range(d - c, -1, -1):
            dp[d_s + c] = max(dp[d_s + c], dp[d_s] + s)
    return max(dp)


def main():
    n = int(input())
    dcs_list = [tuple(map(int, input().split())) for _ in range(n)]
    res = solve(n, dcs_list)
    print(res)


def test():
    assert solve(1, [(12, 3, 69853)]) == 69853
    assert solve(3, [(7, 3, 200000), (3, 2, 100000), (5, 3, 150000)]) == 350000
    assert solve(8, [
        (376, 640, 602876667), (4015, 1868, 533609371), (3330, 152, 408704870), (1874, 798, 30417810),
        (2, 1450, 40706045), (3344, 1840, 801881841), (2853, 1229, 5235900), (458, 1277, 997429858)
    ]) == 1744196082


if __name__ == "__main__":
    test()
    main()
