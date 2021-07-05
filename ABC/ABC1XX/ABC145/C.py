import math


def solve(n, x_list, y_list):
    d_total = 0.0
    for i in range(n - 1):
        for j in range(i + 1, n):
            d_total += math.sqrt((x_list[i] - x_list[j]) ** 2 + (y_list[i] - y_list[j]) ** 2)
    return d_total * 2 / n


def main():
    n = int(input())
    x_list = [0] * n
    y_list = [0] * n
    for i in range(n):
        x, y = map(int, input().split())
        x_list[i] = x
        y_list[i] = y
    res = solve(n, x_list, y_list)
    print(res)


def test():
    assert abs(solve(3, [0, 1, 0], [0, 0, 1]) - 2.2761423749) < 0.000001
    assert abs(solve(2, [-879, -866], [981, 890]) - 91.9238815543) < 0.000001
    assert abs(solve(
        8, [-406, 512, 494, -955, 128, -986, 763, 449], [10, 859, 362, -475, 553, -885, 77, 310]
    ) - 7641.9817824387) < 0.000001


if __name__ == "__main__":
    test()
    main()
