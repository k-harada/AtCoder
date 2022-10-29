import math


def solve_d(a, b, x):
    if 2 * x == a * a * b:
        return math.atan(b / a) * 180 / math.pi
    elif 2 * x > a * a * b:
        return math.atan((b - x / (a ** 2)) * 2 / a) * 180 / math.pi
    else:
        return 90 - math.atan((x / (a * b)) * 2 / b) * 180 / math.pi


def main():
    # input
    a, b, x = map(int, input().split())
    res = solve_d(a, b, x)
    print(res)


def test():
    assert abs(solve_d(2, 2, 4) - 45.0000000) <= 0.000001
    assert abs(solve_d(12, 21, 10) - 89.7834636934) <= 0.000001
    assert abs(solve_d(3, 1, 8) - 4.2363947991) <= 0.000001


if __name__ == "__main__":
    test()
    main()
