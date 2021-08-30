MOD = 998244353


def solve(n):
    for sq in range(n + 1):
        if (sq + 1) ** 2 > n:
            break
    # print(sq)
    res = 0
    for i in range(1, sq + 1):
        if i % 2 == 1:
            max_odd = n // i
            res += (max_odd - (i - 2)) // 2
        else:
            max_even = n // i
            res += (max_even - (i - 2)) // 2
        # print(i, res)
        res %= MOD
    return res


def main():
    n = int(input())
    res = solve(n)
    print(res)


def test():
    assert solve(3) == 2
    assert solve(10) == 8
    assert solve(10000000000) == 52583544


if __name__ == "__main__":
    test()
    main()
