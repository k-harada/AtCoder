LARGE = 10 ** 9 + 7


def solve(n, a_list):

    # inverse
    res = 0
    for i in range(n):
        res += pow(a_list[i], LARGE - 2, LARGE)
        res %= LARGE

    # primes
    p_candidate_list = [1] * 10 ** 3
    p_candidate_list[0] = 0
    p_candidate_list[1] = 0
    for p in range(2, 10 ** 3):
        if p_candidate_list[p]:
            for q in range(p * p, 10 ** 3, p):
                p_candidate_list[q] = 0
    primes_1000 = [p for p in range(1000) if p_candidate_list[p]]

    lcm = 1
    for p in primes_1000:
        r_max = 0
        for i in range(n):
            r = 0
            while a_list[i] % p == 0:
                r += 1
                a_list[i] = a_list[i] // p
            r_max = max(r_max, r)
        lcm *= pow(int(p), r_max, LARGE)
        lcm %= LARGE

    for q in set(a_list):
        lcm *= q
        lcm %= LARGE

    return res * lcm % LARGE


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(3, [2, 3, 4]) == 13
    assert solve(5, [12, 12, 12, 12, 12]) == 5
    assert solve(3, [1000000, 999999, 999998]) == 996989508


if __name__ == "__main__":
    test()
    main()
