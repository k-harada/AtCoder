MOD = 998244353

def solve_sub(c):
    # x < y < z
    res_1 = 0
    for y in range(2, c + 1):
        if y * y >= c:
            break
        res_1 += ((c // y) - y) * (y - 1) % MOD
    res_1 %= MOD
    # x < y = z
    res_2 = 0
    for y in range(2, c + 1):
        if y * y > c:
            break
        res_2 += y - 1
    res_2 %= MOD
    # x = y < z
    res_3 = 0
    for y in range(1, c + 1):
        if y * y >= c:
            break
        res_3 += ((c // y) - y)
    res_3 %= MOD
    # x = y = z
    res_4 = 0
    for y in range(1, c + 1):
        if y * y > c:
            break
        res_4 += 1
    return (res_1 * 6 + res_2 * 3 + res_3 * 3 + res_4) % MOD


def solve(t, c_list):
    res = [solve_sub(c) for c in c_list]
    # print(res)
    return res


def main():
    t = int(input())
    c_list = [int(input()) for _ in range(t)]
    res = solve(t, c_list)
    for r in res:
        print(r)


def test():
    assert solve(4, [1, 2, 5, 998244353]) == [1, 4, 17, 727512986]


if __name__ == "__main__":
    test()
    main()
