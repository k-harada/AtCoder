def solve(n, a_list):
    res = 2 ** 30
    for i in range(2 ** n - 1):
        r1 = a_list[0]
        r2 = 0
        for j, a in enumerate(a_list[1:]):
            if i >> j & 1:
                r1 |= a
            else:
                r2 ^= r1
                r1 = a
        r = r2 ^ r1
        res = min(res, r)
    return res


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(3, [1, 5, 7]) == 2
    assert solve(3, [10, 10, 10]) == 0
    assert solve(4, [1, 3, 3, 1]) == 0


if __name__ == "__main__":
    test()
    main()
