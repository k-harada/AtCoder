def solve(n, k, c, s):
    # greedy from first
    g_f = [0] * n
    last_worked = - c - 1
    cnt = 0
    for i in range(n):
        if last_worked + c + 1 <= i and s[i] == "o":
            cnt += 1
            g_f[i] = cnt
            last_worked = i
        if cnt == k:
            break
    # print(g_f)

    # greedy from last
    g_l = [0] * n
    last_worked = n + c
    cnt = k
    for i in range(n - 1, -1, -1):
        if i + c + 1 <= last_worked and s[i] == "o":
            g_l[i] = cnt
            cnt -= 1
            last_worked = i
        if cnt == 0:
            break
    # print(g_l)

    res = []
    for i in range(n):
        if 0 < g_f[i] == g_l[i]:
            res.append(i + 1)
    return res


def main():
    n, k, c = map(int, input().split())
    s = input()
    res = solve(n, k, c, s)
    for r in res:
        print(r)


def test():
    assert solve(11, 3, 2, "ooxxxoxxxoo") == [6]
    assert solve(5, 2, 3, "ooxoo") == [1, 5]
    assert solve(5, 1, 0, "ooooo") == []
    assert solve(16, 4, 3, "ooxxoxoxxxoxoxxo") == [11, 16]


if __name__ == "__main__":
    test()
    main()
