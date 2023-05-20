def solve(n, k, a_list):
    left = [0] * n
    right = [0] * n
    m = n * (n + 1) // 2
    for i in range(n):
        for j in range(i + 1, n):
            if a_list[j] < a_list[i]:
                left[i] += 1
            else:
                right[i] += 1
    # print(left)
    # print(right)

    i0, j0 = -1, -1

    if sum(left) >= k:
        left_s = 0
        for i in range(n):
            left_s += left[i]
            if left_s >= k:
                left_s -= left[i]
                j_list = []
                for j in range(i + 1, n):
                    if a_list[j] < a_list[i]:
                        j_list.append(a_list[j])
                j_list_s = list(sorted(j_list))
                i0, j0 = i, j_list_s[k - left_s - 1]
            if i0 >= 0:
                break
    elif sum(left) + n >= k:
        pass
    else:
        right_s = 0
        for i in range(n):
            right_s += right[i]
            if right_s >= m - k + 1:
                right_s -= right[i]
                j_list = []
                for j in range(i + 1, n):
                    if a_list[j] > a_list[i]:
                        j_list.append(a_list[j])
                j_list_s = list(sorted(j_list, reverse=True))
                # print(i, j_list_s)
                i0, j0 = i, j_list_s[m - k + 1 - right_s - 1]
            if i0 >= 0:
                break
    # print(i0, j0)
    if i0 == -1:
        return " ".join([str(a) for a in a_list])
    else:
        for i in range(n):
            if a_list[i] == j0:
                p = i
        # print(i0, j0, p)
        b_list = a_list[:i0] + list(reversed(a_list[i0:p + 1])) + a_list[p + 1:]
        # print(b_list)
        return " ".join([str(a) for a in b_list])


def main():
    n, k = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, k, a_list)
    print(res)


def test():
    assert solve(3, 5, [1, 3, 2]) == "2 3 1"
    assert solve(5, 15, [1, 2, 3, 4, 5]) == "5 4 3 2 1"
    assert solve(10, 37, [9, 2, 1, 3, 8, 7, 10, 4, 5, 6]) == "9 2 1 6 5 4 10 7 8 3"


if __name__ == "__main__":
    test()
    main()
