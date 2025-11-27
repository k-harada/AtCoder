def solve(n, s):
    left_count_list = [0]
    left_count = 0
    del_flag = [0] * n
    for i in range(n):
        if s[i] == "(":
            # 0 -> 1
            left_count += 1
        elif s[i] == ")":
            left_count -= 1
        if left_count < 0:
            left_count = 0
            del_flag[i] = -1
        left_count_list.append(left_count)
    # print(left_count_list)

    cum_min = n + 1
    for i in range(n - 1, -1, -1):
        cum_min = min(cum_min, left_count_list[i + 1])
        if cum_min < left_count_list[i + 1]:
            del_flag[i] += 1
        elif cum_min == left_count_list[i + 1] and s[i] == ")":
            del_flag[i] += 1

    res_list = []
    for i in range(n):
        if del_flag[i] == 0:
            res_list.append(s[i])
    res = "".join(res_list)
    # print(res)

    return res


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
