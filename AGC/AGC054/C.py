MOD = 998244353


def solve(n, k, p_list):
    res = 1
    c_list = [0] * (n + 1)
    for i in range(n - 1):
        p = p_list[i]
        if p_list[i] < p_list[i + 1]:
            c = sum(c_list[(p + 1):])
            if c == k:
                res *= (n - i)
                res %= MOD
        c_list[p] += 1

    return res


def main():
    n, k = map(int, input().split())
    p_list = list(map(int, input().split()))
    res = solve(n, k, p_list)
    print(res)


def test():
    assert solve(3, 1, [3, 1, 2]) == 2
    assert solve(4, 3, [4, 3, 2, 1]) == 1
    assert solve(5, 2, [4, 2, 1, 5, 3]) == 3


if __name__ == "__main__":
    test()
    main()
