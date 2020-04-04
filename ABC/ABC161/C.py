def solve(n, k):
    if n > k:
        n = n % k
    return min(n, k - n)


def main():
    n, k = map(int, input().split())
    res = solve(n, k)
    print(res)


def test():
    assert solve(7, 4) == 1
    assert solve(2, 6) == 2
    assert solve(1000000000000000000, 1) == 0


if __name__ == "__main__":
    test()
    main()
