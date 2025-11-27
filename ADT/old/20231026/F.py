def solve(n, tka_list):
    flag = [0] * (n + 1)
    flag[n] = 1
    for i in range(n, 0, -1):
        if flag[i] == 1:
            for a in tka_list[i - 1][2:]:
                flag[a] = 1
    res = 0
    for i in range(n + 1):
        if flag[i] == 1:
            res += tka_list[i - 1][0]
    return res


def main():
    n = int(input())
    tka_list = [list(map(int, input().split())) for _ in range(n)]
    res = solve(n, tka_list)
    print(res)


def test():
    assert solve(3, [[3, 0], [5, 1, 1], [7, 1, 1]]) == 10
    assert solve(5, [
        [1000000000, 0], [1000000000, 0], [1000000000, 0], [1000000000, 0], [1000000000, 4, 1, 2, 3, 4]
    ]) == 5000000000


if __name__ == "__main__":
    test()
    main()
