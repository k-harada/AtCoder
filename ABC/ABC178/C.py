def solve(n):
    mod = 10 ** 9 + 7
    return (pow(10, n, mod) - 2 * pow(9, n, mod) + pow(8, n, mod)) % mod


def main():
    n = int(input())
    res = solve(n)
    print(res)


def test():
    assert solve(2) == 2
    assert solve(1) == 0
    assert solve(869121) == 2511445


if __name__ == "__main__":
    test()
    main()
