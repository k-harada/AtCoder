def solve(n):
    prime_count = [0] * 101
    for i in range(1, n + 1):
        v = i
        for p in range(2, 101):
            while v % p == 0:
                prime_count[p] += 1
                v //= p
    # print(prime_count)
    res = 0
    # 5 * 5 * 3 = 75
    # 15 * 5
    # 25 * 3
    # 75
    c74 = 0
    c24 = 0
    c14 = 0
    c4 = 0
    c2 = 0
    for p in range(101):
        if prime_count[p] >= 74:
            c74 += 1
        if prime_count[p] >= 24:
            c24 += 1
        if prime_count[p] >= 14:
            c14 += 1
        if prime_count[p] >= 4:
            c4 += 1
        if prime_count[p] >= 2:
            c2 += 1
    # 5 * 5 * 3 = 75
    v1 = (c4 * (c4 - 1) // 2) * (c2 - 2)
    if v1 > 0:
        res += v1
    # 15 * 5
    v2 = c14 * (c4 - 1)
    if v2 > 0:
        res += v2
    # 25 * 3
    v3 = c24 * (c2 - 1)
    if v3 > 0:
        res += v3
    # 75
    v4 = c74
    if v4 > 0:
        res += v4
    return res


def main():
    n = int(input())
    res = solve(n)
    print(res)


def test():
    assert solve(9) == 0
    assert solve(10) == 1
    assert solve(100) == 543


if __name__ == "__main__":
    test()
    main()
