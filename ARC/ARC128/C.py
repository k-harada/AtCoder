def solve(n, m, s, a_list):
    res = 0
    a_cum_sum = [0]
    a_sum = 0
    for a in a_list:
        a_sum += a
        a_cum_sum.append(a_sum)
    for i in range(n - 1):
        for j in range(i + 1, n):
            # [j, n - 1]の平均 * m
            if m * (n - j) < s:
                r = m * (a_cum_sum[n] - a_cum_sum[j])
                # [i, j)の平均 * 残り
                w = s - m * (n - j)
                if w > m * (j - i):
                    continue
                r += w * (a_cum_sum[j] - a_cum_sum[i]) / (j - i)
                if res < r:
                    res = r

    for i in range(n):
        # [i, n - 1]の平均 * s
        if m * (n - i) >= s:
            r = s * (a_cum_sum[n] - a_cum_sum[i]) / (n - i)
            if res < r:
                res = r
    return res


def main():
    n, m, s = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, m, s, a_list)
    print(res)


def test():
    assert solve(3, 2, 3, [1, 2, 3]) == 8.0
    assert solve(3, 3, 2, [5, 1, 1]) == 14.0 / 3
    assert solve(10, 234567, 1000000, [
        353239, 53676, 45485, 617014, 886590, 423581, 172670, 928532, 312338, 981241
    ]) == 2707120580393.0 / 4


if __name__ == "__main__":
    # test()
    main()
