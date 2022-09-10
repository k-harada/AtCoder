def solve(n, p_list):
    d_list = [0] * n
    for i, p in enumerate(p_list):
        d_list[(p - i) % n] += 1

    if n % 2 == 0:
        m = n // 2
        r = 0
        for i in range(m):
            r += i * d_list[i]
        for i in range(m, n):
            r += (n - i) * d_list[i]
        res = r

        d = sum(d_list[:m])
        for i in range(n):
            r += 2 * d
            r -= n
            res = min(res, r)
            d -= d_list[(m - i - 1) % n]
            d += d_list[(- i - 1) % n]

    else:
        m = n // 2
        r = 0
        for i in range(m + 1):
            r += i * d_list[i]
        for i in range(m + 1, n):
            r += (n - i) * d_list[i]
        res = r

        d = 2 * sum(d_list[:m]) + d_list[m]
        for i in range(n):
            r += d
            r -= n
            res = min(res, r)
            d -= d_list[(m - i - 1) % n]
            d -= d_list[(m - i) % n]
            d += 2 * d_list[(- i - 1) % n]

    return res


def main():
    n = int(input())
    p_list = list(map(int, input().split()))
    res = solve(n, p_list)
    print(res)


def test():
    assert solve(4, [1, 2, 0, 3]) == 2
    assert solve(3, [0, 1, 2]) == 0
    assert solve(3, [0, 2, 1]) == 2
    assert solve(10, [3, 9, 6, 1, 7, 2, 8, 0, 5, 4]) == 20


def solve_greed(n, p_list):
    res = n * n
    for r in range(n):
        d = 0
        for i, p in enumerate(p_list):
            d += min((p - i - r) % n, (-(p - i - r)) % n)
        res = min(res, d)
    return res


def test_random():
    import random
    n = 11
    x = list(range(n))
    for _ in range(100):
        random.shuffle(x)
        print(n, x)
        assert solve_greed(n, x) == solve(n, x)


if __name__ == "__main__":
    test()
    # test_random()
    main()
