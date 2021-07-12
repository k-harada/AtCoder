MOD = 10 ** 9 + 7


def solve(n, c_list):
    c_list_s = list(sorted(c_list))
    r = 1
    for i, c in enumerate(c_list_s):
        r *= c - i
        r %= MOD
    return r


def main():
    n = int(input())
    c_list = list(map(int, input().split()))
    res = solve(n, c_list)
    print(res)


def test():
    assert solve(2, [1, 3]) == 2
    assert solve(4, [3, 3, 4, 4]) == 12
    assert solve(2, [1, 1]) == 0


if __name__ == "__main__":
    test()
    main()
