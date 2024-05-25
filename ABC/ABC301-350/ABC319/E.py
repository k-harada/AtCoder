def solve(n, x, y, pt_list, q, q_list):
    mod = 8 * 3 * 7 * 5
    res = []
    dp = [-1] * mod
    for q_ in q_list:
        if dp[q_ % mod] != -1:
            res.append(q_ + dp[q_ % mod])
            continue
        r = q_ + x
        for p, t in pt_list:
            r += (-r) % p
            r += t
        r += y
        dp[q_ % mod] = r - q_
        res.append(r)
    return res


def main():
    n, x, y = map(int, input().split())
    pt_list = [tuple(map(int, input().split())) for _ in range(n - 1)]
    q = int(input())
    q_list = [int(input()) for _ in range(q)]
    res = solve(n, x, y, pt_list, q, q_list)
    for r in res:
        print(r)


def test():
    assert solve(4, 2, 3, [(5, 4), (6, 6), (3, 1)], 7, [
        13, 0, 710511029, 136397527, 763027379, 644706927, 447672230
    ]) == [34, 22, 710511052, 136397548, 763027402, 644706946, 447672250]


if __name__ == "__main__":
    test()
    main()
