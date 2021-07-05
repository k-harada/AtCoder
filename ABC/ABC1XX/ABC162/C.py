import math


def solve(k):
    res = 0
    for a in range(1, k + 1):
        for b in range(1, k + 1):
            d = math.gcd(a, b)
            for c in range(1, k + 1):
                res += math.gcd(c, d)
    return res


def main():
    k = int(input())
    res = solve(k)
    print(res)


def test():
    assert solve(2) == 9
    assert solve(200) == 10813692


if __name__ == "__main__":
    # test()
    main()
