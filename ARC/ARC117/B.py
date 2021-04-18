MOD = 10 ** 9 + 7


def solve(n, a_list):
    a_list_s = [0] + sorted(a_list)
    res = 1
    for i in range(n):
        res *= a_list_s[i + 1] - a_list_s[i] + 1
        res %= MOD
    return res


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(2, [1, 2]) == 4
    assert solve(6, [5, 3, 4, 1, 5, 2]) == 32
    assert solve(7, [314, 159, 265, 358, 979, 323, 846]) == 492018656


if __name__ == "__main__":
    test()
    main()
