MOD = 998244353
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def solve_sub(n, s):
    res = 0
    for i, c in enumerate(s):
        j = ALPHABET.index(c)
        freedom = ((n - 2 * (i + 1)) + 1) // 2
        # print(i, j, freedom)
        res += j * pow(26, freedom, MOD)

        # last
        if (i + 1) * 2 == n:
            if s[:(i + 1)] + "".join(list(reversed(s[:(i + 1)]))) <= s:
                res += 1
            break
        elif 2 * i + 1 == n:
            if s[:i] + s[i] + "".join(list(reversed(s[:i]))) <= s:
                res += 1
            break
    res %= MOD
    # print(res)
    return res


def solve(t, ns_list):
    return [solve_sub(n, s) for n, s in ns_list]


def main():
    t = int(input())
    ns_list = []
    for _ in range(t):
        n = int(input())
        s = input()
        ns_list.append((n, s))
    res = solve(t, ns_list)
    for r in res:
        print(r)


def test():
    assert solve(5, [
        (3, "AXA"), (6, "ABCZAZ"), (30, "QWERTYUIOPASDFGHJKLZXCVBNMQWER"),
        (28, "JVIISNEOXHSNEAAENSHXOENSIIVJ"), (31, "KVOHEEMSOZZASHENDIGOJRTJVMVSDWW")
    ]) == [24, 29, 212370247, 36523399, 231364016]


if __name__ == "__main__":
    test()
    main()
