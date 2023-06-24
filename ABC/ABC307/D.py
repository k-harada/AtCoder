def solve(n, s):
    del_flg = [0] * n
    l_cnt = 0
    left_start = 0

    for i in range(n):
        if s[i] == ")":
            l_cnt -= 1
            if l_cnt == 0:
                for j in range(left_start, i + 1):
                    del_flg[j] = 1
                left_start = i
            elif l_cnt < 0:
                l_cnt = 0
                left_start = i
        elif s[i] == "(":
            l_cnt += 1
            if l_cnt == 1:
                left_start = i

    r_cnt = 0
    right_start = n - 1
    for i in range(n - 1, -1, -1):
        if s[i] == "(":
            r_cnt -= 1
            if r_cnt == 0:
                for j in range(i, right_start + 1):
                    del_flg[j] = 1
                right_start = i
            elif r_cnt < 0:
                r_cnt = 0
                right_start = i
        elif s[i] == ")":
            r_cnt += 1
            if r_cnt == 1:
                right_start = i

    t = "".join([s[i] for i in range(n) if del_flg[i] == 0])
    # print(t)
    return t


def main():
    n = int(input())
    s = input()
    res = solve(n, s)
    print(res)


def test():
    assert solve(8, "a(b(d))c") == "ac"
    assert solve(5, "a(b)(") == "a("
    assert solve(2, "()") == ""
    assert solve(6, ")))(((") == ")))((("


if __name__ == "__main__":
    test()
    main()
