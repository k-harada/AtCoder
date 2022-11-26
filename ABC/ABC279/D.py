import math


def solve(a, b):
    res = 10 ** 18
    t_min = math.pow(a / (2 * b), 2 / 3) - 1
    t_min_int = int(t_min)
    for t in range(max(0, t_min_int - 1), t_min_int + 2):
        r = b * t + (a / math.sqrt(t + 1))
        res = min(res, r)
    # print(res)
    return res


def main():
    a, b = map(int, input().split())
    res = solve(a, b)
    print(res)


def test():
    assert abs(solve(10, 1) - 7.7735026919) < 0.0000001
    assert abs(solve(5, 10) - 5.0000000000) < 0.0000001
    assert abs(solve(1000000000000000000, 100) - 8772053214538.5976562500) < 0.0000001


if __name__ == "__main__":
    test()
    main()
