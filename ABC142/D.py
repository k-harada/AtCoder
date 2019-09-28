def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


primes = [1] * (10 ** 6 + 1)
primes[0] = 0
primes[1] = 0
for p in range(10 ** 3 + 1):
    if primes[p]:
        for n in range(p * p, 10 ** 6 + 1, p):
            primes[n] = 0
prime_list = [p for p in range(10 ** 6 + 1) if primes[p] == 1]


def solve_d(a, b):
    d = gcd(a, b)
    res = 1
    for p in prime_list:
        if d % p == 0:
            res += 1
        while d % p == 0:
            d = d // p
    if d > 1:
        res += 1

    return res


def main():
    a, b = map(int, input().split())
    res = solve_d(a, b)
    print(res)


if __name__ == "__main__":
    main()