MOD = 10 ** 9 + 7


def solve(n, a_list):
    s1 = sum(a_list) % MOD
    s2 = sum([a ** 2 % MOD for a in a_list])
    half = pow(2, MOD - 2, MOD)
    return ((s1 ** 2 - s2) % MOD * half) % MOD


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(3, [1, 2, 3]) == 11
    assert solve(4, [141421356, 17320508, 22360679, 244949]) == 437235829


if __name__ == "__main__":
    test()
    main()
