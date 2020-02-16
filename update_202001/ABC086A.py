import sys


TEST_INPUT = [
    """
    3 4
    """,
    """
    1 21
    """
]
ANSWER = [
    "Even",
    "Odd"
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


def solve(a, b):
    if a * b % 2:
        return "Odd"
    else:
        return "Even"


def main():
    ih = InputHandler()
    a, b = map(int, ih.input().split())
    res = solve(a, b)
    print(res)


def test():
    for test_input, ans in zip(TEST_INPUT, ANSWER):
        ih = InputHandler(test_input, True)
        a, b = map(int, ih.input().split())
        res = solve(a, b)
        assert str(res) == str(ans)


if __name__ == "__main__":
    test()
    main()
