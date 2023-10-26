def solve(n, m, p, a_list, b_list):
    a_list_s = list(sorted(a_list))
    b_list_s = list(sorted(b_list))

    res = p * n * m

    b_list_cum = [0]
    for b in b_list_s:
        b_list_cum.append(b_list_cum[-1] + b)
    # print(b_list_cum)
    # print(res)

    j = m - 1
    for i in range(n):
        while a_list_s[i] + b_list_s[j] >= p and j >= 0:
            j -= 1
            if j < 0:
                break

        res += b_list_cum[j + 1] + a_list_s[i] * (j + 1)
        res -= p * (j + 1)
        # print(i, j, res)

    return res


def main():
    n, m, p = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    res = solve(n, m, p, a_list, b_list)
    print(res)


def test():
    assert solve(2, 2, 7, [3, 5], [6, 1]) == 24
    assert solve(1, 3, 2, [1], [1, 1, 1]) == 6
    assert solve(7, 12, 25514963, [
        2436426, 24979445, 61648772, 23690081, 33933447, 76190629, 62703497
    ], [
        11047202, 71407775, 28894325, 31963982, 22804784, 50968417,
        30302156, 82631932, 61735902, 80895728, 23078537, 7723857
    ]) == 2115597124


if __name__ == "__main__":
    test()
    main()
