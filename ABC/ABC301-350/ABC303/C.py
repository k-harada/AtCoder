from collections import defaultdict


def solve(n, m, h, k, s, xy_list):
    potions = defaultdict(int)
    for x, y in xy_list:
        z = x * 1000000 + y
        potions[z] = 1

    takahashi = h
    x = 0
    y = 0
    for c in s:
        if c == "R":
            x += 1
        elif c == "L":
            x -= 1
        elif c == "U":
            y += 1
        else:
            y -= 1
        takahashi -= 1
        if takahashi < 0:
            return "No"
        z = x * 1000000 + y
        if potions[z] == 1 and takahashi < k:
            potions[z] = 0
            takahashi = k
    return "Yes"


def main():
    n, m, h, k = map(int, input().split())
    s = input()
    xy_list = [tuple(map(int, input().split())) for _ in range(m)]
    res = solve(n, m, h, k, s, xy_list)
    print(res)


def test():
    assert solve(4, 2, 3, 1, "RUDL", [(-1, -1), (1, 0)]) == "Yes"
    assert solve(5, 2, 1, 5, "LDRLD", [(0, 0), (-1, -1)]) == "No"


if __name__ == "__main__":
    test()
    main()
