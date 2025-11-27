LARGE = 10 ** 17


def solve(n, a_list):
    dp_1 = [LARGE] * (n + 1)
    dp_2 = [LARGE] * (n + 1)
    dp_1[0] = a_list[0]
    dp_1[1] = a_list[0]
    dp_2[0] = a_list[-1]
    for i in range(1, n):
        a = a_list[i]
        dp_1[i] = min(dp_1[i], dp_1[i - 1] + a)
        dp_1[i + 1] = min([dp_1[i + 1], dp_1[i - 1] + a, dp_1[i] + a])
        dp_2[i] = min(dp_2[i], dp_2[i - 1] + a)
        dp_2[i + 1] = min([dp_2[i + 1], dp_2[i - 1] + a, dp_2[i] + a])
    # print(dp_1[n - 1], dp_2[n - 2])
    return min(dp_1[n - 1], dp_2[n - 2])


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    res = solve(n, a_list)
    print(res)


def test():
    assert solve(5, [2, 5, 3, 2, 5]) == 7
    assert solve(20, [
        29, 27, 79, 27, 30,
        4, 93, 89, 44, 88,
        70, 75, 96, 3, 78,
        39, 97, 12, 53, 62
    ]) == 426


if __name__ == "__main__":
    test()
    main()
