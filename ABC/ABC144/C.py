import math


def solve_c(c):
    res = c - 1
    d = math.floor(math.sqrt(c))
    for a in range(2, d + 1):
        if c % a == 0:
            res = (a - 1) + (c // a - 1)
    return res


def main():
    # input
    c = int(input())
    res = solve_c(c)
    print(res)


def test():
    assert solve_c(10) == 5
    assert solve_c(50) == 13
    assert solve_c(10000000019) == 10000000018


if __name__ == "__main__":
    test()
    main()
