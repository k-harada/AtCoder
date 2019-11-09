LARGE = 998244353


def solve(n, d_list):
    cnt = [0] * (max(d_list) + 1)
    for i in range(n):
        cnt[d_list[i]] += 1
    if cnt[0] != 1 or d_list[0] != 0:
        return 0
    res = 1
    for i in range(max(d_list)):
        res *= pow(cnt[i], cnt[i + 1], LARGE)
        res %= LARGE
    return res


def main():
    n = int(input())
    d_list = list(map(int, input().split()))
    res = solve(n, d_list)
    print(res)


def test():
    assert solve(4, [0, 1, 1, 2]) == 2
    assert solve(4, [1, 1, 1, 1]) == 0
    assert solve(7, [0, 3, 2, 1, 2, 2, 1]) == 24


if __name__ == "__main__":
    test()
    main()
