import sys


TEST_INPUT = [
    """
    5
    6 7 9 10 31
    """,
    """
    3
    28 27 24
    """
]
ANSWER = [
    "APPROVED",
    "DENIED"
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


def solve(n, a_list):
    for a in a_list:
        if a % 2 == 0 and a % 3 != 0 and a % 5 != 0:
            return "DENIED"
    return "APPROVED"


def input_and_solve(ih):
    n = int(ih.input())
    a_list = list(map(int, ih.input().split()))
    res = solve(n, a_list)
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
