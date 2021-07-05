def solve(n, s):

    r_list = [i for i in range(n) if s[i] == "R"]
    g_list = [i for i in range(n) if s[i] == "G"]
    # b_list = [i for i in range(n) if s[i] == "B"]
    b_dict = {i: 1 for i in range(n) if s[i] == "B"}

    res = len(r_list) * len(g_list) * len(b_dict.keys())
    for i in r_list:
        for j in g_list:
            # candidate
            m, n = min(i, j), max(i, j)
            if n + (n - m) in b_dict.keys():
                res -= 1
            if m - (n - m) in b_dict.keys():
                res -= 1
            if (n - m) % 2 == 0 and (n + m) // 2 in b_dict.keys():
                res -= 1

    return res


def main():
    n = int(input())
    s = input()
    res = solve(n, s)
    print(res)


def test():
    assert solve(4, "RRGB") == 1
    assert solve(39, "RBRBGRBGGBBRRGBBRRRBGGBRBGBRBGBRBBBGBBB") == 1800


if __name__ == "__main__":
    test()
    main()
