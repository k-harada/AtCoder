def solve(n, x, m):
    v = x
    v_dict = {v: 1}
    v_list = [0, v]
    j = 1
    for j in range(2, n + 1):
        v = (v * v) % m
        if v not in v_dict.keys():
            v_dict[v] = j
            v_list.append(v)
        else:
            break
    i = v_dict[v]
    # 1 to i
    res_1 = x
    v = x
    for k in range(2, i + 1):
        v = (v * v) % m
        res_1 += v
    # i to j
    res_2 = 0
    if i < j:
        for k in range(i + 1, j + 1):
            v = (v * v) % m
            res_2 += v
        res_2 *= (n - i) // (j - i)
        ll = i + ((n - i) // (j - i)) * (j - i)
    # m to last
    res_3 = 0
    if i < j:
        for k in range(ll + 1, n + 1):
            v = (v * v) % m
            res_3 += v

    return res_1 + res_2 + res_3


def main():
    n, x, m = map(int, input().split())
    res = solve(n, x, m)
    print(res)


def test():
    assert solve(6, 2, 1001) == 1369
    assert solve(1000, 2, 16) == 6
    assert solve(10000000000, 10, 99959) == 492443256176507


if __name__ == "__main__":
    test()
    main()
