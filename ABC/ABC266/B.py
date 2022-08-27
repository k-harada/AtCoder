MOD = 998244353


def solve(n):
    return n % MOD


def main():
    n = int(input())
    res = solve(n)
    print(res)


def test():
    assert solve(998244354) == 1
    assert solve(-9982443534) == 998244349


if __name__ == "__main__":
    test()
    main()
