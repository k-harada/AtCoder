from collections import defaultdict


def solve(k):
    primes = [1] * (10 ** 6 + 1)
    primes[0] = 0
    primes[1] = 0
    for p in range(2, 1005):
        if primes[p]:
            for r in range(p * p, 10 ** 6 + 1, p):
                primes[r] = 0
    prime_list = [p for p in range(10 ** 6 + 1) if primes[p]]
    # print(prime_list)
    m = k
    counter = defaultdict(int)
    for p in prime_list:
        while m % p == 0:
            m //= p
            counter[p] += 1
    if m > 1:
        counter[m] = 1
    res = 1
    for p in counter.keys():
        c = counter[p]
        # 素数の山を計算
        p_list = [0, 1]
        while p_list[-1] < c:
            p_list.append(p_list[-1] * p + 1)
        r = 0
        i = len(p_list) - 1
        while i > 0:
            while c >= p_list[i]:
                r += p ** i
                c -= p_list[i]
            i -= 1
        res = max(res, r)
    return res


def main():
    k = int(input())
    res = solve(k)
    print(res)


def test():
    assert solve(30) == 5
    assert solve(123456789011) == 123456789011
    assert solve(280) == 7


if __name__ == "__main__":
    test()
    main()
