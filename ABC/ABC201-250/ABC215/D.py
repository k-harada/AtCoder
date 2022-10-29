def solve(n, m, a_list):
    primes = [1] * (10 ** 5 + 1)
    primes[0] = 0
    primes[1] = 0
    for p in range(2, 10 ** 5 + 1):
        if primes[p]:
            for q in range(p * p, 10 ** 5 + 1, p):
                primes[q] = 0
    q_list = [0] * (10 ** 5 + 1)
    for a in a_list:
        for i in range(1, a + 1):
            if i * i > a:
                break
            if a % i == 0:
                q_list[i] = 1
                q_list[a // i] = 1

    res = [1] * (m + 1)
    res[0] = 0
    for q in range(1, m + 1):
        if primes[q] and q_list[q]:
            for r in range(q, m + 1, q):
                res[r] = 0
    res_list = [sum(res)] + [r for r in range(m + 1) if res[r]]
    return res_list


def main():
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, m, a_list)
    for r in res:
        print(r)


def test():
    assert solve(3, 12, [6, 1, 5]) == [3, 1, 7, 11]
    _ = solve(100000, 100000, [100000] * 100000)


if __name__ == "__main__":
    test()
    main()
