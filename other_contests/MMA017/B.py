def solve(n, m, a_list):
    # (a + b)^2 >= a^2 + b^2なので、
    # 難易度の小さい順に並べたとき、間を飛ばす理由がない
    if m == 1:
        return 0
    d_list = []
    a_list_s = list(sorted(a_list))
    for i in range(n - 1):
        d_list.append((a_list_s[i + 1] - a_list_s[i]) ** 2)
    r = sum(d_list[:(m - 1)])
    res = r
    for i in range(m - 1, n - 1):
        r += d_list[i]
        r -= d_list[i - (m - 1)]
        res = min(res, r)
    return res


def main():
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, m, a_list)
    print(res)


def test():
    assert solve(5, 3, [7, 6, 2, 9, 5]) == 2
    assert solve(10, 5, [
        227930076, 836334727, 108597970, 656892815, 455743732, 901045388, 302006162, 256603330, 228958951, 169578258
    ]) == 6231622091586614


if __name__ == "__main__":
    test()
    main()
