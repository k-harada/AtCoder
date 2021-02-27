def solve(k, s, t):
    s_cnt = [0] * 10
    t_cnt = [0] * 10
    for c in s[:4]:
        s_cnt[int(c)] += 1
    for c in t[:4]:
        t_cnt[int(c)] += 1
    s_score_base = sum([i * 10 ** s_cnt[i] for i in range(1, 10)])
    t_score_base = sum([i * 10 ** t_cnt[i] for i in range(1, 10)])
    res = 0.0
    for i in range(1, 10):
        s_score = s_score_base + i * 10 ** s_cnt[i] * 9
        p = (k - s_cnt[i] - t_cnt[i]) / (9 * k - 8)
        for j in range(1, 10):
            t_score = t_score_base + j * 10 ** t_cnt[j] * 9
            q = (k - s_cnt[j] - t_cnt[j] - (i == j)) / (9 * k - 9)
            if p * q > 0 and s_score > t_score:
                # print(i, j, p * q)
                res += p * q
    return res


def main():
    k = int(input())
    s = input()
    t = input()
    res = solve(k, s, t)
    print(res)


def test():
    assert abs(solve(2, "1144#", "2233#") - 0.4444444444444444) < 0.000001
    assert abs(solve(2, "9988#", "1122#") - 1.0) < 0.000001
    assert abs(solve(6, "1122#", "2228#") - 0.001932367149758454) < 0.000001
    assert abs(solve(100000, "3226#", "3597#") - 0.6296297942426154) < 0.000001


if __name__ == "__main__":
    test()
    main()
