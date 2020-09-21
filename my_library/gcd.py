def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def lcm(x, y):
    return x * y // gcd(x, y)


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


