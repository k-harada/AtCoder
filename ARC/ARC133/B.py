from bisect import bisect_left


def solve(n, p_list, q_list):
    dp = [[n] * (n + 1) for _ in range(2)]
    dp[1][0] = -1

    p_index_list = [0] * (n + 1)
    for i in range(n):
        p_index_list[p_list[i]] = i

    for i in range(n):
        j = i % 2
        q = q_list[i]
        r_index_list = []
        for r in range(q, n + 1, q):
            r_index_list.append(p_index_list[r])
        r_index_list_s = sorted(r_index_list)

        dp[j][1] = dp[1 - j]

    return 0


def main():
    n = int(input())
    p_list = list(map(int, input().split()))
    q_list = list(map(int, input().split()))
    res = solve(n, p_list, q_list)
    print(res)


def test():
    assert solve() == 0
    assert solve() == 0
    assert solve() == 0


if __name__ == "__main__":
    test()
    main()
