from bisect import bisect_left, bisect_right


def solve(n, ab_list):
    a_list = []
    b_list = []
    for a, b in ab_list:
        a_list.append(a)
        b_list.append(b)
    a_list = sorted(a_list)
    b_list = sorted(b_list)
    v_list = list(sorted(list(set(a_list + b_list))))
    m = len(v_list)

    if n % 2 == 1:
        ok_min = 10 ** 9 + 7
        ok_max = -1
        for i in range(m):
            v = v_list[i]
            lower_count = bisect_left(b_list, v)
            higher_count = n - bisect_right(a_list, v)
            if lower_count <= n // 2 and higher_count <= n // 2:
                ok_min = min(ok_min, v)
                ok_max = max(ok_max, v)
        return ok_max - ok_min + 1
    else:
        ok_min_left = 10 ** 9 + 7
        ok_max_left = -1
        ok_min_right = 10 ** 9 + 7
        ok_max_right = -1
        for i in range(m):
            v = v_list[i]
            lower_count = bisect_left(b_list, v)
            higher_count = n - bisect_right(a_list, v)
            if lower_count <= n // 2 - 1 and higher_count <= n // 2:
                ok_min_left = min(ok_min_left, v)
                ok_max_left = max(ok_max_left, v)
            if lower_count <= n // 2 and higher_count <= n // 2 - 1:
                ok_min_right = min(ok_min_right, v)
                ok_max_right = max(ok_max_right, v)
        return (ok_max_right - ok_min_right + ok_max_left - ok_min_left) + 1


def main():
    n = int(input())
    ab_list = [list(map(int, input().split())) for _ in range(n)]
    res = solve(n, ab_list)
    print(res)


def test():
    assert solve(2, [[1, 2], [2, 3]]) == 3
    assert solve(3, [[100, 100], [10, 10000], [1, 1000000000]]) == 9991


if __name__ == "__main__":
    test()
    main()
