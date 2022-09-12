from collections import defaultdict


MOD = 998244353


def solve(n, k, a_list):
    a_list_s = list(sorted(a_list))
    left = 0
    right = n - 1
    res = 1
    places = 1

    factorial = [1] * (n + 1)
    factorial_inv = [1] * (n + 1)
    for i in range(1, n + 1):
        factorial[i] = (factorial[i - 1] * i) % MOD

    factorial_inv[-1] = pow(factorial[-1], MOD - 2, MOD)

    for i in range(n, 0, -1):
        factorial_inv[i - 1] = (factorial_inv[i] * i) % MOD

    # 重複分の割り算
    count = defaultdict(int)
    for a in a_list:
        count[a] += 1

    for a in count.keys():
        res *= factorial_inv[count[a]]
        res %= MOD

    for _ in range(n):
        if a_list_s[left] + a_list_s[right] < k:
            # print(a_list_s[left])
            res *= places - 2 * left
            left += 1
        else:
            # print(a_list_s[right])
            res *= places - 2 * left
            right -= 1
        places += 1
        # print(res)
        res %= MOD

    return res


def main():
    n, k = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, k, a_list)
    print(res)


def test():
    assert solve(4, 5, [1, 2, 3, 4]) == 4
    assert solve(4, 3, [1, 2, 3, 3]) == 12
    assert solve(10, 7, [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]) == 108


if __name__ == "__main__":
    test()
    main()
