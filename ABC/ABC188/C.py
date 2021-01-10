def solve(n, a_list):

    # find max in left
    max_i0 = -1
    max_a0 = 0
    for i in range(2 ** (n - 1)):
        a = a_list[i]
        if a > max_a0:
            max_a0 = a
            max_i0 = i + 1

    # find max in right
    max_i1 = -1
    max_a1 = 0
    for i in range(2 ** (n - 1), 2 ** n):
        a = a_list[i]
        if a > max_a1:
            max_a1 = a
            max_i1 = i + 1
    if max_a1 > max_a0:
        return max_i0
    else:
        return max_i1


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(2, [1, 4, 2, 5]) == 2
    assert solve(2, [3, 1, 5, 4]) == 1
    assert solve(4, [6, 13, 12, 5, 3, 7, 10, 11, 16, 9, 8, 15, 2, 1, 14, 4]) == 2


if __name__ == "__main__":
    test()
    main()
