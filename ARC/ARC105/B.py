def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def solve(n, a_list):
    res = a_list[0]
    for i in range(1, n):
        res = gcd(res, a_list[i])
    return res


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(3, [2, 6, 6]) == 2
    assert solve(15, [546, 3192, 1932, 630, 2100, 4116, 3906, 3234, 1302, 1806, 3528, 3780, 252, 1008, 588]) == 42


if __name__ == "__main__":
    test()
    main()
