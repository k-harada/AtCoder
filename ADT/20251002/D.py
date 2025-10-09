import math


def solve(a, b, d):
    theta = d / 180 * math.pi
    x = a * math.cos(theta) - b * math.sin(theta)
    y = a * math.sin(theta) + b * math.cos(theta)
    # print(x, y)
    return f"{x} {y}"


def main():
    a, b, d = map(int, input().split())
    res = solve(a, b, d)
    print(res)


def test():
    assert solve(2, 2, 180) == 0
    assert solve(5, 0, 120) == 0
    assert solve(0, 0, 11) == 0
    assert solve(15, 5, 360) == 0
    assert solve(-505, 191, 278) == 0


if __name__ == "__main__":
    # test()
    main()
