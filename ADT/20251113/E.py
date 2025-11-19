def solve(n, k, a_list, b_list):
    ga = [0] * n
    gb = [0] * n
    ga[0] = 1
    gb[0] = 1
    for i in range(1, n):
        if abs(a_list[i] - a_list[i - 1]) <= k and ga[i - 1] == 1:
            ga[i] = 1
        if abs(b_list[i] - a_list[i - 1]) <= k and ga[i - 1] == 1:
            gb[i] = 1
        if abs(a_list[i] - b_list[i - 1]) <= k and gb[i - 1] == 1:
            ga[i] = 1
        if abs(b_list[i] - b_list[i - 1]) <= k and gb[i - 1] == 1:
            gb[i] = 1
    if ga[-1] == 1 or gb[-1] == 1:
        return "Yes"
    else:
        return "No"


def main():
    n, k = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    res = solve(n, k, a_list, b_list)
    print(res)


def test():
    assert solve(5, 4, [9, 8, 3, 7, 2], [1, 6, 2, 9, 5]) == "Yes"
    assert solve(4, 90, [1, 1, 1, 100], [1, 2, 3, 100]) == "No"
    assert solve(4, 1000000000, [1, 1, 1000000000, 1000000000], [1, 1000000000, 1, 1000000000]) == "Yes"


if __name__ == "__main__":
    test()
    main()
