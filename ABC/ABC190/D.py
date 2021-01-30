def solve(n):
    res = 0
    for i in range(1, 2 * n + 1):
        if i * i > 2 * n:
            break
        if (2 * n) % i == 0:
            p = i
            q = (2 * n) // i
            if (q - p + 1) % 2 == 0:
                if p == q:
                    res += 1
                else:
                    res += 2
    return res


def main():
    n = int(input())
    res = solve(n)
    print(res)


def test():
    assert solve(12) == 4
    assert solve(1) == 2
    assert solve(963761198400) == 1920


def test_large():
    print(solve(1000000000000))


if __name__ == "__main__":
    test()
    main()
