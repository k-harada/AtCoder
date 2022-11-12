def solve(n, a_list, b_list):
    res = 0
    for k in range(0, 29):
        a_list_k_s = list(sorted([a % (2 ** (k + 1)) for a in a_list], reverse=True))
        b_list_k_s = list(sorted([b % (2 ** (k + 1)) for b in b_list]))

        left = 0
        right = 0
        left_2 = 0
        r = 0
        for a in a_list_k_s:
            while left < n:
                if a + b_list_k_s[left] < 2 ** k:
                    left += 1
                else:
                    break
            while right < n:
                if a + b_list_k_s[right] < 2 ** (k + 1):
                    right += 1
                else:
                    break
            while left_2 < n:
                if a + b_list_k_s[left_2] < 3 * (2 ** k):
                    left_2 += 1
                else:
                    break
            # print(a, b_list_k_s[left:right], b_list_k_s[left_2:])
            r += right - left
            r += n - left_2
        # print(k, r)
        if r % 2 == 1:
            res += 2 ** k
    # print(res)
    return res


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    res = solve(n, a_list, b_list)
    print(res)


def test():
    assert solve(2, [1, 2], [3, 4]) == 2
    assert solve(6, [4, 6, 0, 0, 3, 3], [0, 5, 6, 5, 0, 3]) == 8
    assert solve(5, [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]) == 2
    assert solve(1, [0], [0]) == 0


if __name__ == "__main__":
    test()
    main()
