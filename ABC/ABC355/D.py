from bisect import bisect_right


def solve(n, lr_list):
    left_list = []
    for left, right in lr_list:
        left_list.append(left)
    left_list = list(sorted(left_list))
    lr_list_s = list(sorted(lr_list, key=lambda x: x[0]))
    res = 0
    for i, (left, right) in enumerate(lr_list_s):
        res += bisect_right(left_list, right) - (i + 1)
    return res


def main():
    n = int(input())
    lr_list = [tuple(map(int, input().split())) for _ in range(n)]
    res = solve(n, lr_list)
    print(res)


def test():
    assert solve(3, [(1, 5), (7, 8), (3, 7)]) == 2
    assert solve(3, [(3, 4), (2, 5), (1, 6)]) == 3
    assert solve(2, [(1, 2), (3, 4)]) == 0


if __name__ == "__main__":
    test()
    main()
