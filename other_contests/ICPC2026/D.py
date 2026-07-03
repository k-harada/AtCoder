def solve(s, k):
    if k <= s * s:
        t = 0
        st = 0
        x = 0
        for i in range(s):
            t += 2 * (s - i) - 1
            if k <= t:
                st = t - 2 * (s - i) + 1
                x = i + 1
                break
        if k == st + 1:
            res = s
        elif (k - st) % 2 == 1:
            res = x
        else:
            res = (k - st) // 2 + i
    elif k == s * s + 1:
        res = s
    else:
        x = k - (s * s + 1)
        q, r = (x - 1) // (2 * s), (x - 1) % (2 * s) + 1
        if r % 2 == 0:
            res = r // 2
        else:
            res = s + q + 1
    # print(res)
    return res


def main():
    s, k = map(int, input().split())
    res = solve(s, k)
    print(res)


def test():
    assert solve(3, 1) == 3
    assert solve(3, 2) == 1
    assert solve(3, 3) == 1
    assert solve(3, 4) == 2
    assert solve(3, 5) == 1
    assert solve(6, 100) == 12
    assert solve(1, 100) == 1
    assert solve(1, 101) == 51
    assert solve(100000000, 100000000) == 50000000
    assert solve(123456789, 987654321) == 5
    assert solve(31415926, 535897932) == 16621598


if __name__ == "__main__":
    test()
    main()
