from bisect import bisect_left, bisect_right

def solve(n, t, s_list):

    m = len(t)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    len_s_list = [len(s) for s in s_list]
    s_all = "".join(s_list)
    q = len(s_all)
    res_array = [[0] * 26 for _ in range(q + 1)]
    for i, c in enumerate(s_all):
        for r in range(26):
            res_array[i + 1][r] = res_array[i][r]
        res_array[i + 1][alphabet.index(c)] += 1

    cum_len_s = [0]
    for a in len_s_list:
        cum_len_s.append(cum_len_s[-1] + a)

    i = 0
    j = 0
    k = 0
    res_a = [0] * n

    while k < n:
        c = alphabet.index(t[j])
        left = i
        right = cum_len_s[k + 1]
        if res_array[left][c] == res_array[right][c]:
            i = right
            j = 0
            k += 1
            continue
        while left + 1 < right:
            mid = (left + right) // 2
            if res_array[left][c] == res_array[mid][c]:
                left = mid
            else:
                right = mid
        i = right
        j += 1
        res_a[k] = j

        if j == m:
            i = cum_len_s[k + 1]
            j = 0
            k += 1

    s_all = "".join(["".join(list(reversed(s))) for s in s_list])
    q = len(s_all)
    t_rev = "".join(list(reversed(t)))
    res_array = [[0] * 26 for _ in range(q + 1)]
    for i, c in enumerate(s_all):
        for r in range(26):
            res_array[i + 1][r] = res_array[i][r]
        res_array[i + 1][alphabet.index(c)] += 1

    cum_len_s = [0]
    for a in len_s_list:
        cum_len_s.append(cum_len_s[-1] + a)
    i = 0
    j = 0
    k = 0
    res_b = [0] * n

    while k < n:
        c = alphabet.index(t_rev[j])
        left = i
        right = cum_len_s[k + 1]
        if res_array[left][c] == res_array[right][c]:
            i = right
            j = 0
            k += 1
            continue
        while left + 1 < right:
            mid = (left + right) // 2
            if res_array[left][c] == res_array[mid][c]:
                left = mid
            else:
                right = mid
        i = right
        j += 1
        res_b[k] = j

        if j == m:
            i = cum_len_s[k + 1]
            j = 0
            k += 1
    # print(res_a)
    # print(res_b)
    count_b = [0] * (len(t) + 1)
    for r in res_b:
        count_b[r] += 1
    count_b_cum = [0] * (len(t) + 1)
    count_b_cum[0] = count_b[-1]
    for i in range(1, len(t) + 1):
        count_b_cum[i] = count_b_cum[i - 1] + count_b[- i - 1]
    # print(count_b_cum)
    res = 0
    for r in res_a:
        res += count_b_cum[r]
    return res


def main():
    n_, t = input().split()
    n = int(n_)
    s_list = [input() for _ in range(n)]
    res = solve(n, t, s_list)
    print(res)


def test():
    assert solve(3, "abc", ["abba", "bcb", "aaca"]) == 3
    assert solve(5, "xx", ["x", "x", "x", "x", "x"]) == 25
    assert solve(1, "y", ["x"]) == 0
    assert solve(10, "ms", [
        "mkgn", "m", "hlms", "vmsle", "mxsm", "nnzdhi",
        "umsavxlb", "ffnsybomr", "yvmm", "naouel"
    ]) == 68


if __name__ == "__main__":
    test()
    main()
