import numpy as np
import numba


MOD = 10 ** 9 + 7


@numba.njit('i8(i8, i8, i8, i8[:])')
def solve(n, b, k, c_list):
    dp = np.zeros((120, b), dtype=np.int64)
    for c in c_list:
        dp[0, c % b] += 1
    d_list = np.zeros(61, dtype=np.int64)
    d_list[0] = 10 % b
    for i in range(60):
        d_list[i + 1] = (d_list[i] * d_list[i]) % b
    m = 1
    i = 0
    for i in range(60):
        if 2 * m > n:
            break
        m *= 2
        for x in range(b):
            p = x * d_list[i]
            for y in range(b):
                dp[i + 1, (p + y) % b] += dp[i][x] * dp[i][y]
                dp[i + 1, (p + y) % b] %= MOD

    # print(m, i)
    # print(dp)

    for j in range(59, -1, -1):
        # print(n, m, 2 ** j)
        if n - m >= 2 ** j:
            for x in range(b):
                p = x * d_list[j]
                for y in range(b):
                    dp[i + 1, (p + y) % b] += dp[i][x] * dp[j][y]
                    dp[i + 1, (p + y) % b] %= MOD
            m += 2 ** j
            i += 1

    # print(dp)

    return dp[i, 0]


def main():
    n, b, k = map(int, input().split())
    c_list = np.array(list(map(int, input().split())), dtype=np.int64)
    res = solve(n, b, k, c_list)
    print(res)


def test():
    assert solve(3, 7, 3, np.array([1, 4, 9])) == 3
    assert solve(5, 2, 3, np.array([1, 4, 9])) == 81
    assert solve(10000, 27, 7, np.array([1, 3, 4, 6, 7, 8, 9])) == 989112238
    assert solve(1000000000000000000, 29, 6, np.array([1, 2, 4, 5, 7, 9])) == 853993813
    assert solve(1000000000000000000, 957, 7, np.array([1, 2, 3, 5, 6, 7, 9])) == 205384995


if __name__ == "__main__":
    test()
    main()
