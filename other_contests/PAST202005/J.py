from bisect import bisect_right


def solve(n, m, a_list):
    taste_list = [0] * n
    res_list = [0] * m
    for i, a in enumerate(a_list):
        j = bisect_right(taste_list, -a)
        if j == n:
            res_list[i] = -1
        else:
            res_list[i] = j + 1
            taste_list[j] = -a
    return res_list


def main():
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, m, a_list)
    for r in res:
        print(r)


def test():
    assert solve(2, 5, [5, 3, 2, 4, 8]) == [1, 2, -1, 2, 1]
    assert solve(5, 10, [13, 16, 6, 15, 10, 18, 13, 17, 11, 3]) == [1, 1, 2, 2, 3, 1, 3, 2, 4, 5]


if __name__ == "__main__":
    test()
    main()
