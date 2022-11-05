from itertools import product


def solve(n):
    m = len(str(n))
    if m <= 2:
        return 0
    res = 0
    # m - 1ケタ以下を全部採用
    for i in range(3, m):
        res += 3 ** i - 3 * (2 ** i - 2) - 3
    # print(res)
    # m桁を全列挙
    for p in product(["3", "5", "7"], repeat=m):
        if ("3" not in p) or ("5" not in p) or ("7" not in p):
            continue
        v = int("".join(p))
        if v <= n:
            res += 1

    return res


def main():
    n = int(input())
    res = solve(n)
    print(res)


def test():
    assert solve(575) == 4
    assert solve(3600) == 13
    assert solve(999999999) == 26484


if __name__ == "__main__":
    test()
    main()
