import sys


TEST_INPUT = [
    """
    100
    1
    """,
    """
    25
    2
    """,
    """
    314159
    2
    """,
    """
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    3
    """
]
ANSWER = [
    "19",
    "14",
    "937",
    "117879300"
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


def solve(n, k):
    res = 0
    le = len(n) - 1

    # smaller order
    if k == 1 and le >= 1:
        res += 9 * le
    if k == 2 and le >= 2:
        res += 9 * 9 * le * (le - 1) // 2
    if k == 3 and le >= 3:
        res += 9 * 9 * 9 * le * (le - 1) * (le - 2) // 6

    # bxxxxx
    if k == 1:
        res += int(n[0]) - 1
    if k == 2:
        res += (int(n[0]) - 1) * (9 * le)
    if k == 3:
        res += (int(n[0]) - 1) * (9 * 9 * le * (le - 1) // 2)

    # axxxxx
    if k == 1:
        res += 1
    if k == 2:
        # first nonzero
        for i in range(1, le + 1):
            if int(n[i]) > 0:
                res += int(n[i])
                res += 9 * (le - i)
                break
    if k == 3:
        j = 0
        # first nonzero
        for i in range(1, le + 1):
            if int(n[i]) > 0:
                res += (int(n[i]) - 1) * 9 * (le - i)
                res += 9 * 9 * ((le - i) * (le - i - 1) // 2)
                j = i
                break
        # second nonzero
        for i in range(j + 1, le + 1):
            if int(n[i]) > 0:
                res += int(n[i])
                res += 9 * (le - i)
                break
    return res


def input_and_solve(ih):
    n = ih.input()
    k = int(ih.input())
    res = solve(n, k)
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
