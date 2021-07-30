def f(m):
    r = 1
    for c in str(m):
        r *= int(c)
    return r


def solve(n, b):

    m2, m3, m5, m7 = 0, 0, 0, 0
    x2, x3, x5, x7 = 1, 1, 1, 1

    while x2 <= n:
        x2 *= 2
        m2 += 1
    while x3 <= n:
        x3 *= 3
        m3 += 1
    while x5 <= n:
        x5 *= 5
        m5 += 1
    while x7 <= n:
        x7 *= 7
        m7 += 1

    fm_list = [0]
    for a2 in range(m2):
        f2 = 2 ** a2
        for a3 in range(m3):
            f23 = f2 * (3 ** a3)
            if f23 > n:
                break
            for a5 in range(m5):
                f235 = f23 * (5 ** a5)
                if f235 > n:
                    break
                for a7 in range(m7):
                    x = f235 * (7 ** a7)
                    if x > n:
                        break
                    fm_list.append(x)
    # print(fm_list)
    # print(len(fm_list))
    res = 0
    for fm in fm_list:
        m = fm + b
        if f(m) == fm and m != 0 and m <= n:
            res += 1

    return res


def main():
    n, b = map(int, input().split())
    res = solve(n, b)
    print(res)


def test():
    assert solve(999, 434) == 2
    assert solve(255, 15) == 2
    assert solve(9999999999, 1) == 0


if __name__ == "__main__":
    test()
    main()
