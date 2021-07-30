import numpy as np
import numba


@numba.njit
def pre_solve():
    w_max = 50
    b_max = 50 + np.arange(51).sum()
    dp = np.zeros((b_max + 1, w_max + 1), dtype=np.int32)
    v_count = np.zeros(b_max + 1, dtype=np.int32)
    r = 0
    # w = 0
    dp[1, 0] = 0
    v_count[0] += 1
    for b in range(2, b_max + 1):
        if b % 2 == 1:
            v_count[dp[b // 2, 0]] -= 1
        for r in range(w_max + 1):
            if v_count[r] == 0:
                break
        dp[b, 0] = r
        v_count[dp[b, 0]] += 1

    # w >= 1
    for w in range(1, w_max + 1):

        v_count *= 0

        # b = 0
        b = 0
        if dp[w + b, w - 1] == 0:
            dp[b, w] = 1
        else:
            dp[b, w] = 0

        # b = 1
        b = 1
        if dp[w + b, w - 1] == 0:
            dp[b, w] = 1
        else:
            dp[b, w] = 0
        v_count[dp[b, w]] += 1

        for b in range(2, b_max + 1 - w):
            v_count[dp[w + b, w - 1]] += 1
            if b % 2 == 1:
                v_count[dp[b // 2, w]] -= 1
            for r in range(w_max + 1):
                if v_count[r] == 0:
                    break
            dp[b, w] = r
            v_count[dp[w + b, w - 1]] -= 1
            v_count[dp[b, w]] += 1
    return dp


dp_pre = pre_solve()
# print(dp_pre[:10, :10])


def solve(n, w_list, b_list):
    res = 0
    for w, b in zip(w_list, b_list):
        res ^= dp_pre[b, w]
    if res == 0:
        return "Second"
    else:
        return "First"


def main():
    n = int(input())
    w_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    res = solve(n, w_list, b_list)
    print(res)


def test():
    assert solve(1, [0], [2]) == "First"
    assert solve(2, [10, 10], [10, 10]) == "Second"
    assert solve(1, [1], [1]) == "Second"
    assert solve(6, [3, 1, 4, 1, 5, 9], [2, 7, 1, 8, 2, 8]) == "Second"
    assert solve(6, [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]) == "First"


if __name__ == "__main__":
    test()
    main()
