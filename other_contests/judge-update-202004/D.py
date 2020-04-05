import math


def solve(n, q, a_list, s_list):
    res = []
    b_list = [1] * n
    b_list[0] = a_list[0]
    for i in range(1, n):
        b_list[i] = math.gcd(b_list[i - 1], a_list[i])
    # print(b_list)

    # binary search
    def binary_search(x, left_initial, right_initial):

        left = left_initial
        right = right_initial

        while left + 1 < right:
            mid = (left + right) // 2

            if math.gcd(b_list[mid], x) == 1:
                right = mid
            else:
                left = mid

        return left

    for i in range(q):
        s_i = s_list[i]
        if math.gcd(b_list[0], s_i) == 1:
            r = 1
        elif math.gcd(b_list[-1], s_i) > 1:
            r = math.gcd(b_list[-1], s_i)
        else:
            r = binary_search(s_i, 0, n) + 2
        res.append(r)
    # print(res)
    return res


def main():
    n, q = map(int, input().split())
    a_list = list(map(int, input().split()))
    s_list = list(map(int, input().split()))
    res = solve(n, q, a_list, s_list)
    for r in res:
        print(r)


def test():
    assert solve(4, 3, [6, 12, 6, 9], [4, 6, 3]) == [4, 3, 3]
    assert solve(4, 3, [4, 6, 2, 1], [3, 2, 1000000000]) == [1, 4, 4]


if __name__ == "__main__":
    test()
    main()
