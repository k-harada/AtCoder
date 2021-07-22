def solve(n, a_list, b_list, c_list):
    res = 0
    a_list_s = list(sorted(a_list))
    b_list_s = list(sorted(b_list))
    c_list_s = list(sorted(c_list))
    i = 0
    j = 0
    b_list_new = []
    while j < n:
        if b_list_s[j] > a_list_s[i]:
            b_list_new.append(b_list_s[j])
            i += 1
            j += 1
        else:
            j += 1
    i = 0
    j = 0
    while i < len(b_list_new) and j < n:
        if c_list_s[j] > b_list_new[i]:
            res += 1
            i += 1
            j += 1
        else:
            j += 1
    return res


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    c_list = list(map(int, input().split()))
    res = solve(n, a_list, b_list, c_list)
    print(res)


def test():
    assert solve(5, [9, 6, 14, 1, 8], [2, 10, 3, 12, 11], [15, 13, 5, 7, 4]) == 3
    assert solve(1, [10], [20], [30]) == 1
    assert solve(3, [1, 1, 1], [1, 1, 2], [2, 2, 2]) == 0


if __name__ == "__main__":
    test()
    main()
