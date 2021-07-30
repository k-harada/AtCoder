import math


def solve(t, l, x, y, q, e_list):
    res = []

    x_1 = 0
    z = 0

    for e in e_list:
        y_1 = - (l / 2) * math.sin(2 * math.pi * e / t)
        z_1 = (l / 2) - (l / 2) * math.cos(2 * math.pi * e / t)
        d_1 = math.sqrt((x - x_1) ** 2 + (y - y_1) ** 2)
        res.append(math.atan(z_1 / d_1) * 180 / math.pi)
    # print(res)
    return res


def main():
    t = int(input())
    l, x, y = map(int, input().split())
    q = int(input())
    e_list = [int(input()) for _ in range(q)]
    res = solve(t, l, x, y, q, e_list)
    for r in res:
        print(r)


def test():
    print(solve(4, 2, 1, 1, 4, [0, 1, 2, 3]))
    print(solve(5121, 312000000, 4123, 3314, 6, [123, 12, 445, 4114, 42, 1233]))


if __name__ == "__main__":
    # test()
    main()
