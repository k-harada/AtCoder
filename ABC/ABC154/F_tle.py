import sys


TEST_INPUT = [
    """
    1 1 2 2
    """,
    """
    314 159 2653 589
    """
]
ANSWER = [
    "14",
    "602215194"
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


LARGE = 10 ** 9 + 7


def solve_special(r, c):

    if r > 0 and c > 0:
        inv_large = [0] * max(r, c)
        for i in range(1, max(r, c)):
            inv_large[i] = pow(i, LARGE - 2, LARGE)

        # go away for right
        ncr = 1
        pow2 = pow(2, c, LARGE)
        res_right = ncr * (pow2 - 1)

        for i in range(1, c):
            ncr *= (r + i)
            ncr %= LARGE
            ncr *= inv_large[i]
            ncr %= LARGE
            pow2 *= inv_large[2]
            pow2 %= LARGE

            res_right += ncr * (pow2 - 1)
            res_right %= LARGE

        # go away for up
        ncr = 1
        pow2 = pow(2, r, LARGE)
        res_up = ncr * (pow2 - 1)

        for i in range(1, r):
            ncr *= (c + i)
            ncr %= LARGE
            ncr *= inv_large[i]
            ncr %= LARGE
            pow2 *= inv_large[2]
            pow2 %= LARGE

            res_up += ncr * (pow2 - 1)
            res_up %= LARGE

        res = pow(2, r + c + 1, LARGE) - 1 - res_right - res_up
        # print(res_right, res_up)
        return res % LARGE
    else:
        return r + c + 1


def solve(r1, c1, r2, c2):
    res = solve_special(r2, c2) - solve_special(r1 - 1, c2) - solve_special(r2, c1 - 1) + solve_special(r1 - 1, c1 - 1)
    return res % LARGE


def input_and_solve(ih):
    r1, c1, r2, c2 = map(int, ih.input().split())
    res = solve(r1, c1, r2, c2)
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
    # test()
    main()
