MOD = 998244353


def solve(n, d):
    res = 0
    for i in range(d + 1):
        # i times up
        depth_min = i
        depth_max = min(n - 1, n - 1 - (d - 2 * i))
        if depth_max < depth_min:
            continue
        if i == 0:
            vol = pow(2, depth_max + 1, MOD) - 1
        else:
            vol = pow(2, depth_max + 1, MOD) - pow(2, depth_min, MOD)
        if i == d:
            res += vol
        elif i == 0:
            res += vol * pow(2, d, MOD)
        else:
            res += vol * pow(2, d - i - 1, MOD)
        res %= MOD
        # print(res)
    # print(res)
    return res


def main():
    n, d = map(int, input().split())
    res = solve(n, d)
    print(res)


def test():
    assert solve(3, 2) == 14
    assert solve(14142, 17320) == 11284501


if __name__ == "__main__":
    test()
    main()
