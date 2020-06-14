def solve(n, k, s, t, a_list):

    if s & t != s:
        return 0

    s_list = [0] * 18
    t_list = [0] * 18
    ab_list = [[0] * 18 for _ in range(n)]

    for i in range(18):
        s_list[i] = (s // (2 ** i)) % 2
        t_list[i] = (t // (2 ** i)) % 2
        for m in range(n):
            ab_list[m][i] = (a_list[m] // (2 ** i)) % 2

    # select
    m_list = []
    for m in range(n):
        flag = True
        for i in range(18):
            if s_list[i] == 1 and ab_list[m][i] == 0:
                # fail
                flag = False
            if t_list[i] == 0 and ab_list[m][i] == 1:
                # fail
                flag = False
        if flag:
            m_list.append(m)

    mm = len(m_list)
    if mm == 0:
        return 0

    u = 0
    for i in range(18):
        if s_list[i] == 0 and t_list[i] == 1:
            u += 2 ** i

    # new list
    a_list_new = [a_list[m] & u for m in m_list]

    res = 0

    for m in range(mm):
        # force use
        dp = [[0] * (2 ** 18) for _ in range(mm)]
        a = a_list_new[m]
        dp[0][0] = 1
        for n in range(m + 1, mm):
            for i in range(mm - 1, 0, -1):
                for j in range(2 ** 18):
                    dp[i][j | (a_list_new[n] ^ a)] += dp[i - 1][j]
        for i in range(k):
            res += dp[i][u]

    return res


def main():
    n, k, s, t = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, k, s, t, a_list)
    print(res)


def test():
    assert solve(3, 3, 0, 3, [1, 2, 3]) == 2
    assert solve(5, 3, 1, 7, [3, 4, 9, 1, 5]) == 2
    assert solve(5, 4, 0, 15, [3, 4, 9, 1, 5]) == 3


if __name__ == "__main__":
    test()
    main()
