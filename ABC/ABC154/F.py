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


def solve(r1, c1, r2, c2):

    fact = [0] * (r2 + c2 + 3)
    fact[0] = 1
    for i in range(1, r2 + c2 + 3):
        fact[i] = fact[i - 1] * i % LARGE

    fact_inv = [0] * (r2 + c2 + 3)
    fact_inv[-1] = pow(fact[-1], LARGE - 2, LARGE)
    for i in range(r2 + c2 + 1, -1, -1):
        fact_inv[i] = fact_inv[i + 1] * (i + 1) % LARGE

    def solve_special(r, c):
        return (fact[r + c + 2] * fact_inv[r + 1] * fact_inv[c + 1] - 1) % LARGE

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
