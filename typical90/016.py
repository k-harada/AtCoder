def ext_gcd(a, b):
    """ extended Euclidean
    :param a:
    :param b:
    :return: g: gcd(a, b)
    x, y s.t. ax + by = g
    """
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = ext_gcd(b % a, a)
        return g, x - (b // a) * y, y


def solve(n, a, b, c):
    z = max([a, b, c])
    x = min([a, b, c])
    y = a + b + c - x - z

    res = 10000
    g, s, t = ext_gcd(x, y)
    # print(g, s, t, y // g, x // g)
    for k in range(n // z + 1):
        v = n - k * z
        q = v // y
        r = v % y
        if r % g != 0:
            continue
        i = s * (r // g)
        j = q + t * (r // g)
        # modify
        c_i = (i % (y // g) - i) // (y // g)
        i += c_i * (y // g)
        j -= c_i * (x // g)
        if i < 0 or j < 0:
            continue
        res = min(res, i + j + k)
        # print(i + j + k, i, j, k, i * x + j * y + k * z)
    # print(res)
    return res


def main():
    n = int(input())
    a, b, c = map(int, input().split())
    res = solve(n, a, b, c)
    print(res)


def test():
    assert solve(227, 21, 47, 56) == 5
    assert solve(9999, 1, 5, 10) == 1004
    assert solve(998244353, 314159, 265358, 97932) == 3333
    assert solve(100000000, 10001, 10002, 10003) == 9998


if __name__ == "__main__":
    test()
    main()
