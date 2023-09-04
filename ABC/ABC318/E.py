def solve(n, a_list):
    m = max(a_list)
    dp = [[] for _ in range(m + 1)]
    for i, a in enumerate(a_list):
        dp[a].append(i)
    res = 0
    for a in range(m + 1):
        if len(dp[a]) <= 1:
            continue
        b_list = []
        c_list = []
        i_before = dp[a][0] - 1
        w = 0
        for i in dp[a]:
            # stock
            if i_before == i - 1:
                w += 1
            else:
                b_list.append((0, w))
                b_list.append((1, i - 1 - i_before))
                w = 1
            i_before = i
        b_list.append((0, w))
        # print(b_list)
        # print(c_list)
        x = 0
        c = 0
        p = len(b_list)
        for i, v in b_list:
            if i == 0:
                c += v
                res += x * v
            else:
                x += c * v
        # print(a, x)
    return res


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(5, [1, 2, 1, 3, 2]) == 3
    assert solve(7, [1, 2, 3, 4, 5, 6, 7]) == 0
    assert solve(13, [9, 7, 11, 7, 3, 8, 1, 13, 11, 11, 11, 6, 13]) == 20


if __name__ == "__main__":
    test()
    main()
