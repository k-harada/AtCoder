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


def solve_sub(n, s, k):
    g, x, y = ext_gcd(n, k)
    if s % g != 0:
        return -1
    res = - (s // g) * y
    res %= n // g
    return res


def solve(t, query_list):
    res_list = []
    for n, s, k in query_list:
        res_list.append(solve_sub(n, s, k))
    return res_list


def main():
    t = int(input())
    query_list = [tuple(map(int, input().split())) for _ in range(t)]
    res_list = solve(t, query_list)
    for res in res_list:
        print(res)


def test():
    assert solve(4, [(10, 4, 3), (1000, 11, 2), (998244353, 897581057, 595591169), (10000, 6, 14)]) == [2, -1, 249561088, 3571]


if __name__ == "__main__":
    test()
    main()
