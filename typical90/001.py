def solve(n, le, k, a_list):
    left = 0
    right = le

    while left < right - 1:
        mid = (left + right) // 2
        k_temp = 0
        a = 0
        for i in range(n):
            if a_list[i] >= a + mid:
                k_temp += 1
                a = a_list[i]
                # print(mid, a, i)
        if le >= a + mid:
            k_temp += 1
        if k_temp >= k + 1:
            left = mid
        else:
            right = mid
        # print(mid)
    # print(left)
    return left


def main():
    n, le = map(int, input().split())
    k = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, le, k, a_list)
    print(res)


def test():
    assert solve(3, 34, 1, [8, 13, 26]) == 13
    assert solve(7, 45, 2, [7, 11, 16, 20, 28, 34, 38]) == 12
    assert solve(3, 100, 1, [28, 54, 81]) == 46


if __name__ == "__main__":
    test()
    main()
