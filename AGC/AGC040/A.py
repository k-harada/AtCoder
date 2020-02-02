def solve_a(s):
    n = len(s) + 1
    # from left
    left = [0] * n
    for i in range(1, n):
        if s[i - 1] == "<":
            left[i] = left[i - 1] + 1
    # from right
    right = [0] * n
    for i in range(n - 2, -1, -1):
        if s[i] == ">":
            right[i] = right[i + 1] + 1
    return sum([max(left[i], right[i]) for i in range(n)])


def main():
    s = list(input())
    res = solve_a(s)
    print(res)


def test():
    assert solve_a(list("<>>")) == 3
    assert solve_a(list("<>>><<><<<<<>>><")) == 28


if __name__ == "__main__":
    test()
    main()
