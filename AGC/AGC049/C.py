def solve(n, a_list, b_list):

    res = 10 ** 9 + 1

    reach_flag = [0] * n
    for i in range(n):
        if a_list[i] <= b_list[i]:
            reach_flag[i] = 1

    cleaner = 10 ** 9 + 1
    cost = 0
    for i in range(n - 1, -1, -1):
        if reach_flag[i] == 0:
            cleaner = min(cleaner, a_list[i] - b_list[i])
        else:
            res = min(res, max(cost, b_list[i] - a_list[i] + 1))
            if cleaner <= a_list[i]:
                pass
            else:
                cost += 1
                cleaner = a_list[i]
    res = min(res, cost)
    # print(res)
    return res


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    res = solve(n, a_list, b_list)
    print(res)


def test():
    assert solve(3, [1, 2, 3], [1, 2, 1]) == 1
    assert solve(4, [1, 3, 5, 7], [3, 1, 4, 1]) == 0


if __name__ == "__main__":
    test()
    main()
