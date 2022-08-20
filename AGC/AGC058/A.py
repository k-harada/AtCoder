def solve(n, x_list):
    y_list = x_list.copy()
    res = 0
    op_list = []
    for i in range(2 * n - 1):
        if i % 2 == 0:
            if y_list[i] > y_list[i + 1]:
                res += 1
                y_list[i], y_list[i + 1] = y_list[i + 1], y_list[i]
                op_list.append(i + 1)
        else:
            if y_list[i] < y_list[i + 1]:
                res += 1
                y_list[i], y_list[i + 1] = y_list[i + 1], y_list[i]
                op_list.append(i + 1)
        # print(res, op_list)
    # postprocess
    binary = [0] * (2 * n + 1)
    for i in op_list:
        binary[i] = 1
    switch = 0
    start = 0
    for i in range(2 * n + 1):
        if binary[i] == 1 and switch == 0:
            switch = 1
            start = i
        elif binary[i] == 0 and switch == 1:
            # print(i - 2, start - 1)
            for j in range(i - 2, start - 1, -2):
                binary[j] = 0
            switch = 0
    # print(binary)
    op_list = []
    for i in range(2 * n):
        if binary[i]:
            op_list.append(i)
    res = len(op_list)
    return res, op_list


def main():
    n = int(input())
    x_list = list(map(int, input().split()))
    res, op_list = solve(n, x_list)
    print(res)
    print(" ".join([str(op) for op in op_list]))


def test():
    assert solve(2, [4, 3, 2, 1]) == (2, [1, 3])
    assert solve(1, [1, 2]) == (0, [])


if __name__ == "__main__":
    test()
    main()
