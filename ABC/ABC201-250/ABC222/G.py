def euler_phi(x):
    res = 1
    for p in range(2, x):
        if p * p > x:
            break
        r = 0
        while x % p == 0:
            r += 1
            x //= p
        if r > 0:
            res *= p ** r - p ** (r - 1)
    if x > 1:
        res *= x - 1
    return res


def solve(t, k_list):
    res = []
    for k in k_list:
        if k % 2 == 0:
            k //= 2
        k *= 9

        if k % 2 == 0 or k % 5 == 0:
            res.append(-1)
        else:
            r = k - 1
            m = euler_phi(k)
            for i in range(1, m + 1):
                if i * i > m:
                    break
                if m % i == 0:
                    p = i
                    if pow(10, p, k) == 1:
                        r = min(r, p)
                    p = m // i
                    if pow(10, p, k) == 1:
                        r = min(r, p)
            res.append(r)
    # print(res)
    return res


def main():
    t = int(input())
    k_list = [int(input()) for _ in range(t)]
    res = solve(t, k_list)
    for r in res:
        print(r)


def test():
    assert solve(4, [1, 7, 10, 999983]) == [1, 6, -1, 999982]


if __name__ == "__main__":
    test()
    main()
