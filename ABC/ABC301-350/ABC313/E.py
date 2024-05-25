MOD = 998244353


def solve(n, s):
    for i in range(n - 1):
        if s[i] != "1" and s[i + 1] != "1":
            return -1
    ones = []
    counts = []
    one_count = 0
    for i in range(n):
        if s[i] == "1":
            one_count += 1
        else:
            ones.append(one_count)
            counts.append(int(s[i]))
            one_count = 0

    res = one_count
    n_dup = one_count
    # print(ones)
    # print(counts)
    while len(counts):
        p = counts.pop()
        c = ones.pop()
        res += 1
        n_dup += 1
        if c > 0:
            res += n_dup * (p - 1) + c
            n_dup += n_dup * (p - 1) + c
        res %= MOD
        n_dup %= MOD
        # print(p, c, res, n_dup)
    return res - 1


def main():
    n = int(input())
    s = input()
    res = solve(n, s)
    print(res)


def test():
    assert solve(3, "313") == 4
    assert solve(9, "123456789") == -1
    assert solve(2, "11") == 1


if __name__ == "__main__":
    test()
    main()
