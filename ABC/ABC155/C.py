import sys
from collections import Counter

TEST_INPUT = [
    """
    7
    beat
    vet
    beet
    bed
    vet
    bet
    beet
    """,
    """
    8
    buffalo
    buffalo
    buffalo
    buffalo
    buffalo
    buffalo
    buffalo
    buffalo
    """,
    """
    7
    bass
    bass
    kick
    kick
    bass
    kick
    kick
    """,
    """
    4
    ushi
    tapu
    nichia
    kun
    """
]
ANSWER = [
    "['beet', 'vet']",
    "['buffalo']",
    "['kick']",
    "['kun', 'nichia', 'tapu', 'ushi']"
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


def solve(n, s_list):
    c = Counter(s_list)
    m = max(c.values())
    res_list = [k for k in c.keys() if c[k] == m]
    return list(sorted(res_list))


def input_and_solve(ih):
    n = int(ih.input())
    s_list = [ih.input() for _ in range(n)]
    res = solve(n, s_list)
    return res


def main():
    ih = InputHandler()
    res = input_and_solve(ih)
    for r in res:
        print(r)


def test():
    for test_input, ans in zip(TEST_INPUT, ANSWER):
        ih = InputHandler(test_input, True)
        res = input_and_solve(ih)
        assert str(res) == str(ans)


if __name__ == "__main__":
    test()
    main()
