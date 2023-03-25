MOD = 998244353


def solve(n, m, k, a_list):
    count_0 = 0
    # 元々x以下の個数
    count_leq_list = [0] * (m + 1)
    nonzero = []
    for a in a_list:
        if a == 0:
            count_0 += 1
        else:
            nonzero.append(a)
    nonzero_s = list(sorted(nonzero))
    nonzero_s.append(m + 1)
    c = 0
    j = 0
    i = 0
    while i <= m:
        if nonzero_s[j] <= i:
            c += 1
            j += 1
        else:
            count_leq_list[i] = c
            i += 1
    # print(count_leq_list)

    # 前計算
    factorial = [1] * (n + 1)
    factorial_inv = [1] * (n + 1)
    for i in range(1, n + 1):
        factorial[i] = (factorial[i - 1] * i) % MOD

    factorial_inv[-1] = pow(factorial[-1], MOD - 2, MOD)

    for i in range(n, 0, -1):
        factorial_inv[i - 1] = (factorial_inv[i] * i) % MOD

    pow_list = [[1] * (count_0 + 1) for _ in range(m + 1)]
    for j in range(1, count_0 + 1):
        pow_list[0][j] = 0
    pow_inv_list = [[1] * (count_0 + 1) for _ in range(m + 1)]
    for i in range(2, m + 1):
        for j in range(count_0):
            pow_list[i][j + 1] = (pow_list[i][j] * i) % MOD
    for i in range(2, m + 1):
        pow_inv_list[i][-1] = pow(pow_list[i][-1], MOD - 2, MOD)
        for j in range(count_0, 0, -1):
            pow_inv_list[i][j - 1] = (pow_inv_list[i][j] * i) % MOD
    # print(pow_list)
    # print(pow_inv_list)

    # x以下になる確率
    prob_leq_list = [0] * (m + 2)
    prob_leq_list[-1] = 1
    for i in range(1, m + 1):
        c_target = k - count_leq_list[i]
        # print(i, c_target)
        if c_target <= 0:
            prob_leq_list[i] = 1
        elif c_target <= count_0:
            # c_target個以上がi以下であればいい
            p = 0
            for j in range(c_target, count_0 + 1):
                # print(i, count_0, j)
                p_add = factorial[count_0] * ((factorial_inv[j] * factorial_inv[count_0 - j]) % MOD) % MOD
                p_add *= pow_list[i][j]
                p_add %= MOD
                p_add *= pow_list[m - i][count_0 - j]
                p_add %= MOD
                # print(p_add)
                p_add *= pow_inv_list[m][count_0]
                p_add %= MOD
                p += p_add
            prob_leq_list[i] = p
        else:
            prob_leq_list[i] = 0
    # print(prob_leq_list)
    res = 0
    for i in range(m + 1):
        res += (i + 1) * (prob_leq_list[i + 1] - prob_leq_list[i])
    res %= MOD
    # print(res)
    return res


def main():
    n, m, k = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, m, k, a_list)
    print(res)


def test():
    assert solve(3, 5, 2, [2, 0, 4]) == 3
    assert solve(2, 3, 1, [0, 0]) == 221832080
    assert solve(10, 20, 7, [6, 5, 0, 2, 0, 0, 0, 15, 0, 0]) == 617586310


if __name__ == "__main__":
    test()
    main()
