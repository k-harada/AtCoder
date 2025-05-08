import math


def solve(n, m, p_list):
    left = 0
    right = m
    while left + 1 < right:
        mid = (left + right) // 2
        cost = 0
        for p in p_list:
            q = (mid // p + 1) // 2
            cost += q * q * p
        # print(left, right, mid, cost)
        if cost > m:
            right = mid
        else:
            left = mid
    # print(left, right, cost)
    res = 0
    cost = 0
    for p in p_list:
        q = (left // p + 1) // 2
        cost += q * q * p
        res += q
    # rightの調整
    count_just = 0
    for p in p_list:
        if right % p == 0:
            if (right // p) % 2 == 1:
                count_just += 1
    d = (m - cost) // right
    res += min(d, count_just)
    return res


def main():
    n, m = map(int, input().split())
    p_list = list(map(int, input().split()))
    res = solve(n, m, p_list)
    print(res)


def test():
    assert solve(3, 9, [4, 1, 9]) == 3
    assert solve(10, 1000, [2, 15, 6, 5, 12, 1, 7, 9, 17, 2]) == 53


if __name__ == "__main__":
    test()
    main()
