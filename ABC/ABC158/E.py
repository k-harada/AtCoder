def solve(n, p, s):
    res = 0
    if p == 2 or p == 5:
        for i in range(n):
            if int(s[i]) % p == 0:
                res += i + 1
        return res

    mod_count = [0] * p
    temp = 0
    pow_10_i_p = [0] * n
    pow_10_i_p[0] = 1
    for i in range(1, n):
        pow_10_i_p[i] = pow_10_i_p[i - 1] * 10 % p
    for i in range(n):
        temp = (temp + pow_10_i_p[i] * int(s[-(i + 1)])) % p
        mod_count[temp] += 1
    res += mod_count[0]
    for i in range(p):
        res += mod_count[i] * (mod_count[i] - 1) // 2
    return res


def main():
    n, p = map(int, input().split())
    s = input()
    res = solve(n, p, s)
    print(res)


def test():
    assert solve(4, 3, "3543") == 6
    assert solve(4, 2, "2020") == 10
    assert solve(20, 11, "33883322005544116655") == 68


if __name__ == "__main__":
    test()
    main()
