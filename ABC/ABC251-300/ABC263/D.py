def solve(n, l, r, a_list):
    s = sum(a_list)
    res = s
    reduce_left = [0]
    reduce_right = [0]
    for a in a_list:
        reduce_left.append(reduce_left[-1] + (a - l))
    for a in reversed(a_list):
        reduce_right.append(reduce_right[-1] + (a - r))
    reduce_left_max = [0]
    reduce_right_max = [0]
    for i in range(n):
        reduce_left_max.append(max(reduce_left_max[-1], reduce_left[i + 1]))
    for i in range(n):
        reduce_right_max.append(max(reduce_right_max[-1], reduce_right[i + 1]))

    for i in range(n + 1):
        res = min(res, s - reduce_right[i] - reduce_left_max[n - i])

    return res


def main():
    n, l, r = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, l, r, a_list)
    print(res)


def test():
    assert solve(5, 4, 3, [5, 5, 0, 6, 3]) == 14
    assert solve(4, 10, 10, [1, 2, 3, 4]) == 10
    assert solve(10, -5, -3, [9, -6, 10, -1, 2, 10, -1, 7, -15, 5]) == -58


if __name__ == "__main__":
    test()
    main()
