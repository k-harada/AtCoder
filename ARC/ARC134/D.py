def solve(n, a_list):

    # cum_min
    cum_min = [0] * n
    m = 10 ** 9 + 7
    cum_min[-1] = m
    for i in range(n - 1, 0, -1):
        m = min(m, a_list[i])
        cum_min[i - 1] = m

    array_left = []
    array_right = []
    # find where to start
    a_min = min(a_list[:n])
    mini_an = a_min
    mini_i = 0
    for i in range(n):
        if a_list[i] == a_min:
            if a_list[i + n] < mini_an:
                mini_an = a_list[i + n]
                mini_i = i
    dec_flag = 0
    inc_flag = 0
    right_start = 10 ** 9 + 7
    for i in range(mini_i, n):
        if a_list[i] <= min(cum_min[i], right_start):
            if a_list[i] == right_start:
                if inc_flag == 0:
                    continue
            array_left.append(a_list[i])
            array_right.append(a_list[n + i])
            if len(array_right) == 1:
                right_start = a_list[n + i]
            else:
                if array_right[-1] < array_right[-2] and inc_flag == 0:
                    dec_flag = 1
                elif array_right[-1] > array_right[-2] and dec_flag == 0:
                    inc_flag = 1

    # print(dec_flag)
    res_list = array_left + array_right
    res = " ".join([str(a) for a in res_list])
    # print(res)
    return res


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(3, [2, 1, 3, 1, 2, 2]) == "1 2"
    assert solve(
        10, [38, 38, 80, 62, 62, 67, 38, 78, 74, 52, 53, 77, 59, 83, 74, 63, 80, 61, 68, 55]
    ) == "38 38 38 52 53 77 80 55"
    assert solve(
        12, [52, 73, 49, 63, 55, 74, 35, 68, 22, 22, 74, 50, 71, 60, 52, 62, 65, 54, 70, 59, 65, 54, 60, 52]
    ) == "22 22 50 65 54 52"


if __name__ == "__main__":
    test()
    main()
