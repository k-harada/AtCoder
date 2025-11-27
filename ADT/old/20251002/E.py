import math


def solve(d):
    res = d
    dd = int(math.sqrt(d))
    for x in range(dd + 1):
        xx = x ** 2
        yy = d - xx
        y1 = int(math.sqrt(yy))
        r = abs(d - xx - y1 ** 2)
        res = min(res, r)
        y2 = int(math.sqrt(yy)) + 1
        r = abs(d - xx - y2 ** 2)
        res = min(res, r)
        # print(x, y1, y2, r, res)

    return res


def main():
    d = int(input())
    res = solve(d)
    print(res)


def test():
    assert solve(21) == 1
    assert solve(998244353) == 0
    assert solve(264428617) == 32


if __name__ == "__main__":
    test()
    main()
