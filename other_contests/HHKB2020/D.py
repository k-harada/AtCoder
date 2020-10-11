MOD = 1000000007


def solve(t, nab_list):
    res_list = []
    for s in range(t):
        n, a, b = nab_list[s]
        # red completely left than blue
        # res_1 = 0
        # for j in range(n + 1):
        #     if b <= j <= n - a:
        #         res_1 += (j - b + 1) * (n - b + 1)
        # for j in range(n - a - b + 1):
        #     res_1 += (j + 1) * (n - b + 1)
        res_1 = ((n - b + 1) * (n - a + 1) % MOD) * ((n - a - b + 1) * (n - a - b + 2) % MOD) % MOD
        # res_2 = 0
        # red completely left and up than blue
        # for i in range(n + 1):
        #     for j in range(n + 1):
        #         if b <= i <= n - a and b <= j <= n - a:
        #             res_2 += (i - b + 1) * (j - b + 1)
        # for i in range(n - a - b + 1):
        #     for j in range(n - a - b + 1):
        #         res_2 += (i + 1) * (j + 1)
        res_2 = (((n - a - b + 1) * (n - a - b + 2) % MOD) ** 2) % MOD
        # print(res_1, res_2)
        if a + b > n:
            res_list.append(0)
        else:
            res_list.append((2 * res_1 - res_2) % MOD)
    # print(res_list)
    return res_list


def main():
    t = int(input())
    nab_list = [list(map(int, input().split())) for _ in range(t)]
    res = solve(t, nab_list)
    # print(res)
    for r in res:
        print(r)


def test():
    assert solve(3, [[3, 1, 2], [4, 2, 2], [331895368, 154715807, 13941326]]) == [20, 32, 409369707]


if __name__ == "__main__":
    test()
    main()
