def solve(n, s, t):
    diff_list = [0] * n
    for i in range(n):
        if s[i] != t[i]:
            diff_list[i] = 1
    m = sum(diff_list)
    if m % 2 == 1:
        return "-1"
    res_list = []
    c_s = 0
    c_t = 0
    for i in range(n):
        if diff_list[i] == 0:
            res_list.append("0")
        else:
            if max(c_s, c_t) < m // 2:
                res_list.append("0")
                if s[i] == "0":
                    c_s += 1
                else:
                    c_t += 1
            else:
                if c_s == m // 2:
                    res_list.append(t[i])
                else:
                    res_list.append(s[i])
    return "".join(res_list)


def main():
    n = int(input())
    s = input()
    t = input()
    res = solve(n, s, t)
    print(res)


def test():
    assert solve(5, "00100", "10011") == "00001"
    assert solve(1, "0", "1") == "-1"


if __name__ == "__main__":
    test()
    main()
