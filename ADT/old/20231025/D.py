def solve(n, a_list):
    flag_list = [0] * (n + 1)
    flag_list[0] = 1
    for i in range(1, n + 1):
        if flag_list[i] == 0:
            flag_list[a_list[i - 1]] = 1
        # print(flag_list)
    res = " ".join([str(i) for i in range(1, n + 1) if flag_list[i] == 0])
    # print(res)
    return [str(n + 1 - sum(flag_list)), res]


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    for r in res:
        print(r)


def test():
    assert solve(5, [3, 1, 4, 5, 4]) == ["2", "2 4"]
    assert solve(
        20, [9, 7, 19, 7, 10, 4, 13, 9, 4, 8, 10, 15, 16, 3, 18, 19, 12, 13, 2, 12]
    ) == ["10", "1 2 5 6 8 11 14 17 18 20"]


if __name__ == "__main__":
    test()
    main()
