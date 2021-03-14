MOD = 998244353


def solve(h, w, h1, w1, h2, w2):
    up = min(h1, h2) - 1
    down = h - max(h1, h2)
    left = min(w1, w2) - 1
    right = w - max(w1, w2)
    center = h + w - 2 - (up + down + left + right)

    mod_inv = [0] * (h + w + 1)
    for i in range(1, h + w + 1):
        mod_inv[i] = pow(i, MOD - 2, MOD)

    res = 0
    for i in range(up):
        res += mod_inv[i + 1 + center]
    for i in range(down):
        res += mod_inv[i + 1 + center]
    for i in range(left):
        res += mod_inv[i + 1 + center]
    for i in range(right):
        res += mod_inv[i + 1 + center]
    return (res + 1) % MOD


def main():
    h, w = map(int, input().split())
    h1, w1, h2, w2 = map(int, input().split())
    res = solve(h, w, h1, w1, h2, w2)
    print(res)


def test():
    assert solve(2, 3, 2, 2, 1, 1) == 332748119
    assert solve(1, 5, 1, 2, 1, 3) == 332748120
    assert solve(2, 1, 2, 1, 1, 1) == 1
    assert solve(10, 10, 3, 4, 5, 6) == 831078040


if __name__ == "__main__":
    test()
    main()
