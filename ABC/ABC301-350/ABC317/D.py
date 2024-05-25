def solve(n, xyz_list):
    z0 = 0
    z1 = 0
    diff_list = []
    for x, y, z in xyz_list:
        if x < y:
            z1 += z
            diff_list.append(((y - x + 1) // 2, z))
        else:
            z0 += z
    # print(z0, z1)
    # print(diff_list)
    if z0 > z1:
        return 0
    m = len(diff_list)
    dp = [[10 ** 15] * (10 ** 5 + 1) for _ in range(m + 1)]
    dp[0][0] = 0
    for i, (d, z) in enumerate(diff_list):
        for z_ in range(10 ** 5 + 1):
            if dp[i][z_] < 10 ** 15 and z_ + z <= 10 ** 5:
                dp[i + 1][z_ + z] = min(dp[i + 1][z_ + z], dp[i][z_] + d)
            dp[i + 1][z_] = min(dp[i + 1][z_], dp[i][z_])
    res = min(dp[m][(z1 - z0 + 1) // 2:])
    return res


def main():
    n = int(input())
    xyz_list = [tuple(map(int, input().split())) for _ in range(n)]
    res = solve(n, xyz_list)
    print(res)


def test():
    assert solve(1, [(3, 8, 1)]) == 3
    assert solve(2, [(3, 6, 2), (1, 8, 5)]) == 4
    assert solve(3, [(3, 4, 2), (1, 2, 3), (7, 2, 6)]) == 0
    assert solve(10, [
        (1878, 2089, 16),
        (1982, 1769, 13),
        (2148, 1601, 14),
        (2189, 2362, 15),
        (2268, 2279, 16),
        (2394, 2841, 18),
        (2926, 2971, 20),
        (3091, 2146, 20),
        (3878, 4685, 38),
        (4504, 4617, 29),
    ]) == 86


if __name__ == "__main__":
    test()
    main()
