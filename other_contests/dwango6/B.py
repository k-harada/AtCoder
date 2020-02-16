LARGE = 10 ** 9 + 7


def solve(n, x_list):

    n_1_fac = 1
    for i in range(2, n):
        n_1_fac *= i
        n_1_fac %= LARGE

    res = 0
    for i in range(n - 1):
        res += (x_list[n - 1] - x_list[i]) * n_1_fac * pow(n - 1 - i, LARGE - 2, LARGE)
        res %= LARGE

    x_left = 0
    x_right = 0
    for k in range(1, n - 1):
        x_right += x_list[n - 1 - k]
        x_left += x_list[k - 1]
        res += (x_right - x_left) * n_1_fac * pow(k, LARGE - 2, LARGE) * pow(k + 1, LARGE - 2, LARGE)
        res %= LARGE
    return res


def main():
    n = int(input())
    x_list = list(map(int, input().split()))
    res = solve(n, x_list)
    print(res)


def test():
    assert solve(3, [1, 2, 3]) == 5
    assert solve(12, [
        161735902, 211047202, 430302156, 450968417, 628894325, 707723857,
        731963982, 822804784, 880895728, 923078537, 971407775, 982631932
    ]) == 750927044


if __name__ == "__main__":
    test()
    main()
