import math


def solve(n):
    if n == 2:
        return 1
    res = 0

    # divisor of n - 1
    m = int(math.sqrt(n - 1))
    for i in range(2, m + 1):
        if (n - 1) % i == 0:
            res += 2
    if m * m == n - 1:
        res -= 1
    res += 1

    # divisor of n
    # n itself
    res += 1
    divisors = []
    m = int(math.sqrt(n))
    for i in range(2, m):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n // i)
    if n % m == 0 and m * m == n:
        divisors.append(m)
    elif n % m == 0:
        divisors.append(m)
        divisors.append(n // m)
    # print(divisors)
    for p in divisors:
        q = n // p
        while q % p == 0:
            q = q // p
        if q % p == 1:
            res += 1
    # print(res)
    return res


def solve_greed(n):
    for p in range(2, n + 1):
        m = n
        while m % p == 0:
            m = m // p
        if m % p == 1:
            print(p)


def main():
    n = int(input())
    res = solve(n)
    print(res)


def test():
    assert solve(6) == 3
    assert solve(3141) == 13
    assert solve(314159265358) == 9


if __name__ == "__main__":
    test()
    main()
