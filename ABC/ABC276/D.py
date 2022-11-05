def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def solve(n, a_list):
    g = a_list[0]
    for i in range(1, n):
        g = gcd(g, a_list[i])
    res = 0
    for i in range(n):
        b = a_list[i] // g
        while b % 2 == 0:
            res += 1
            b //= 2
        while b % 3 == 0:
            res += 1
            b //= 3
        if b > 1:
            return -1
    return res


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(3, [1, 4, 3]) == 3
    assert solve(3, [2, 7, 6]) == -1
    assert solve(6, [1, 1, 1, 1, 1, 1]) == 0


if __name__ == "__main__":
    test()
    main()
