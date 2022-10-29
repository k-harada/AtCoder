import sys


TEST_INPUT = [
    """
    36
    """,
    """
    91
    """,
    """
    314159265358979323846264338327950288419716939937551058209749445923078164062862089986280348253421170
    """
]
ANSWER = [
    "8",
    "3",
    "243"
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


def solve(n):

    dp = [0, 1]
    for s in n:
        a = int(s)
        dp = [min(dp[0] + a, dp[1] + 10 - a), min(dp[0] + a + 1, dp[1] + 9 - a)]

    return dp[0]


def input_and_solve(ih):
    n = ih.input()
    res = solve(n)
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
