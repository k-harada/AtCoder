import math


def solve(r):
    return math.pi * r * 2


def main():
    r = int(input())
    res = solve(r)
    print(res)


def test():
    assert abs(solve(1) - 6.28318530717958623200) < 0.01
    assert abs(solve(73) - 458.67252742410977361942) < 0.01


if __name__ == "__main__":
    test()
    main()
