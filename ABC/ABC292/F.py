import math


def solve_sub(x, b):
    tan = ((b / x) + math.sqrt(3)) / (math.sqrt(3) * b / x - 1)
    cos = 1 / math.sqrt(1 + tan ** 2)
    return x + math.sqrt(x * x + b * b) * cos


def solve(a, b):
    a, b = max(a, b), min(a, b)

    if a >= b * 2 / math.sqrt(3):
        return b * 2 / math.sqrt(3)
    left = b / 4
    right = b / math.sqrt(3)
    while left < right - 10 ** (-14) and left * (1 + 10 ** (-14)) < right:
        mid = (left + right) / 2
        # print(left, right, solve_sub(mid, b))
        if solve_sub(mid, b) >= a:
            right = mid
        else:
            left = mid
    x = (left + right) / 2
    res = math.sqrt(x * x + b * b)
    # print(res)
    return res


def main():
    a, b = map(int, input().split())
    res = solve(a, b)
    print(res)


def test():
    assert abs(solve(1, 1) - (math.sqrt(6) - math.sqrt(2))) < 10 ** (-9)


if __name__ == "__main__":
    test()
    main()
