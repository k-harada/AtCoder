def solve(n, a_list, b_list):
    a_list.append(a_list[0])
    dp_1 = [[10 ** 18] * 2 for _ in range(n + 1)]
    dp_1[0][0] = 0
    for i in range(n):
        dp_1[i + 1][0] = min(dp_1[i + 1][0], dp_1[i][0] + b_list[i])
        dp_1[i + 1][0] = min(dp_1[i + 1][0], dp_1[i][1])

        dp_1[i + 1][1] = min(dp_1[i + 1][1], dp_1[i][0] + a_list[i + 1])
        dp_1[i + 1][1] = min(dp_1[i + 1][1], dp_1[i][1] + b_list[i] + a_list[i + 1])

    # print(dp_1)
    res_1 = dp_1[-1][0]

    dp_2 = [[10 ** 18] * 2 for _ in range(n + 1)]
    dp_2[0][1] = 0
    for i in range(n):
        dp_2[i + 1][0] = min(dp_2[i + 1][0], dp_2[i][0] + b_list[i])
        dp_2[i + 1][0] = min(dp_2[i + 1][0], dp_2[i][1])

        dp_2[i + 1][1] = min(dp_2[i + 1][1], dp_2[i][0] + a_list[i + 1])
        dp_2[i + 1][1] = min(dp_2[i + 1][1], dp_2[i][1] + b_list[i] + a_list[i + 1])

    # print(dp_2)
    res_2 = dp_2[-1][1]
    return min(res_1, res_2)


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    res = solve(n, a_list, b_list)
    print(res)


def test():
    assert solve(5, [31, 4, 159, 2, 65], [5, 5, 5, 5, 10]) == 16
    assert solve(4, [100, 100, 100, 1000000000], [1, 2, 3, 4]) == 10


if __name__ == "__main__":
    test()
    main()
