def solve(n, d_list):
    res = 0
    for i in range(1, n + 1):
        d = d_list[i - 1]
        if 1 <= i <= 9:
            if i <= d:
                res += 1
            if i * 11 <= d:
                res += 1
        elif i % 11 == 0:
            j = i // 11
            if j <= d:
                res += 1
            if j * 11 <= d:
                res += 1
    return res


def main():
    n = int(input())
    d_list = list(map(int, input().split()))
    res = solve(n, d_list)
    print(res)


def test():
    assert solve(12, [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]) == 13
    assert solve(10, [10, 1, 2, 3, 4, 5, 6, 7, 8, 100]) == 1
    assert solve(30, [
        73, 8, 55, 26, 97, 48, 37, 47, 35, 55,
        5, 17, 62, 2, 60, 23, 99, 73, 34, 75,
        7, 46, 82, 84, 29, 41, 32, 31, 52, 32
    ]) == 15


if __name__ == "__main__":
    test()
    main()
