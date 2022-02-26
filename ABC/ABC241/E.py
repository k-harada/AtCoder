def solve(n, k, a_list):

    appear = [0] * n
    r = 0
    appear[0] = 1
    while True:
        r += a_list[r % n]
        r %= n
        if appear[r] == 1:
            break
        appear[r] += 1

    s1 = 0
    c1 = 0
    while True:
        s1 += a_list[s1 % n]
        c1 += 1
        if s1 % n == r:
            break
    # print(s1, c1)

    s2 = s1
    c2 = 0
    while True:
        s2 += a_list[s2 % n]
        c2 += 1
        if s2 % n == r:
            break
    # print(s2, c2)

    if k >= c1:
        res = s1 + (s2 - s1) * ((k - c1) // c2)
        c = c1 + c2 * ((k - c1) // c2)
    else:
        res = 0
        c = 0

    for _ in range(k - c):
        res += a_list[res % n]
    # print(res)
    return res


def main():
    n, k = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, k, a_list)
    print(res)


def test():
    assert solve(5, 3, [2, 1, 6, 3, 1]) == 11
    assert solve(10, 1000000000000, [260522, 914575, 436426, 979445, 648772, 690081, 933447, 190629, 703497, 47202]) == 826617499998784056


if __name__ == "__main__":
    test()
    main()
