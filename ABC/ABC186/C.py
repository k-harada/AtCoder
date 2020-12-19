def solve(n):
    res = 0
    for i in range(1, n + 1):
        x = i
        # 10
        if '7' in str(i):
            continue
        # 8
        while x > 0:
            q, r = x // 8, x % 8
            if r == 7:
                break
            x = q
        if x == 0:
            res += 1

    return res


def main():
    n = int(input())
    res = solve(n)
    print(res)


def test():
    assert solve(20) == 17
    assert solve(100000) == 30555


if __name__ == "__main__":
    test()
    main()
