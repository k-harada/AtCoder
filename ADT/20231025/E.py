from collections import defaultdict


def solve(n, x, a_list):
    d = defaultdict(int)
    for a in a_list:
        d[a + x] = 1
    for a in a_list:
        if d[a] == 1:
            return "Yes"
    return "No"


def main():
    n, x = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, x, a_list)
    print(res)


def test():
    assert solve(6, 5, [3, 1, 4, 1, 5, 9]) == "Yes"
    assert solve(6, -4, [-2, -7, -1, -8, -2, -8]) == "No"
    assert solve(2, 0, [141421356, 17320508]) == "Yes"


if __name__ == "__main__":
    test()
    main()
