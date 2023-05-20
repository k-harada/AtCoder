def solve(a, x, m):
    pow_list = [1, a % m]
    ind = 1
    while ind <= x:
        pow_list.append((pow_list[-1] * pow_list[-1]) % m)
        ind *= 2
    sum_list = [1]
    for i in range(1, len(pow_list)):
        sum_list.append((sum_list[i - 1] * (1 + pow_list[i])) % m)
    # print(sum_list)
    res = 0
    seq = []
    y = x
    i = 0
    while y >= 2 ** i:
        if (y >> i) & 1:
            seq.append(i)
        i += 1
    # print(seq)
    z = x
    for p in reversed(seq):
        r = sum_list[p] * pow(a, z - 2 ** p, m)
        z -= 2 ** p
        res += r
        res %= m
    return res


def main():
    a, x, m = map(int, input().split())
    res = solve(a, x, m)
    print(res)


def test():
    assert solve(3, 4, 7) == 5
    assert solve(8, 10, 9) == 0
    assert solve(1000000000, 1000000000000, 998244353) == 919667211


if __name__ == "__main__":
    test()
    main()
