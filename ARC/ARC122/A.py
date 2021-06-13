MOD = 10 ** 9 + 7


def solve(n, a_list):
    dp_v = [[0] * 2 for _ in range(n)]
    dp_n = [[0] * 2 for _ in range(n)]
    dp_v[0][0] = a_list[0]
    dp_n[0][0] = 1
    for i in range(1, n):
        dp_v[i][0] = (dp_v[i - 1][0] + dp_v[i - 1][1] + (dp_n[i - 1][0] + dp_n[i - 1][1]) * a_list[i]) % MOD
        dp_v[i][1] = (dp_v[i - 1][0] - dp_n[i - 1][0] * a_list[i]) % MOD
        dp_n[i][0] = (dp_n[i - 1][0] + dp_n[i - 1][1]) % MOD
        dp_n[i][1] = dp_n[i - 1][0]
    # print(dp_v)
    # print(dp_n)
    return (dp_v[-1][0] + dp_v[-1][1]) % MOD


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(3, [3, 1, 5]) == 15
    assert solve(4, [1, 1, 1, 1]) == 10
    assert solve(10, [
        866111664, 178537096, 844917655, 218662351, 383133839, 231371336, 353498483, 865935868, 472381277, 579910117
    ]) == 279919144


if __name__ == "__main__":
    test()
    main()