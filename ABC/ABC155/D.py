import sys
import numpy as np


TEST_INPUT = [
    """
    4 3
    3 3 -4 -2
    """,
    """
    10 40
    5 4 3 2 -1 0 0 0 0 0
    """,
    """
    30 413
    -170202098 -268409015 537203564 983211703 21608710 -443999067 -937727165 -97596546 -372334013 398994917 -972141167 798607104 -949068442 -959948616 37909651 0 886627544 -20098238 0 -948955241 0 -214720580 277222296 -18897162 834475626 0 -425610555 110117526 663621752 0
    """
]
ANSWER = [
    "-6",
    "6",
    "448283280358331064"
]


class InputHandler:

    def __init__(self, text_lines="", is_test=False):
        self.data = list(text_lines.split("\n"))
        self.index = 0
        self.is_test = is_test

    def input(self):
        if self.is_test:
            self.index += 1
            return self.data[self.index].strip()
        else:
            return sys.stdin.readline().rstrip()


def query(a, n, a_arr_p, a_arr_n, n_zeros, k):

    # return (num of pairs <= a) < k

    if a >= 0:
        # negative
        res = len(a_arr_p) * len(a_arr_n)
        # zero
        res += n_zeros * (n - n_zeros) + n_zeros * (n_zeros - 1) // 2
        # p * p
        res_pp = np.searchsorted(a_arr_p, a // a_arr_p, side="right").sum()
        res_pp -= (a_arr_p * a_arr_p <= a).sum()
        res += res_pp // 2
        # n * n
        res_nn = np.searchsorted(a_arr_n, a // a_arr_n, side="right").sum()
        res_nn -= (a_arr_n * a_arr_n <= a).sum()
        res += res_nn // 2
    else:
        # p * n
        res = len(a_arr_p) * len(a_arr_n) - np.searchsorted(a_arr_n, (a_arr_p - a - 1) // a_arr_p, side="left").sum()
    # print(a, res)
    if res < k:
        return True
    else:
        return False


def solve(n, k, a_list):

    left = - 10 ** 18 - 1
    right = 10 ** 18 + 1
    center = 0

    a_arr = np.array(a_list)

    a_arr_p = a_arr[a_arr > 0]
    a_arr_n = - a_arr[a_arr < 0]
    n_zeros = (a_arr == 0).sum()
    a_arr_p.sort()
    a_arr_n.sort()

    while right > left + 1:
        if query(center, n, a_arr_p, a_arr_n, n_zeros, k):
            left, center = center, (center + right) // 2
        else:
            center, right = (left + center) // 2, center

    return right


def input_and_solve(ih):
    n, k = map(int, ih.input().split())
    a_list = list(map(int, ih.input().split()))
    res = solve(n, k, a_list)
    return res


def main():
    ih = InputHandler()
    res = input_and_solve(ih)
    print(res)


def test():
    for test_input, ans in zip(TEST_INPUT, ANSWER):
        ih = InputHandler(test_input, True)
        res = input_and_solve(ih)
        # print(res, ans)
        assert str(res) == str(ans)


if __name__ == "__main__":
    test()
    main()
