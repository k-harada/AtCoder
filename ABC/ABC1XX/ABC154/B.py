import sys


TEST_INPUT = [
    """
    sardine
    """,
    """
    xxxx
    """,
    """
    gone
    """
]
ANSWER = [
    "xxxxxxx",
    "xxxx",
    "xxxx"
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


def solve(ih):
    s = ih.input()
    return "x" * len(s)


def main():
    ih = InputHandler()
    res = solve(ih)
    print(res)


def test():
    for test_input, ans in zip(TEST_INPUT, ANSWER):
        ih = InputHandler(test_input, True)
        res = solve(ih)
        assert str(res) == str(ans)


if __name__ == "__main__":
    test()
    main()
