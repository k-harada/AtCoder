def solve(n, m, k, a_list):
    res = 0
    b_list = a_list.copy()
    for i in range(30, -1, -1):
        d_list = []
        for b in b_list:
            if (b >> i) & 1:
                d_list.append(0)
            else:
                d_list.append((1 << i) - b % (1 << i))
        e_list = list(sorted([b_list[j] + d_list[j] - a_list[j] for j in range(n)]))
        if sum(e_list[:k]) <= m:
            res += 1 << i
            b_list = [b_list[j] + d_list[j] for j in range(n)]

    return res


def main():
    n, m, k = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, m, k, a_list)
    print(res)


def test():
    assert solve(4, 8, 2, [1, 2, 4, 8]) == 10
    assert solve(5, 345, 3, [111, 192, 421, 390, 229]) == 461


def test_large():
    print(solve(200000, 2**30, 200000, [2**30] * 200000))


if __name__ == "__main__":
    test()
    # test_large()
    main()
