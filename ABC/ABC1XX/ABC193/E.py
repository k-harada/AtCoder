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


def solve(t, xypq_list):
    res_list = []
    for x, y, p, q in xypq_list:
        t_min = 10 ** 19
        g, a, b = ext_gcd(p + q, 2 * x + 2 * y)
        # print(g, a, b)
        for z in range(x - p - q + 1, x - p + y):
            if z % g != 0:
                continue
            t = ((p + q) // g) * (a * (z // g) % ((2 * x + 2 * y) // g)) * g + p
            # print(t, z)
            if z < x - p:
                t += x - p - z
            if t < t_min:
                t_min = t
                # print(t_min, z)
        if t_min < 10 ** 19:
            res_list.append(t_min)
        else:
            res_list.append("infinity")
    # print(res_list)
    return res_list


def main():
    t = int(input())
    xypq_list = [tuple(map(int, input().split())) for _ in range(t)]
    res_list = solve(t, xypq_list)
    for res in res_list:
        print(res)


def test():
    assert solve(3, [(5, 2, 7, 6), (1, 1, 3, 1), (999999999, 1, 1000000000, 1)]) == [20, "infinity", 1000000000999999999]


if __name__ == "__main__":
    test()
    main()
