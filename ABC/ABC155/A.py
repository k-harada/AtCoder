import sys


TEST_INPUT = [
    """
    5 7 5
    """,
    """
    4 4 4
    """,
    """
    4 9 6
    """,
    """
    3 3 4
    """
]
ANSWER = [
    "Yes",
    "No",
    "No",
    "Yes"
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


def solve(a, b, c):
    if len({a, b, c}) == 2:
        return "Yes"
    else:
        return "No"


def input_and_solve(ih):
    a, b, c = map(int, ih.input().split())
    res = solve(a, b, c)
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
