def solve(m, n):
    """
    斜めに同じ数字が並ぶしかない
    m + n - 1個を問題なく１行に並べる方法をdpで出す
    長くなったら結局4周期で同じの続くからカット
    min(m, n) == 1 の時はそれでいい
    そうじゃない時は斜めのとり方が２通り

    あとはmax(m, n) <= 3のときはその限りじゃないので個別にケア
    例えば
    1 2 3
    3 1 2
    2 3 1
    とか、１行にすると2 3 1 2 3で違反になりそうで違反してない
    """
    if m > 8:
        m = (m - 8) % 4 + 8
    if n > 8:
        n = (n - 8) % 4 + 8
    r = m + n - 1
    key_list = [
        "000", "001", "002", "003", "012", "013", "021", "023", "031", "032",
        "121", "123", "131", "132", "213", "231", "312", "321"
    ]

    p = len(key_list)
    key_dict = dict()
    for i in range(p):
        key_dict[key_list[i]] = i

    edge_list = []
    # 1
    for k in range(p):
        key_k = key_list[k]
        if key_k[-1] == "1":
            continue
        key_s = key_k[1:] + "1"
        s = key_dict[key_s]
        edge_list.append((k, s))
    # 2
    for k in range(p):
        key_k = key_list[k]
        if "2" in key_k[-2:]:
            continue
        key_s = key_k[1:] + "2"
        s = key_dict[key_s]
        edge_list.append((k, s))
    # 3
    for k in range(p):
        key_k = key_list[k]
        if "3" in key_k:
            continue
        key_s = key_k[1:] + "3"
        s = key_dict[key_s]
        edge_list.append((k, s))

    dp = [[0] * p for _ in range(2)]
    dp[0][0] = 1

    for i in range(r):
        for k in range(p):
            dp[(i + 1) % 2][k] = 0
        for k, s in edge_list:
            dp[(i + 1) % 2][s] += dp[i % 2][k]
    if min(m, n) == 1:
        return sum(dp[r % 2])
    elif m == 2 and n == 2:
        return 18
    elif m == 2 and n == 3:
        return 20
    elif m == 3 and n == 2:
        return 20
    elif m == 3 and n == 3:
        return 28
    else:
        return 2 * sum(dp[r % 2])


def main():
    m, n = map(int, input().split())
    res = solve(m, n)
    print(res)


def test():
    assert solve(1, 1) == 3
    assert solve(3, 1) == 8


if __name__ == "__main__":
    test()
    main()
