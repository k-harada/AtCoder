def solve(n, a_list, q, b_list):
    res = [0] * q
    a_list_s = [-10 ** 10] + list(sorted(a_list)) + [10 ** 10]
    b_list_p = [(b, i) for i, b in enumerate(b_list)]
    b_list_ps = sorted(b_list_p, key=lambda x: x[0])
    i = 0
    for j in range(q):
        p, s = b_list_ps[j]
        while a_list_s[i] < p:
            i += 1
        res[s] = min(p - a_list_s[i - 1], a_list_s[i] - p)
    return res


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    q = int(input())
    b_list = list([int(input()) for _ in range(q)])
    res = solve(n, a_list, q, b_list)
    for r in res:
        print(r)


def test():
    assert solve(4, [4000, 4400, 5000, 3200], 3, [3312, 2992, 4229]) == [112, 208, 171]
    assert solve(1, [4000], 10, [3582, 3538, 3320, 3312, 3296, 3257, 3111, 3040, 3013, 2994]) == [
        418, 462, 680, 688, 704, 743, 889, 960, 987, 1006
    ]


if __name__ == "__main__":
    test()
    main()
