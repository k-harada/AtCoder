def solve(n, a_list):

    # judge_if_possible
    b_list = [0] * (n + 1)  # nodes with child

    for d in range(n + 1):
        if d == 0:
            n_nodes = 1
        else:
            n_nodes = b_list[d - 1] * 2
        if a_list[d] > n_nodes:
            return -1
        b_list[d] = n_nodes - a_list[d]
    # print(a_list, b_list)
    # backward
    b_list[n] = 0
    for i in range(n - 1, -1, -1):
        b_list[i] = min(b_list[i], a_list[i + 1] + b_list[i + 1])
    res = sum(a_list) + sum(b_list)
    # print(a_list, b_list, res)
    return res


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(3, [0, 1, 1, 2]) == 7
    assert solve(4, [0, 0, 1, 0, 2]) == 10
    assert solve(2, [0, 3, 1]) == -1
    assert solve(10, [0, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34]) == 264


if __name__ == "__main__":
    test()
    main()
