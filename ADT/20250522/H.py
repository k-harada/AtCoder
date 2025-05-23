ALPHABET = "abcdefghijklmnopqrstuvwxyz".upper()
MOD = 998244353


def solve_sub(n, s):
    # print(n, s)
    res = 0
    m = (n + 1) // 2
    for i in range(m):
        c = s[i]
        res += (ALPHABET.index(c) * pow(26, m - i - 1, MOD)) % MOD
        res %= MOD
    # last
    if n % 2 == 0:
        s_last = "".join(list(s[:m]) + list(reversed(list(s[:m]))))
    else:
        s_last = "".join(list(s[:m]) + list(reversed(list(s[:m - 1]))))
    # print(s_last)
    if s_last <= s:
        res += 1
        res %= MOD
    return res


def solve(n, case_list):
    res = [solve_sub(m, s) for m, s in case_list]
    # print(res)
    return res


def main():
    n = int(input())
    case_list = []
    for _ in range(n):
        m = int(input())
        s = input()
        case_list.append((m, s))
    res = solve(n, case_list)
    for r in res:
        print(r)


def test():
    assert solve(5, [
        (3, "AXA"),
        (6, "ABCZAZ"),
        (30, "QWERTYUIOPASDFGHJKLZXCVBNMQWER"),
        (28, "JVIISNEOXHSNEAAENSHXOENSIIVJ"),
        (31, "KVOHEEMSOZZASHENDIGOJRTJVMVSDWW"),
    ]) == [24, 29, 212370247, 36523399, 231364016]


if __name__ == "__main__":
    test()
    main()
