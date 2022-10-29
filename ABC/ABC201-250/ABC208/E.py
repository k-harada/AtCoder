def solve(n, k):
    # value
    values = [0]
    r1 = 1
    for i in range(60):
        if r1 > k:
            break
        r2 = r1
        for j in range(60):
            if r2 > k:
                break
            r3 = r2
            for p in range(60):
                if r3 > k:
                    break
                r4 = r3
                for q in range(60):
                    if r4 > k:
                        break
                    values.append(r4)
                    r4 *= 7
                r3 *= 5
            r2 *= 3
        r1 *= 2
    values = list(sorted(values))
    values.append(k + 1)
    index_dict = {v: i for i, v in enumerate(values)}
    le = len(str(n))
    dp = [[0] * (len(values)) for _ in range(le + 1)]
    max_value = 1

    for i in range(le):
        # middle -> middle
        for v in values:
            for j in range(10):
                w = j * v
                if w > k:
                    w = k + 1
                w_ind = index_dict[w]
                v_ind = index_dict[v]
                dp[i + 1][w_ind] += dp[i][v_ind]
        # none -> middle
        if i > 0:
            for j in range(1, 10):
                w = j
                if w > k:
                    w = k + 1
                w_ind = index_dict[w]
                dp[i + 1][w_ind] += 1
        # max
        a = int(str(n)[i])
        for j in range(a):
            if i == 0 and j == 0:
                continue
            v = max_value
            w = j * v
            if w > k:
                w = k + 1
            w_ind = index_dict[w]
            dp[i + 1][w_ind] += 1
        max_value *= a

    # print(dp)
    res = sum(dp[-1][:-1])
    if max_value <= k:
        res += 1
    # print(res)
    return res


def main():
    n, k = map(int, input().split())
    res = solve(n, k)
    print(res)


def test():
    assert solve(13, 2) == 5
    assert solve(100, 80) == 99
    assert solve(1000, 1000) == 1000
    assert solve(25, 5) == 14
    assert solve(1000000000000000000, 1000000000) == 841103275147365677


if __name__ == "__main__":
    test()
    main()
