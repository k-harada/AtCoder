import sys


TEST_INPUT = [
    """
    5 3
    1 2 2 4 5
    """,
    """
    4 1
    6 6 6 6
    """,
    """
    10 4
    17 13 13 12 15 20 10 13 17 11
    """
]
ANSWER = [
    "7.0",
    "3.5",
    "32.0"
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


def solve(n, k, p_list):
    res = sum(p_list[:k])
    res_temp = res
    for i in range(n - k):
        res_temp -= p_list[i]
        res_temp += p_list[i + k]
        if res_temp > res:
            res = res_temp
    return (res + k) / 2


def input_and_solve(ih):
    n, k = map(int, ih.input().split())
    p_list = list(map(int, ih.input().split()))
    res = solve(n, k, p_list)
    return res


def main():
    ih = InputHandler()
    res = input_and_solve(ih)
    print(res)


def test():
    for test_input, ans in zip(TEST_INPUT, ANSWER):
        ih = InputHandler(test_input, True)
        res = input_and_solve(ih)
        assert abs(float(res) - float(ans)) < 0.00000001


if __name__ == "__main__":
    test()
    main()
