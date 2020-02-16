import sys
from bisect import bisect_left, bisect_right


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


def query(a, n, a_list_s, k):
    res = 0

    for i in range(n - 1):
        p = a_list_s[i]
        if p > 0:
            q = (a + p - 1) // p
            res += min(n - bisect_left(a_list_s, q), n - i - 1)
        elif p == 0:
            if a <= 0:
                res += n - i - 1
        else:
            q = a // p
            res += max(bisect_right(a_list_s, q) - (i + 1), 0)
    if res < n * (n - 1) // 2 - k + 1:
        return False
    else:
        return True


def solve(n, k, a_list):

    a_list_s = list(sorted(a_list))

    left = - 10 ** 18 - 1
    right = 10 ** 18 + 1
    center = 0

    while right > left + 1:
        if query(center, n, a_list_s, k):
            left, center = center, (center + right) // 2
        else:
            center, right = (left + center) // 2, center

    return left


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
        assert str(res) == str(ans)


if __name__ == "__main__":
    test()
    main()
