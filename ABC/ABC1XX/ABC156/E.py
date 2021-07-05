LARGE = 10 ** 9 + 7


def solve(n, k):
    # singular cases
    if k == 0:
        return 1
    elif k == 1:
        return n * (n - 1)

    # pow
    pow_mod = [1] * (n + 1)
    for i in range(n):
        pow_mod[i + 1] = pow_mod[i] * (i + 1) % LARGE
    pow_mod_inv = [1] * (n + 1)
    pow_mod_inv[-1] = pow(pow_mod[-1], LARGE - 2, LARGE)
    for i in range(n - 1, 0, -1):
        pow_mod_inv[i] = pow_mod_inv[i + 1] * (i + 1) % LARGE

    res = 0
    for i in range(min(k, n - 1) + 1):
        # find where to set 0
        pick_zeros = pow_mod[n] * pow_mod_inv[i] * pow_mod_inv[n - i] % LARGE
        # how to assign ones
        assign_ones = pow_mod[n - 1] * pow_mod_inv[i] * pow_mod_inv[n - 1 - i] % LARGE
        res += pick_zeros * assign_ones
        res %= LARGE
    return res


def main():
    n, k = map(int, input().split())
    res = solve(n, k)
    print(res)


def test():
    assert solve(3, 2) == 10
    assert solve(200000, 1000000000) == 607923868
    assert solve(15, 6) == 22583772


if __name__ == "__main__":
    test()
    main()
