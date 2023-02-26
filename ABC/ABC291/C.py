from collections import defaultdict


def solve(n, s):
    xy_dict = defaultdict(int)
    x = 0
    y = 0
    xy_dict[x * 1000000 + y] += 1
    for c in s:
        if c == "R":
            x += 1
        elif c == "L":
            x -= 1
        elif c == "U":
            y += 1
        else:
            y -= 1
        if xy_dict[x * 1000000 + y] > 0:
            return "Yes"
        xy_dict[x * 1000000 + y] += 1
    return "No"


def main():
    n = int(input())
    s = input()
    res = solve(n, s)
    print(res)


def test():
    assert solve(5, "RLURU") == "Yes"
    assert solve(20, "URDDLLUUURRRDDDDLLLL") == "No"


if __name__ == "__main__":
    test()
    main()
