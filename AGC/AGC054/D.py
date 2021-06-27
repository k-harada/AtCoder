from collections import deque


def solve(s):

    left_queue = deque()
    right_queue = deque()

    # solve ()
    for i, c in enumerate(s):
        if c == "(":
            left_queue.append(i)
        elif c == ")":
            right_queue.append(i)

    return 0


def main():
    s = input()
    res = solve(s)
    print(res)


def test():
    assert solve() == 0
    assert solve() == 0
    assert solve() == 0


if __name__ == "__main__":
    test()
    main()
