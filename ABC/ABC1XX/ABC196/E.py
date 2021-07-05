def solve(n, at_list, q, x_list):
    left = -10 ** 10
    right = 10 ** 10
    add_sum = 0
    break_flag = False
    for a, t in at_list:
        if not break_flag:
            if t == 1:
                add_sum += a
            elif t == 2:
                left_now = a - add_sum
                left = max(left_now, left)
            else:
                right_now = a - add_sum
                right = min(right_now, right)
            if left > right:
                break_flag = True
                add_sum = a
        else:
            if t == 1:
                add_sum += a
            elif t == 2:
                add_sum = max(a, add_sum)
            else:
                add_sum = min(a, add_sum)

    res_list = []
    for x in x_list:

        if not break_flag:
            if x <= left:
                res_list.append(left + add_sum)
            elif x >= right:
                res_list.append(right + add_sum)
            else:
                res_list.append(x + add_sum)
        else:
            res_list.append(add_sum)
    return res_list


def main():
    n = int(input())
    at_list = [tuple(map(int, input().split())) for _ in range(n)]
    q = int(input())
    x_list = list(map(int, input().split()))
    res = solve(n, at_list, q, x_list)
    for r in res:
        print(r)


def test():
    assert solve(3, [(-10, 2), (10, 1), (10, 3)], 5, [-15, -10, -5, 0, 5]) == [0, 0, 5, 10, 10]


if __name__ == "__main__":
    test()
    main()
