def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def solve(n, m, ac_list):
    ac_list_s = sorted(ac_list, key=lambda x: x[1])
    res = 0
    g = n
    left = n - 1
    for a, c in ac_list_s:
        g = gcd(g, a)
        res += (left - (g - 1)) * c
        left = g - 1
        if g == 1:
            break
    if g == 1:
        return res
    else:
        return -1


def main():
    n, m = map(int, input().split())
    ac_list = [tuple(map(int, input().split())) for _ in range(m)]
    res = solve(n, m, ac_list)
    print(res)


def test():
    assert solve(4, 2, [(2, 3), (3, 5)]) == 11
    assert solve(6, 1, [(3, 4)]) == -1


if __name__ == "__main__":
    test()
    main()
