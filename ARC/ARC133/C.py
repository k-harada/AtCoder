def solve(h, w, k, a_list, b_list):
    if sum(a_list) % k != sum(b_list) % k:
        return -1
    res = (k - 1) * (h - 1) * (w - 1)
    res_a = (h - 1) * (k - 1)
    for a in a_list[:-1]:
        r = (a - (w - 1) * (k - 1)) % k
        res += r
        res_a -= r
    res_b = (w - 1) * (k - 1)
    for b in b_list[:-1]:
        r = (b - (h - 1) * (k - 1)) % k
        res += r
        res_b -= r
    r = (sum(a_list) - res) % k
    res += r
    d = min(res_a, res_b) // k
    res += d * k
    res_a -= d * k
    res_b -= d * k
    if r < k - 1 and min(res_a, res_b) > r:
        res += k
    return res


def main():
    h, w, k = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    res = solve(h, w, k, a_list, b_list)
    print(res)


def test():
    assert solve(2, 4, 3, [0, 2], [1, 2, 2, 0]) == 11
    assert solve(3, 3, 4, [0, 1, 2], [1, 2, 3]) == -1


if __name__ == "__main__":
    test()
    main()
