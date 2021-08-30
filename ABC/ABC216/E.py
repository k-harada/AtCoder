def solve(n, k, a_list):
    a_list_s = list(sorted(a_list, reverse=True))
    a_list_s.append(0)
    k_rest = k
    a = a_list_s[0]
    res = 0
    cnt = 0
    i = 0
    while a > 0 and k_rest > 0:
        while a_list_s[i] == a:
            i += 1
            cnt += 1
        next_a = a_list_s[i]
        # print(a, cnt, next_a)
        if (a - next_a) * cnt <= k_rest:
            res += cnt * (a - next_a) * (a + next_a + 1) // 2
            k_rest -= (a - next_a) * cnt
            a = next_a
        else:
           cnt_q = k_rest // cnt
           cnt_r = k_rest % cnt
           res += cnt * (a + a - cnt_q + 1) * cnt_q // 2
           res += cnt_r * (a - cnt_q)
           k_rest = 0
        # print(res, a, k_rest)
    return res


def main():
    n, k = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, k, a_list)
    print(res)


def test():
    assert solve(3, 5, [100, 50, 102]) == 502
    assert solve(2, 2021, [2, 3]) == 9


if __name__ == "__main__":
    test()
    main()
