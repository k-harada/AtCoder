def solve(s):
    mod = 10 ** 9 + 7
    if s <= 2:
        return 0
    elif s <= 5:
        return 1
    res = [0] * (s + 1)
    res_3 = 0
    for i in range(3, s + 1):
        res[i] = 1 + res_3
        res_3 += res[i - 2]
        res_3 %= mod
    return res[s] % mod


def main():
    s = int(input())
    res = solve(s)
    print(res)


def test():
    assert solve(7) == 3
    assert solve(2) == 0
    assert solve(1729) == 294867501


if __name__ == "__main__":
    test()
    main()
