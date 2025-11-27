def solve(n, s):
    left = []
    right_rev = []
    for i, c in enumerate(s):
        if c == "L":
            right_rev.append(i)
        else:
            left.append(i)
    res = left + [n] + list(reversed(right_rev))
    # print(res)
    return " ".join(map(str, res))


def main():
    n = int(input())
    s = input()
    res = solve(n, s)
    print(res)


def test():
    assert solve(5, "LRRLR") == "1 2 4 5 3 0"
    assert solve(7, "LLLLLLL") == "7 6 5 4 3 2 1 0"


if __name__ == "__main__":
    test()
    main()
