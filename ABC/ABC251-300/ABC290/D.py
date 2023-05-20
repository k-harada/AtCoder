def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def solve_sub(n, d, k):
    g = gcd(n, d)
    c = n // g
    q = (k - 1) // c
    r = (k - 1) % c
    res = (q + (r * d)) % n
    return res


def solve(t, case_list):
    return [solve_sub(n, d, k) for n, d, k in case_list]


def main():
    t = int(input())
    case_list = [tuple(map(int, input().split())) for _ in range(t)]
    res = solve(t, case_list)
    for r in res:
        print(r)


def test():
    assert solve(9, [
        (4, 2, 1), (4, 2, 2), (4, 2, 3), (4, 2, 4), (5, 8, 1), (5, 8, 2), (5, 8, 3), (5, 8, 4), (5, 8, 5)
    ]) == [0, 2, 1, 3, 0, 3, 1, 4, 2]


if __name__ == "__main__":
    test()
    main()
