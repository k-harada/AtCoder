def solve(n, d, p, f_list):
    f_list_s = list(sorted(f_list, reverse=True))
    res = sum(f_list)
    i = 0
    while i * d < n:
        if sum(f_list_s[(i * d):((i + 1) * d)]) > p:
            res -= sum(f_list_s[(i * d):((i + 1) * d)]) - p
        i += 1
    # print(res)
    return res


def main():
    n, d, p = map(int, input().split())
    f_list = list(map(int, input().split()))
    res = solve(n, d, p, f_list)
    print(res)


def test():
    assert solve(5, 2, 10, [7, 1, 6, 3, 6]) == 20
    assert solve(3, 1, 10, [1, 2, 3]) == 6
    assert solve(8, 3, 1000000000, [
        1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000
    ]) == 3000000000


if __name__ == "__main__":
    test()
    main()
