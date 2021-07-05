A, B, C, D = map(int, input().split())


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def lcm(x, y):
    return x * y // gcd(x, y)


E = lcm(C, D)

res_b = B // C + B // D - B // E
res_a = (A - 1) // C + (A - 1) // D - (A - 1) // E

print((B - res_b) - (A - 1 - res_a))
