def solve(n, k, td_list):
    # d-greedy
    eaten = [0] * (n + 1)
    seconds = []
    firsts = []
    r = 0
    s = 0
    td_list_s = list(sorted(td_list, key=lambda x: -x[1]))
    cnt = 0
    for t, d in td_list_s:
        if cnt < k:
            # eat
            r += d
            cnt += 1
            if eaten[t] == 1:
                seconds.append(d)
            else:
                s += 1
                eaten[t] = 1
        else:
            if eaten[t] == 0:
                firsts.append(d)
                eaten[t] = 1
    # print(r, s, firsts, seconds)
    res = r + s ** 2
    for i in range(min(len(firsts), len(seconds))):
        r -= seconds[-(i + 1)]
        r += firsts[i]
        s += 1
        res = max(res, r + s ** 2)

    return res


def main():
    n, k = map(int, input().split())
    td_list = [tuple(map(int, input().split())) for _ in range(n)]
    res = solve(n, k, td_list)
    print(res)


def test():
    assert solve(5, 3, [(1, 9), (1, 7), (2, 6), (2, 5), (3, 1)]) == 26
    assert solve(7, 4, [(1, 1), (2, 1), (3, 1), (4, 6), (4, 5), (4, 5), (4, 5)]) == 25
    assert solve(6, 5, [
        (5, 1000000000), (2, 990000000), (3, 980000000), (6, 970000000), (6, 960000000), (4, 950000000)
    ]) == 4900000016


if __name__ == "__main__":
    test()
    main()
