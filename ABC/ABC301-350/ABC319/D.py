def solve_sub(n, w, le_list):
    res = 1
    c = 0
    for le in le_list:
        if le > w:
            return 10 ** 9 + 7
        if c == 0:
            c = le
        elif c + le + 1 <= w:
            c += le + 1
        else:
            c = le
            res += 1
    return res


def solve(n, m, le_list):
    left = 0
    right = sum(le_list) + n - 1
    while left + 1 < right:
        mid = (left + right) // 2
        if solve_sub(n, mid, le_list) > m:
            left = mid
        else:
            right = mid
    # print(right)
    return right


def main():
    n, m = map(int, input().split())
    le_list = list(map(int, input().split()))
    res = solve(n, m, le_list)
    print(res)


def test():
    assert solve(13, 3, [9, 5, 2, 7, 1, 8, 8, 2, 1, 5, 2, 3, 6]) == 26
    assert solve(10, 1, [
        1000000000, 1000000000, 1000000000, 1000000000, 1000000000,
        1000000000, 1000000000, 1000000000, 1000000000, 1000000000
    ]) == 10000000009
    assert solve(30, 8, [
        8, 55, 26, 97, 48, 37, 47, 35, 55, 5,
        17, 62, 2, 60, 23, 99, 73, 34, 75, 7,
        46, 82, 84, 29, 41, 32, 31, 52, 32, 60
    ]) == 189


if __name__ == "__main__":
    test()
    main()
