def solve(n, t_, s_list):
    res_ac = []
    m = len(t_)
    s1_list = []
    s2_list = []
    s3_list = []
    d_list = [0] * n

    for i in range(n):
        if len(s_list[i]) == m + 1:
            s1_list.append(i)
        elif len(s_list[i]) == m:
            s2_list.append(i)
        elif len(s_list[i]) == m - 1:
            s3_list.append(i)
        else:
            d_list[i] = 99
    # print(s1_list, s2_list, s3_list)
    for j in range(m):
        for i in s1_list:
            if j + d_list[i] >= len(s_list[i]):
                d_list[i] += 1
                continue
            while t_[j] != s_list[i][j + d_list[i]]:
                d_list[i] += 1
                if j + d_list[i] >= len(s_list[i]):
                    break

    for j in range(m):
        for i in s2_list:
            if t_[j] != s_list[i][j]:
                d_list[i] += 1

    for j in range(m):
        for i in s3_list:
            if j + d_list[i] >= len(s_list[i]):
                d_list[i] -= 1
            elif t_[j] != s_list[i][j + d_list[i]]:
                d_list[i] -= 1

    for i in range(n):
        if -1 <= d_list[i] <= 1:
            res_ac.append(str(i + 1))
    # print([str(len(res_ac)), " ".join(res_ac)])
    return [str(len(res_ac)), " ".join(res_ac)]


def main():
    n_, t_ = input().split()
    n = int(n_)
    s_list = [input() for _ in range(n)]
    res = solve(n, t_, s_list)
    for r in res:
        print(r)


def test():
    assert solve(5, "ababc", ["ababc", "babc", "abacbc", "abdbc", "abbac"]) == ["4", "1 2 3 4"]
    assert solve(1, "aoki", ["takahashi"]) == ["0", ""]
    assert solve(9, "atcoder", [
        "atoder",
        "atcode",
        "athqcoder",
        "atcoder",
        "tacoder",
        "jttcoder",
        "atoder",
        "atceoder",
        "atcoer"
    ]) == ["6", "1 2 4 7 8 9"]


if __name__ == "__main__":
    test()
    main()
