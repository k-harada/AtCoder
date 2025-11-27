def solve(n, m, a_list):
    r = 0
    s = 0
    for i in range(m):
        r += (i + 1) * a_list[i]
        s += a_list[i]
    res = r
    for i in range(m, n):
        r -= s
        r += m * a_list[i]
        s -= a_list[i - m]
        s += a_list[i]
        if r > res:
            res = r
    return res


def main():
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, m, a_list)
    print(res)


def test():
    assert solve(4, 2, [5, 4, -1, 8]) == 15
    assert solve(10, 4, [-3, 1, -4, 1, -5, 9, -2, 6, -5, 3]) == 31
    assert solve(2, 2, [-1, -1]) == -3


if __name__ == "__main__":
    test()
    main()
