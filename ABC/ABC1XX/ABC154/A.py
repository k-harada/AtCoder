import sys


TEST_INPUT = [
    """
    red blue
    3 4
    red
    """,
    """
    red blue
    5 5
    blue
    """
]
ANSWER = [
    "2 4",
    "5 4"
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


def solve(s, t, a, b, u):
    if s == u:
        return str(a - 1) + " " + str(b)
    else:
        return str(a) + " " + str(b - 1)


def input_and_solve(ih):
    s, t = ih.input().split()
    a, b = map(int, ih.input().split())
    u = ih.input()
    res = solve(s, t, a, b, u)
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
