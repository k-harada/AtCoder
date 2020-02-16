import sys


TEST_INPUT = [
    """
    1
    2 3
    test
    """,
    """
    72
    128 256
    myonmyon
"""
]
ANSWER = ["6 test", "456 myonmyon"]


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


def solve(a, b, c, s):
    return f"{a + b + c} {s}"


def main():
    ih = InputHandler()
    a = int(ih.input())
    b, c = map(int, ih.input().split())
    s = ih.input()
    res = solve(a, b, c, s)
    print(res)


def test():
    for test_input, ans in zip(TEST_INPUT, ANSWER):
        ih = InputHandler(test_input, True)
        a = int(ih.input())
        b, c = map(int, ih.input().split())
        s = ih.input()
        res = solve(a, b, c, s)
        # print(res)
        assert str(res) == str(ans)


if __name__ == "__main__":
    test()
    main()
