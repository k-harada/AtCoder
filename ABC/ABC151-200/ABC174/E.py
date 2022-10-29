import numpy as np
import numba


@numba.njit
def count(a_arr, bar):
    # <= bar
    res_arr = ((a_arr - 1) // bar)
    new_bar = (a_arr / (res_arr + 1)).max()
    return res_arr.sum(), np.int(np.ceil(new_bar))


def solve(n, k, a_arr):
    left_bar = ((a_arr - 1) // (k + 1)).min()
    right_bar = a_arr.max()
    while True:
        mid_bar = (left_bar + right_bar) // 2
        # print(left_bar, right_bar, mid_bar)
        m, mid_bar_new = count(a_arr, mid_bar)

        if m > k:
            left_bar = mid_bar
        else:
            right_bar = mid_bar_new

        if left_bar > right_bar - 2:
            break
    return right_bar


def main():
    n_, k_ = map(int, input().split())
    n = np.int32(n_)
    k = np.int32(k_)
    a_arr = np.array(list(map(int, input().split())), dtype=np.int32)
    res = solve(n, k, a_arr)
    print(res)


def test():
    assert solve(2, 3, np.array([7, 9])) == 4
    assert solve(3, 0, np.array([3, 4, 5])) == 5
    assert solve(10, 10, np.array([
        158260522, 877914575, 602436426, 24979445, 861648772,
        623690081, 433933447, 476190629, 262703497, 211047202
    ])) == 292638192


if __name__ == "__main__":
    test()
    main()
