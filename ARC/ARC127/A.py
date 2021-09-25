def solve(n):
    m = 1
    res = 0
    ones = [0]
    for _ in range(20):
        ones.append(ones[-1] * 10 + 1)
    ones_cum = []
    s = 0
    for v in ones:
        s += v
        ones_cum.append(s)
    k = 0
    while 10 * m <= n:
        m *= 10
        k += 1
    res = ones_cum[k]
    # print(ones_cum)
    # print(m, res)
    bar = m - 1
    for i, c in enumerate(str(n)):
        if c == "1":
            res += n - bar
            bar += m // (10 ** (i + 1))
            k -= 1
        elif c == "0":
            break
        else:
            res += ones[k + 1]
            break
    # print(res)
    return res


def main():
    n = int(input())
    res = solve(n)
    print(res)


def test():
    assert solve(11) == 4
    assert solve(120) == 44
    assert solve(987654321) == 123456789


if __name__ == "__main__":
    test()
    main()
